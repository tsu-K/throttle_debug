#!/usr/bin/env python

import rospy
from throttle_debug.msg import *


def double_array_publisher():
    rospy.init_node('double_array_publisher')
    array_size_1 = rospy.get_param('~array_size_1', 10)
    array_size_2 = rospy.get_param('~array_size_2', 10)
    publish_rate = rospy.get_param('~publish_rate', 125)
    with_header = rospy.get_param('~with_header', False)

    if with_header:
        pub = rospy.Publisher('/hoge', DoubleArrayStamped, queue_size=10)
    else:
        pub = rospy.Publisher('/hoge', DoubleArray, queue_size=10)

    rate = rospy.Rate(publish_rate)

    while not rospy.is_shutdown():
        if with_header:
            msg = DoubleArrayStamped()
        else:
            msg = DoubleArray()
        msg.data1 = [0.]*array_size_1
        msg.data2 = [0.]*array_size_2
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    double_array_publisher()
