slack-ros-pkg
====================

General description
---------------------
ROS packages to enable communication between ROS and Slack ( https://slack.com/ ).

Node: slack_ros.py (in package slack_ros)
---------------------
#### Parameters
**token** *(string, default: xoxp-123456789)*

You have to place here, the generated token from https://api.slack.com/web#authentication (you can generate a test token for your slack team).


**channel** *(string, default: G1234567Q)*

Enter the channel where you want to speak with your bot. For example, you can type #general if your channel is public. If your channel is private, use https://api.slack.com/methods/groups.list/test to find the correct string.


**username** *(string, default: ros-bot)*

The name given to your bot in Slack.


#### Published Topics
**from_slack_to_ros** *(std_msgs::String)*   

This topic will show you what people say in the selected channel.

#### Subscribed Topics
**from_ros_to_slack** *(std_msgs::String)*   

This topic is used to send something in the selected Slack channel.
