#!/usr/bin/env python

# dr.py -> dimesion reduction system
# Caleb Little, HRL Summer 2014
# Please read all relavent information below before using
# Please note: In order to utilize MiniSom properly, you will need a 
# modified and recompiled MiniSom file. The modifcations can be
# obtained from me.

# Version 3: What.
# Changes:
# Incorporated size-6/count-8 data sets (currently Force Torque)

import numpy as np
from minisom import MiniSom 
from sklearn import manifold, datasets, decomposition, ensemble, lda, random_projection
import pylab as pl
import cPickle as pickle

# Controls Section:
window_control = 0.7 #Controls scaling for graphing
mode = 2 #Selects Dimension Reduction:1 = SOM, 2 = LLE, 3 = PCA, 4 = Isomap
fresh_data = 1 #Allows for storage: 1 = recalculate, 0 = load old data
#

class vs:
    def init(self, data):
        self.a = 1

# Data Setup section:
# (currently utilizes scikit learn datasets)
#digits = datasets.load_digits(n_class=4)
#data = digits.data # matrix where each row is a vector that represent a digit.
#num = digits.target # num[i] is the digit represented by data[i]
#n_samples, n_features = data.shape
n_neighbors = 5

######################################
f = open ('DataCore','r')
tacitus = vs()
tacitus = pickle.load(f)
f.close()

print "loaded data core"
data = tacitus.cv_21
num = tacitus.cv_21w
n_samples, n_features = data.shape
######################################

# Functional Code Below:
if mode == 1:
    print "Using SOM"
    drmap = MiniSom(50,50,6,sigma=.8,learning_rate=.5) # Replace 64 with the dimensions of desired target (6)
    if fresh_data == 1:
        print "Training..."
        drmap.train_random(data,1500) # random training
        print "\n...ready!"
    elif fresh_data == 0:
        print "Loading Data"
        drmap.load_map()

    # plotting the results
    from pylab import text,show,cm,axis,figure,subplot,imshow,zeros
    figure(1)
    im = 0
    result = np.array([])
    for x,t in zip(data,num): # scatterplot
     w = drmap.winner(x)
     result.resize((im+1,3))
     result[im][0]=w[0]
     result[im][1]=w[1]
     result[im][2]=num[im]
     text(w[0]+.5, w[1]+.5, str(t), color=cm.Dark2(t / 8.), fontdict={'weight': 'bold', 'size': 11})
     im = im + 1
     axis([0,drmap.weights.shape[0],0,drmap.weights.shape[1]])

    # Save SOM file
    drmap.save_map()

else:
    if mode == 2:
        print "Using LLE"
        construct = manifold.LocallyLinearEmbedding(n_neighbors, n_components=2, method='standard')
        if fresh_data == 1:
            print "Training..."
            drmap = construct.fit(data)
            print "\n...ready!"
            f = open('LLE','w')
            pickle.dump(drmap,f)
            f.close()
        else:
            print "Loading Data"
            f = open('LLE', 'r')
            drmap = pickle.load(f)
            f.close()
            
    elif mode == 3:
        print "Using PCA"
        construct = decomposition.TruncatedSVD(n_components=2)
        if fresh_data == 1:
            print "Training..."
            drmap = construct.fit(data)
            print "\n...ready!"
            f = open('PCA','w')
            pickle.dump(drmap,f)
            f.close()
        else:
            print "Loading Data"
            f = open('PCA','r')
            drmap = pickle.load(f)
            f.close()

    elif mode == 4:
        print "Using Isomap"
        construct = manifold.Isomap(n_neighbors, n_components=2)
        if fresh_data == 1:
            print "Training..."
            drmap = construct.fit(data)
            print "\n...ready!"
            f = open('Isomap','w')
            pickle.dump(drmap,f)
            f.close()
        else:
            print "Loading Data"
            f = open('Isomap','r')
            drmap = pickle.load(f)
            f.close()

    from pylab import text,show,cm,axis,figure,subplot,imshow,zeros
    figure(1)
    im = 0
    result = np.array([])
    for x,t in zip(data,num): # scatterplot
     if mode == 4:
         x = np.array([x])
     w = drmap.transform(x)
     result.resize((im+1,3))
     result[im][0]=w[0][0]
     result[im][1]=w[0][1]
     result[im][2]=num[im]
     text(w[0][0]+.5, w[0][1]+.5, str(t), color=cm.Dark2(t / 8.), fontdict={'weight': 'bold', 'size': 11})
     im = im + 1
    x_min = np.amin(result[:,0])
    x_max = np.amax(result[:,0])
    y_min = np.amin(result[:,1])
    y_max = np.amax(result[:,1])
    if mode != 2:
        axis([x_min,x_max,y_min,y_max])
    else:
        axis([0,x_max+window_control,0,y_max+window_control])

show()
f = open('Original_Points','w')
np.save(f,result)
f.close()
