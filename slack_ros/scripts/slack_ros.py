#!/usr/bin/env python

# Import required Python code.
import time
import roslib
import rospy
from std_msgs.msg import String
import sys

from slackclient import SlackClient

# Node example class.
class SlackROS():
    # Must have __init__(self) function for a class, similar to a C++ class constructor.
    def __init__(self):
        # Get the ~private namespace parameters from command line or launch file.
        self.token = rospy.get_param('~token', 'xoxp-123456789')
        self.channel = rospy.get_param('~channel', 'G1234567Q')
        self.username = rospy.get_param('~username', 'ros-bot')
	
        # Create a publisher for our custom message.
        pub = rospy.Publisher('from_slack_to_ros', String, queue_size=10)
	rospy.Subscriber("from_ros_to_slack", String, self.callback)

	# Create the slack client
	self.sc = SlackClient(self.token)

	if self.sc.rtm_connect():

            # Main while loop.
            while not rospy.is_shutdown():
                for reply in self.sc.rtm_read():
                    if "type" in reply and "user" in reply:
                        #print reply
                        if reply["type"] == "message" and reply["channel"] == self.channel:
                            pub.publish(reply["text"])
                
	        # Sleep for a while before publishing new messages. Division is so rate != period.
                rospy.sleep(2.0)

    def callback(self, data):
	self.sc.api_call(
    	    "chat.postMessage", channel=self.channel, text=data.data,
    	    username=self.username, icon_emoji=':robot_face:'
	)
        #rospy.loginfo(rospy.get_caller_id() + "I heard %s %s", data.data, self.channel)


# Main function.
if __name__ == '__main__':
    # Initialize the node and name it.
    rospy.init_node('slack_ros')
    # Go to class functions that do all the heavy lifting. Do error checking.
    try:
        sr = SlackROS()
    except rospy.ROSInterruptException: pass
