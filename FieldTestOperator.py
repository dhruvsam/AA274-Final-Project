#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool


def Field_callback(data):
	rospy.loginfo("Received the following data: ")
	rospy.loginfo(data.data)

	if(data.data):
		rospy.loginfo('True received on /ready_to_rescue, sending a True on /rescue_on topic:')
		pub.publish(True)
	else:
		rospy.loginfo('Wrong value received on /ready_to_rescue, sending a False on /rescue_on topic:')
		pub.publish(False)


def FieldOperator():
	rospy.init_node('FieldTestNode', anonymous=True)
	pub = rospy.Publisher('/rescue_on', Bool, queue_size = 10)
	rospy.Subscriber('/ready_to_rescue', Bool, Field_callback)
	rospy.loginfo("Field tester node initialized ")
	rospy.spin()




if __name__ == '__main__':
    FieldOperator()
