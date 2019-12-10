#!/usr/bin/env python
import rospy
import sys
import math
import time
from std_msgs.msg import Float64
from geometry_msgs.msg import Point

def demo():
	rospy.init_node('simple_demo',anonymous=True)
	rf_leg = rospy.Publisher('rf/point',Point,queue_size=10)
	lf_leg = rospy.Publisher('lf/point',Point,queue_size=10)
	rb_leg = rospy.Publisher('rb/point',Point,queue_size=10)
	lb_leg = rospy.Publisher('lb/point',Point,queue_size=10)
	legs = [rf_leg,lf_leg,rb_leg,lb_leg]
	for i in range(4):
		p = Point(0.2, 0, 1.5)
		legs[i].publish(p)
	time.sleep(3)
	rate = rospy.Rate(20)
	t = time.time()
	while not rospy.is_shutdown():
		for i in range(4):
			p = Point(0.2, 0, 1.5+(math.sin((time.time()-t))*0.2))
			legs[i].publish(p)
		rate.sleep()



if __name__=='__main__':
	try:
		print 'start simeple demo'
		demo()
	except rospy.ROSInterruptException:
		sys.exit()