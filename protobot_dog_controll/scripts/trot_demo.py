#!/usr/bin/env python
import rospy
import sys
import math
import time
from std_msgs.msg import Float64
from geometry_msgs.msg import Point
step_len = 0.8
step_base_hei = 1.5
step_hei = 0.2
cycle = 2
adjust_x = 0.4
adjust_z = 0.15

def trot():
	rospy.init_node('simple_demo',anonymous=True)
	rf_leg = rospy.Publisher('rf/point',Point,queue_size=10)
	lb_leg = rospy.Publisher('lb/point',Point,queue_size=10)
	lf_leg = rospy.Publisher('lf/point',Point,queue_size=10)
	rb_leg = rospy.Publisher('rb/point',Point,queue_size=10)
	legs = [rf_leg,lb_leg,lf_leg,rb_leg]
	for i in range(4):
		p = Point(0, 0, 1.5)
		legs[i].publish(p)
	time.sleep(3)
	rate = rospy.Rate(20)
	t = time.time()
	dp = math.pi
	scale = 0.4#leg up time/cycle  <=0.5
	while not rospy.is_shutdown():
		phase = ((time.time()-t)/cycle*2*math.pi) % (2*math.pi)
		for i in range(2):
			phase1 = (phase + i*dp) % (2*math.pi)
			if phase1>0 and phase1<scale*2*math.pi:
				x = math.cos(phase1/scale/2)*step_len/2
				z = step_base_hei - math.sin(phase1/scale/2)*step_hei
			else:
				x = math.cos((phase1-2*math.pi)/(1-scale)/2)*step_len/2
				z = step_base_hei
			#print phase,x,z
			p0 = Point(x, 0, z-adjust_z)
			p1 = Point(x+adjust_x, 0, z)
			legs[2*i].publish(p0)
			legs[2*i+1].publish(p1)
		rate.sleep()



if __name__=='__main__':
	try:
		print 'start trot demo'
		trot()
	except rospy.ROSInterruptException:
		sys.exit()