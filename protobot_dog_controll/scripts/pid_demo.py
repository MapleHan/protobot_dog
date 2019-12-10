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
	while not rospy.is_shutdown():
		raw_input()
		p = Point(0, 0, 1.6)
		rf_leg.publish(p)
		raw_input()
		p = Point(0, 0, 1.0)
		rf_leg.publish(p)

if __name__=='__main__':
	try:
		print 'start pid demo'
		print 'press Ctrl+D exit'
		demo()
	except rospy.ROSInterruptException:
		sys.exit()