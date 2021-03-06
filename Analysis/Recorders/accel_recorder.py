from __future__ import division
import roslib; roslib.load_manifest('pr2_msgs')
import numpy as np
import rospy
from collections import deque
from geometry_msgs.msg import Vector3
from pr2_msgs.msg import AccelerometerState 
from std_msgs.msg import String, Header, Time
import math

hand="l"

class accel_recorder ():
    def init(self):
        self.num=input("Enter Trial Number: ")
        rospy.init_node('Accel_listener', anonymous=False)
        self.amag=deque([])
        self.accel_x=deque([])
        self.accel_y=deque([])
        self.accel_z=deque([])
        self.accel_t=deque([])
        self.accel_tn=deque([])
        self.xfname="./Trial/Trial%s_ax_part"%self.num
        self.yfname="./Trial/Trial%s_ay_part"%self.num
        self.zfname="./Trial/Trial%s_az_part"%self.num
        self.tfname="./Trial/Trial%s_at_part"%self.num
        self.magname="./Trial/Trial%s_amag_part"%self.num
        self.part="-1"
        self.file0x=open(self.xfname + "0", "w")
        self.file0y=open(self.yfname + "0", "w")
        self.file0z=open(self.zfname + "0", "w")
        self.file0t=open(self.tfname + "0", "w")
        self.file0a=open(self.magname + "0", "w") 
        self.file1x=open(self.xfname + "1", "w")
        self.file1y=open(self.yfname + "1", "w")
        self.file1z=open(self.zfname + "1", "w")
        self.file1t=open(self.tfname + "1", "w")
        self.file1a=open(self.magname + "1", "w") 
        self.file2x=open(self.xfname + "2", "w")
        self.file2y=open(self.yfname + "2", "w")
        self.file2z=open(self.zfname + "2", "w")
        self.file2t=open(self.tfname + "2", "w")
        self.file2a=open(self.magname + "2", "w")
        self.file3x=open(self.xfname + "3", "w")
        self.file3y=open(self.yfname + "3", "w")
        self.file3z=open(self.zfname + "3", "w")
        self.file3t=open(self.tfname + "3", "w")
        self.file3a=open(self.magname + "3", "w")
        self.file4x=open(self.xfname + "4", "w")
        self.file4y=open(self.yfname + "4", "w")
        self.file4z=open(self.zfname + "4", "w")
        self.file4t=open(self.tfname + "4", "w")
        self.file4a=open(self.magname + "4", "w")
        self.file5x=open(self.xfname + "5", "w")
        self.file5y=open(self.yfname + "5", "w")
        self.file5z=open(self.zfname + "5", "w")
        self.file5t=open(self.tfname + "5", "w")
        self.file5a=open(self.magname + "5", "w")
        self.file6x=open(self.xfname + "6", "w")
        self.file6y=open(self.yfname + "6", "w")
        self.file6z=open(self.zfname + "6", "w")
        self.file6t=open(self.tfname + "6", "w")
        self.file6a=open(self.magname + "6", "w")
        self.file7x=open(self.xfname + "7", "w")
        self.file7y=open(self.yfname + "7", "w")
        self.file7z=open(self.zfname + "7", "w")
        self.file7t=open(self.tfname + "7", "w")
        self.file7a=open(self.magname + "7", "w")
        self.file8x=open(self.xfname + "8", "w")
        self.file8y=open(self.yfname + "8", "w")
        self.file8z=open(self.zfname + "8", "w")
        self.file8t=open(self.tfname + "8", "w")
        self.file8a=open(self.magname + "8", "w")
        self.file9x=open(self.xfname + "9", "w")
        self.file9y=open(self.yfname + "9", "w")
        self.file9z=open(self.zfname + "9", "w")
        self.file9t=open(self.tfname + "9", "w")
        self.file9a=open(self.magname + "9", "w")
        self.file10x=open(self.xfname + "10", "w")
        self.file10y=open(self.yfname + "10", "w")
        self.file10z=open(self.zfname + "10", "w")
        self.file10t=open(self.tfname + "10", "w")
        self.file10a=open(self.magname + "10", "w")
        self.file11x=open(self.xfname + "11", "w")
        self.file11y=open(self.yfname + "11", "w")
        self.file11z=open(self.zfname + "11", "w")
        self.file11t=open(self.tfname + "11", "w")
        self.file11a=open(self.magname + "11", "w")
        self.message='b'
        rospy.Subscriber("/accelerometer/%s_gripper_motor"%hand, AccelerometerState, self.callback)
        rospy.Subscriber('Main_Control', String, self.listen)
        
        self.r=rospy.Rate(10) #in hz
        
        
    def callback(self, msg):
        x=[] 
        y=[]
        z=[]
        for i in range(len(msg.samples)):   #grab messages from accelerometer (usually publishes 3 samples per 
            x.append(msg.samples[i].x)      #ROS message)
            y.append(msg.samples[i].y)
            z.append(msg.samples[i].z)
        self.accel_t.append(msg.header.stamp.secs)
        self.accel_tn.append(msg.header.stamp.nsecs)
        if self.message is 'b':
            self.t0=self.accel_t[0]
            self.message='e'
        self.accel_x.append(np.average(x))  #average the samples from the message 
        self.accel_y.append(np.average(y))
        self.accel_z.append(np.average(z))
        self.worknstuff()
    
    def listen(self, msg):
        self.message=msg.data                   #grab message to see which subtask is being performed 
        #if self.message is "Part0":
        #    self.part="0"
        #elif self.message is "Part1":
        #    self.part="1"
        #elif self.message is "Part2":
        #    self.part="2"
        #elif self.message is "Part3":
        #    self.part="3"
        #elif self.message is "Part4":
        #    self.part="4"
        #elif self.message is "Part5":
        #    self.part="5"
        #elif self.message is "Part6":
        #    self.part="6"
        #elif self.message is "Part7":
        #    self.part="7"
        #elif self.message is "Part8":
        #    self.part="8"
        #elif self.message is "Part9":
        #    self.part="9"
        if self.message[-2] is 't':
            self.part=self.message[-1]
        else:
            if self.message[-1] is '0': 
                self.part='10'
            elif self.message[-1] is '1':
                self.part='11'          
            
        
        if self.message[-1] is 'P':
            print("Stop recording")
            self.closefiles()
        
        print(self.part)
        self.worknstuff()           
            
    def worknstuff (self):
        #Calculate magnitude of the newest point and add to magnitude deque 
        if len(self.accel_x)>=1:
            self.amag.append(math.sqrt(self.accel_x[-1]**2+self.accel_y[-1]**2+self.accel_z  [-1]**2))
          
        
        index=range(0, len(self.accel_x))
        magindex=range(0, len(self.amag)) 
        if self.part is "0":               #write each subtask to a file
            for i in index:
                a=self.accel_x.popleft()
                self.file0x.write(str(a)+'\n')
                b=self.accel_y.popleft()
                self.file0y.write(str(b)+'\n')
                c=self.accel_z.popleft()
                self.file0z.write(str(c)+'\n')
                d=self.accel_t.popleft() + (10**-9)*(self.accel_tn.popleft())-self.t0
                self.file0t.write(str(d)+'\n')
            for i in magindex:
                e=self.amag.popleft()
                self.file0a.write(str(e)+'\n')
        if self.part is "1": 
            for i in index:
                a=self.accel_x.popleft()
                self.file1x.write(str(a)+'\n')
                b=self.accel_y.popleft()
                self.file1y.write(str(b)+'\n')
                c=self.accel_z.popleft()
                self.file1z.write(str(c)+'\n')
                d=self.accel_t.popleft() + (10**-9)*(self.accel_tn.popleft())-self.t0
                self.file1t.write(str(d)+'\n')
            for i in magindex: 
                e=self.amag.popleft()
                self.file1a.write(str(e)+'\n')
        if self.part is "2": 
            for i in index:
                a=self.accel_x.popleft()
                self.file2x.write(str(a)+'\n')
                b=self.accel_y.popleft()
                self.file2y.write(str(b)+'\n')
                c=self.accel_z.popleft()
                self.file2z.write(str(c)+'\n')
                d=self.accel_t.popleft() + (10**-9)*(self.accel_tn.popleft())-self.t0
                self.file2t.write(str(d)+'\n')
            for i in magindex:     
                e=self.amag.popleft()
                self.file2a.write(str(e)+'\n')
        if self.part is "3":
             for i in index:
                a=self.accel_x.popleft()
                self.file3x.write(str(a)+'\n')
                b=self.accel_y.popleft()
                self.file3y.write(str(b)+'\n')
                c=self.accel_z.popleft()
                self.file3z.write(str(c)+'\n')
                d=self.accel_t.popleft() + (10**-9)*(self.accel_tn.popleft())-self.t0
                self.file3t.write(str(d)+'\n')
             for i in magindex:    
                e=self.amag.popleft()
                self.file3a.write(str(e)+'\n')
        if self.part is "4":        
             for i in index:
                a=self.accel_x.popleft()
                self.file4x.write(str(a)+'\n')
                b=self.accel_y.popleft()
                self.file4y.write(str(b)+'\n')
                c=self.accel_z.popleft()
                self.file4z.write(str(c)+'\n')
                d=self.accel_t.popleft() + (10**-9)*(self.accel_tn.popleft())-self.t0
                self.file4t.write(str(d)+'\n')
             for i in magindex:    
                e=self.amag.popleft()
                self.file4a.write(str(e)+'\n')
        if self.part is "5":        
            for i in index:
                a=self.accel_x.popleft()
                self.file5x.write(str(a)+'\n')
                b=self.accel_y.popleft()
                self.file5y.write(str(b)+'\n')
                c=self.accel_z.popleft()
                self.file5z.write(str(c)+'\n')
                d=self.accel_t.popleft() + (10**-9)*(self.accel_tn.popleft())-self.t0
                self.file5t.write(str(d)+'\n')
            for i in magindex:    
                e=self.amag.popleft()
                self.file5a.write(str(e)+'\n')    
   
        if self.part is "6":
            for i in index:
                a=self.accel_x.popleft()
                self.file6x.write(str(a)+'\n')
                b=self.accel_y.popleft()
                self.file6y.write(str(b)+'\n')
                c=self.accel_z.popleft()
                self.file6z.write(str(c)+'\n')
                d=self.accel_t.popleft() + (10**-9)*(self.accel_tn.popleft())-self.t0
                self.file6t.write(str(d)+'\n')
            for i in magindex:    
                e=self.amag.popleft()
                self.file6a.write(str(e)+'\n')
        if self.part is "7":        
            for i in index:
                a=self.accel_x.popleft()
                self.file7x.write(str(a)+'\n')
                b=self.accel_y.popleft()
                self.file7y.write(str(b)+'\n')
                c=self.accel_z.popleft()
                self.file7z.write(str(c)+'\n')
                d=self.accel_t.popleft() + (10**-9)*(self.accel_tn.popleft())-self.t0
                self.file7t.write(str(d)+'\n')
            for i in magindex:    
                e=self.amag.popleft()
                self.file7a.write(str(e)+'\n')
        if self.part is "8":        
            for i in index:
                a=self.accel_x.popleft()
                self.file8x.write(str(a)+'\n')
                b=self.accel_y.popleft()
                self.file8y.write(str(b)+'\n')
                c=self.accel_z.popleft()
                self.file8z.write(str(c)+'\n')
                d=self.accel_t.popleft() + (10**-9)*(self.accel_tn.popleft())-self.t0
                self.file8t.write(str(d)+'\n')
            for i in magindex:    
                e=self.amag.popleft()
                self.file8a.write(str(e)+'\n')
        if self.part is "9":        
            for i in index:
                a=self.accel_x.popleft()
                self.file9x.write(str(a)+'\n')
                b=self.accel_y.popleft()
                self.file9y.write(str(b)+'\n')
                c=self.accel_z.popleft()
                self.file9z.write(str(c)+'\n')
                d=self.accel_t.popleft() + (10**-9)*(self.accel_tn.popleft())-self.t0
                self.file9t.write(str(d)+'\n')
            for i in magindex:    
                e=self.amag.popleft()
                self.file9a.write(str(e)+'\n')
        if self.part is "10":        
            for i in index:
                a=self.accel_x.popleft()
                self.file10x.write(str(a)+'\n')
                b=self.accel_y.popleft()
                self.file10y.write(str(b)+'\n')
                c=self.accel_z.popleft()
                self.file10z.write(str(c)+'\n')
                d=self.accel_t.popleft() + (10**-9)*(self.accel_tn.popleft())-self.t0
                self.file10t.write(str(d)+'\n')
            for i in magindex:    
                e=self.amag.popleft()
                self.file10a.write(str(e)+'\n')
        if self.part is "11":        
            for i in index:
                a=self.accel_x.popleft()
                self.file11x.write(str(a)+'\n')
                b=self.accel_y.popleft()
                self.file11y.write(str(b)+'\n')
                c=self.accel_z.popleft()
                self.file11z.write(str(c)+'\n')
                d=self.accel_t.popleft() + (10**-9)*(self.accel_tn.popleft())-self.t0
                self.file11t.write(str(d)+'\n')
            for i in magindex:    
                e=self.amag.popleft()
                self.file11a.write(str(e)+'\n')
        
    def closefiles(self):
		print("*closing files")
		self.file0x.close	#close all the files
		self.file0y.close
		self.file0z.close
		self.file0t.close
		self.file0a.close 
		self.file1x.close
		self.file1y.close
		self.file1z.close
		self.file1t.close
		self.file1a.close 
		self.file2x.close
		self.file2y.close
		self.file2z.close
		self.file2t.close
		self.file2a.close
		self.file3x.close
		self.file3y.close
		self.file3z.close
		self.file3t.close
		self.file3a.close
		self.file4x.close
		self.file4y.close
		self.file4z.close
		self.file4t.close
		self.file4a.close
		self.file5x.close
		self.file5y.close
		self.file5z.close
		self.file5t.close
		self.file5a.close
		self.file6x.close
		self.file6y.close
		self.file6z.close
		self.file6t.close
		self.file6a.close
		self.file7x.close
		self.file7y.close
		self.file7z.close
		self.file7t.close
		self.file7a.close
		self.file8x.close
		self.file8y.close
		self.file8z.close
		self.file8t.close
		self.file8a.close
		self.file9x.close
		self.file9y.close
		self.file9z.close
		self.file9t.close
		self.file9a.close
		self.file10x.close
		self.file10y.close
		self.file10z.close
		self.file10t.close
		self.file10a.close
		self.file11x.close
		self.file11y.close
		self.file11z.close
		self.file11t.close
		self.file11a.close 
   
if __name__=='__main__':
	callthis=accel_recorder()
	callthis.init()
	while not rospy.is_shutdown():
		rospy.spin()
