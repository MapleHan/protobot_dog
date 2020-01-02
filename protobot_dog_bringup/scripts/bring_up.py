#!/usr/bin/env python
import rospy
import sys
import math
import time
import serial
from std_msgs.msg import Float64
from geometry_msgs.msg import Point
from threading import Lock
lock = Lock()
serial_com = None


def callback(data,callback_args):
  global serial_com
  lock.acquire()
  #print data,callback_args
  if(serial_com!=None):
    p = data.data
    if(callback_args==2) or (callback_args==3) or (callback_args==4) or (callback_args==5):
      p = p*-1
    serial_com.write('m '+str(callback_args)+' '+str(int(p*100)/100.0)+'\r\n')
    serial_com.flushInput()
    #time.sleep(0.05)
    #print '1:',serial_com.readline()
    #print '2:',serial_com.readline()
    #print '3:',serial_com.readline()
    #print '4:',serial_com.readline()
  lock.release()

def shutdown():
  global serial_com
  lock.acquire()
  if(serial_com!=None):
    for i in range(8):
      serial_com.write('m '+str(i)+' 0\r\n')
      time.sleep(0.01)
      serial_com.write('m '+str(i)+' 0\r\n')
      time.sleep(0.01)
    serial_com.close()
    serial_com = None
  lock.release()
  
def main():
  global serial_com
  rospy.init_node('protobot_dog',anonymous=True)
  rospy.on_shutdown(shutdown)
  port = rospy.get_param('~serial_port','/dev/ttyACM0')
  baud = rospy.get_param('~serial_baudrate',9600)
  try:
    serial_com = serial.Serial(port,baud,timeout=0.02)
    print 'serial ',port, ' open succeed at ',baud
  except Exception,e:
    print 'serial ',port, ' open failed at ',baud
    print e
    raise Exception
  time.sleep(2)
  serial_com.write('begin\r\n')
  time.sleep(2)
  serial_com.write('cd zen\r\n')
  time.sleep(2)
  print serial_com.readline()
  print serial_com.readline()
  print serial_com.readline()
  print serial_com.readline()
  serial_com.flushInput()
  rf_upper_leg = rospy.Subscriber('rf_upper_joint_position_controller/command',Float64,callback,callback_args=0,queue_size=1)
  rf_lower_leg = rospy.Subscriber('rf_lower_joint_position_controller/command',Float64,callback,callback_args=1,queue_size=1)
  lf_upper_leg = rospy.Subscriber('lf_upper_joint_position_controller/command',Float64,callback,callback_args=2,queue_size=1)
  lf_lower_leg = rospy.Subscriber('lf_lower_joint_position_controller/command',Float64,callback,callback_args=3,queue_size=1)
  rb_upper_leg = rospy.Subscriber('rb_upper_joint_position_controller/command',Float64,callback,callback_args=6,queue_size=1)
  rb_lower_leg = rospy.Subscriber('rb_lower_joint_position_controller/command',Float64,callback,callback_args=7,queue_size=1)
  lb_upper_leg = rospy.Subscriber('lb_upper_joint_position_controller/command',Float64,callback,callback_args=4,queue_size=1)
  lb_lower_leg = rospy.Subscriber('lb_lower_joint_position_controller/command',Float64,callback,callback_args=5,queue_size=1)
  rospy.spin()
  






if __name__ == '__main__':
  try:
    print 'bring up a dog'
    main()
  except rospy.ROSInterruptException:
    sys.exit()



