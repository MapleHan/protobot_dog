#!/usr/bin/env python
import rospy
import sys
import math
import time
from std_msgs.msg import Float64
from geometry_msgs.msg import Point
step_len = 1.2
step_base_hei = 1.5
step_hei = 0.2
cycle = 3.0
adjust_x = 0.2
adjust_z = 0.05

def walk():
	rospy.init_node('simple_demo',anonymous=True)
	rf_leg = rospy.Publisher('rf/point',Point,queue_size=10)
	lb_leg = rospy.Publisher('lb/point',Point,queue_size=10)
	lf_leg = rospy.Publisher('lf/point',Point,queue_size=10)
	rb_leg = rospy.Publisher('rb/point',Point,queue_size=10)
	legs = [rf_leg,rb_leg,lf_leg,lb_leg]
	for i in range(4):
		p = Point(0., 0, 1.5)
		legs[i].publish(p)
	time.sleep(3)
	rate = rospy.Rate(20)
	t = time.time()
	dp = math.pi/2
	scale = 0.2#leg up time/cycle   <=0.25
	while not rospy.is_shutdown():
		phase = ((time.time()-t)/cycle*2*math.pi) % (2*math.pi)
		for i in range(4):
			phase1 = (phase + i*dp) % (2*math.pi)
			if phase1>0 and phase1<scale*2*math.pi:
				x = math.cos(phase1/scale/2)*step_len/2
				z = step_base_hei - math.sin(phase1/scale/2)*step_hei
			else:
				x = math.cos((phase1-2*math.pi)/(1-scale)/2)*step_len/2
				z = step_base_hei
			if i%2==1:
				x = x + adjust_x
			else:
				z = z - adjust_z
			p = Point(x, 0, z)
			legs[i].publish(p)
		rate.sleep()



if __name__=='__main__':
	try:
		print 'start walk demo'
		walk()
	except rospy.ROSInterruptException:
		sys.exit()



#	while not rospy.is_shutdown():
#		phase = ((time.time()-t)/cycle*2*math.pi) % (2*math.pi)
#		adjust_x = 0.4
#		adjust_z = 0.2
#		for i in range(4):
#			phase1 = phase + i*dp
#			x = math.cos(phase1)*step_len/2
#			if phase>i*dp and phase<(i+1)*dp:
#				z = step_base_hei - math.sin(phase1*2)*step_hei
#			else:
#				z = step_base_hei
#			if i%2==1:
#				x = x + adjust_x
#			#else:
#			#	z = z - adjust_z
#			#print phase,x,z