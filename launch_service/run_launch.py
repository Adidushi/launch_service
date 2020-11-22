#!/usr/bin/env python

import rospy, subprocess
from launch_service.srv import launchrequest, killrequest, killallrequest, runrequest

class LaunchService:
    def __init__(self):
        self.counter = 0
        self.services = {}

        rospy.init_node('launch_service')

        node_name = rospy.get_name()
        launch = rospy.Service(node_name + '/launch_service', launchrequest, self.launch_file)
        run = rospy.Service(node_name + '/run_service', runrequest, self.run_file)
        kill = rospy.Service(node_name + '/kill_launch', killrequest, self.kill_process)
        killall = rospy.Service(node_name + '/kill_all', killallrequest, self.kill_all)
        print("Launch service running.")
        rospy.spin()

    def launch_file(self, data):
        package, filename, args = data.package, data.file, data.args

        command = ["roslaunch", package, filename, args]
        if data.args == "":
            command = ["roslaunch", package, filename]
        if data.file == "" and data.args == "":
            command = ["roslaunch", package]
        self.services[self.counter] = subprocess.Popen(command)
        self.counter += 1
        return self.counter - 1

    def run_file(self, data):
        package, filename, args = data.package, data.file, data.args
        command = ["rosrun", package, filename, args]
        if data.file == "" and data.args == "":
            command = ["rosrun", package]
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


