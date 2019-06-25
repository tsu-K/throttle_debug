#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32MultiArray
from throttle_debug.msg import *


def single_array_publisher():
    rospy.init_node('single_array_publisher')
    array_size = rospy.get_param('~array_size', 10)
    publish_rate = rospy.get_param('~publish_rate', 125)
    with_header = rospy.get_param('~with_header', False)

    if with_header:
        pub = rospy.Publisher('/hoge', SingleArrayStamped, queue_size=10)
    else:
        pub = rospy.Publisher('/hoge', Float32MultiArray, queue_size=10)

    rate = rospy.Rate(publish_rate)

    while not rospy.is_shutdown():
        if with_header:
            msg = SingleArrayStamped()
        else:
            msg = Float32MultiArray()
        msg.data = [0.]*array_size
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    single_array_publisher()
