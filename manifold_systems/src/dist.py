#!/usr/bin/env python

# dist.py -> distance for anomaly implimentation
# Caleb Little, HRL Summer 2014
# Please read all relavent information below before using 

# Version 3 : Steel Watcher
# Changes: 
# Active reaction mode (live callback) implimented

import rospy
import os.path
from numpy import *
import scipy.spatial.distance as ssd
import matplotlib.pyplot as plt
import time
from geometry_msgs.msg import WrenchStamped, Wrench
from std_msgs.msg import Float64, String
import roslib; roslib.load_manifest('manifold_systems')
from manifold_systems.srv import *

class vs:
    def Save_Everyone():
        print "You got a problem with that?"

class railer:
    def load_points(self):
        f = open('Original_Points','r')
        self.base = load(f)
        f.close()
        self.get_points = rospy.ServiceProxy('mapping',Compute)
        self.conclusion = rospy.Publisher('FT_Results', Float64)
        self.current_state = -1
        self.max_value = 0.35
        rospy.Subscriber('Current_State', String, self.status)

    def pass_me(self,i,loc,count):
        j = 1
        for a in loc:
            if a == i:
                j = 0
        return j

    def sort_min(self, data,k):
        loc = zeros(k)
        for count in range(k):
            min = 99999
            j = 0
            for i in data :
                if i < min and self.pass_me(j,loc,count) == 1:
                    min = i
                    loc[count] = j
                j = j + 1
        return loc.astype(int)

    def status(self,data):
        print "New State entered: ",data.data
        if data.data = "":
            self.current_state = 1
        elif data.data = "":
            self.current_state = 2
        elif data.data = "":
            self.current_state = 3
        elif data.data = "":
            self.current_state = 4
        elif data.data = "":
            self.current_state = 5
        elif data.data = "":
            self.current_state = 6
        elif data.data = "":
            self.current_state = 7
        elif data.data = "":
            self.current_state = 8

    def calc_dist(self, e1,e2,mode=1):
        if mode == 1:
            return ssd.euclidean(e1,e2)
        elif mode == 2:
            return ssd.cityblock(e1,e2)
        elif mode == 3:
            return ssd.cosine(e1,e2)

    def plot_points(self, data, test_case = array([0,0])):
        for i in data:
            if i[-1] == 1:
                plt.plot(i[0],i[1], 'ro')
            elif i[-1] == 2:
                plt.plot(i[0],i[1], 'b*')
            elif i[-1] == 3:
                plt.plot(i[0],i[1], 'g^')
            elif i[-1] == 4:
                plt.plot(i[0],i[1], 'mx')
	    elif i[-1] == 5:
		plt.plot(i[0],i[1], 'mo')
	    elif i[-1] == 6:
		plt.plot(i[0],i[1], 'b^')
	    elif i[-1] == 7:
		plt.plot(i[0],i[1], 'g*')
	    elif i[-1] == 8:
		plt.plot(i[0],i[1], 'rx')
        plt.plot(test_case[0],test_case[1], 'yp')
        print "Red Circle -> 1"
        print "Blue Star -> 2"
        print "Green Triangle -> 3"
        print "Magenta X -> 4"
        print "Magenta Circle -> 5"
        print "Blue Triangle -> 6"
        print "Green Star -> 7"
        print "Red X -> 8"
        plt.show()

    def dist(self, pdata, test_case = array([0,0])):
        results = array([])
        storage = array([])
        counter = 0
        for i in pdata:
            if i[2] == self.current_state:
                storage.resize((counter+1,1))
                results.resize((counter+1,2))
                storage[counter] = self.calc_dist(i[:2],test_case)
                results[counter][0] = i[0]
                results[counter][1] = i[1]
                counter = counter + 1
        sai = self.sort_min(storage,1)
        print "Distance =", storage[sai]
        return storage[sai]/self.max_value

    def main(self, data):
        print "made it up to service point"
        rospy.wait_for_service('mapping')
        pdata = self.base
        test_case = zeros(2)
        test_block = self.get_points(data.wrench.force.x,data.wrench.force.y,data.wrench.force.z,data.wrench.torque.x,data.wrench.torque.y,data.wrench.torque.z)
        test_case[0] = test_block.x
        test_case[1] = test_block.y
        #print "Current Point is:", test_case
        #self.plot_points(pdata,test_case) #Supressed for computational reasons ######################################
        start = time.clock()       
        terms = self.dist(pdata,test_case) #First number is k, second is total distinct sets in the data
        #print "time required:"
        #print time.clock()-start
        #print "Likely hood of current state:", terms
        self.conclusion.publish(terms)
        return terms

def ros_code():
    test_point = 1 # one is 100% cutoff (if dist/max_value > 1 -> too far away -> anomaly)
    rospy.init_node('dist', anonymous=True)
    print "Node Established."
    if os.path.isfile('Original_Points') == False:
        print "System cannot find Original_Points. Did you run dr.py and then obtain the resultant original points file, and is it located in the same folder as this execution?"
        return -1
    handler = railer()
    handler.load_points()
    rospy.Subscriber("/ft/l_gripper_motor", WrenchStamped, handler.main)
    f = open("DataCore", 'r')
    current = load(f)
    f.close()
                
    rospy.spin()
    
if __name__ == '__main__':
    ros_code()
