#! /usr/bin/python
import roslib
roslib.load_manifest('rospy')
roslib.load_manifest('actionlib')
roslib.load_manifest('pr2_controllers_msgs')
roslib.load_manifest('geometry_msgs')

import rospy
import actionlib
from actionlib_msgs.msg import *
from pr2_controllers_msgs.msg import *
from geometry_msgs.msg import *

rospy.init_node('move_the_head', anonymous=True)

client = actionlib.SimpleActionClient(
    '/head_traj_controller/point_head_action', PointHeadAction)
client.wait_for_server()

g = PointHeadGoal()
g.target.header.frame_id = 'l_gripper_tool_frame'
g.target.point.x = 0.0
g.target.point.y = -0.3
g.target.point.z = 0.1
g.min_duration = rospy.Duration(1.0)

client.send_goal(g)
client.wait_for_result()

if client.get_state() == GoalStatus.SUCCEEDED:
    print "Succeeded"
else:
    print "Failed"

