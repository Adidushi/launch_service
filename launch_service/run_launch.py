#!/usr/bin/env python

import rospy, subprocess
from launch_service.srv import launchrequest, killrequest, killallrequest

class LaunchService:
    def __init__(self):
        self.counter = 0
        self.services = {}

        rospy.init_node('launch_service')
        launch = rospy.Service('launch_service', launchrequest, self.launch_file)
        kill = rospy.Service('kill_launch', killrequest, self.kill_process)
        killall = rospy.Service('kill_all', killallrequest, self.kill_all)
        print("Launch service running.")
        rospy.spin()

    def launch_file(self, data):
        package, filename = data.package, data.file
        command = ["roslaunch", package, filename]
        self.services[self.counter] = subprocess.Popen(command)
        self.counter += 1
        return self.counter - 1

    def kill_process(self, number):
        try:
            process = self.services[number.index]
            process.terminate()
            del self.services[number.index]
        except:
            return False
        return True

    def kill_all(self, _):
        count = 0
        for index in self.services.keys():
            self.services[index].terminate()
            del self.services[index]
            count += 1
        return count



if __name__ == '__main__':
    service_server = LaunchService()


