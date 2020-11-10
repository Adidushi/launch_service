#!/usr/bin/env python

import rospy, subprocess
from launch_service.srv import str

def launch_file(names):

    command = ["roslaunch"] + names.data.split()
    subprocess.Popen(command)


if __name__ == '__main__':

    rospy.init_node('launch_service')
    s = rospy.Service('launch_service', str, launch_file)
    print("Launch service running.")
    rospy.spin()