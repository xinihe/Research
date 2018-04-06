# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 22:14:01 2018

@author: Administrator
"""
import matplotlib.pyplot as plt  
import numpy as np
def kmeans(data, n, m, k):
    rarray = np.random.random(k) * n
    r = rarray.astype(int)
    center = data[r,:]
    
    cls     = np.zeros([n,1],np.int) 
    pcenter = np.zeros([k,m])

    while True:
        for i in range(n):
            tmp = data[i,:] - center
            tmp = np.square(tmp)
            tmp = np.sum(tmp,axis=1)
            cls[i] = np.argmin(tmp)
        center = np.zeros([k,m])
        count  = np.zeros([k,1],np.int)
        for i in range(n):
            center[cls[i]]=center[cls[i]]+data[i]
            count[cls[i]] += 1
        
        center = center / count
        
        if np.sum(np.square(center - pcenter)) <= 1e-4:
            break
        pcenter = center
    return center, cls

datafile = []  
fileIn = open('testdata.txt')  
for line in fileIn.readlines():  
    lineArr = line.strip().split(' ')  
    datafile.append([float(lineArr[0]), float(lineArr[-1])])
    data = np.array(datafile)
k = 4  
centroids, clusterAssment = kmeans(data, len(data), 2, k)

mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb'] 
for i in range(len(data)):  
    markIndex = int(clusterAssment[i, 0])  
    plt.plot(data[i, 0], data[i, 1], mark[markIndex])  
    # draw the centroids  
for i in range(k):  
    plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12)  
      
plt.show()  
