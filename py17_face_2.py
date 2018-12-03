#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 13:56:21 2018

@author: wisdomimac

1- 读入点云文件
2- 将点云作为数组
3- 画图


"""


from __future__ import print_function
#import csv
import numpy as np
import pandas as pd
import random

from mpl_toolkits.mplot3d import Axes3D


def plane_color(pl,colorn):
    plane=pd.DataFrame()
    plane= pd.DataFrame({'x':pl[:,0],'y':pl[:,1],'z':pl[:,2],'color':colorn})
    print(plane)
    return (plane)



#my_matrix = np.loadtxt(open("095927_R-fixed-left.csv","rb"),delimiter=",",skiprows=0)  

 
left_plane_1 = np.loadtxt(open("face_l.asc","rb"),delimiter=" ",skiprows=0)  
left_plane_2 = np.loadtxt(open("face_m.asc","rb"),delimiter=" ",skiprows=0)  
left_plane_3 = np.loadtxt(open("face_50.asc","rb"),delimiter=" ",skiprows=0)  
left_plane_4 = np.loadtxt(open("face_70.asc","rb"),delimiter=" ",skiprows=0)  

#left_plane= random.sample(left_plane, 10000)
# 从160000个点中,随机提取1000个点

#left_plane= left_plane[np.random.randint(0, 48547, 1000)]


plane2= plane_color(left_plane_1,"g")
plane3= plane_color(left_plane_2,"b")
plane4= plane_color(left_plane_3,"r")
plane5= plane_color(left_plane_4,"y")

plane = pd.DataFrame({'x':left_plane_1[:,0],'y':left_plane_1[:,1],'z':left_plane_1[:,2],'color':'g'})
plane1 = pd.DataFrame({'x':left_plane_1[:,0],'y':left_plane_1[:,1],'z':left_plane_1[:,2],'color':'g'})

left_plane=np.append(plane2,plane3,axis=0)
left_plane=np.append(left_plane,plane4,axis=0)
left_plane=np.append(left_plane,plane5,axis=0)


plane.to_csv("plane_20.csv")

plane1= pd.DataFrame()

plane1.x = plane.x
plane1.y=plane.y
plane1.z=plane.z-1

        
np.savetxt('new.csv', left_plane_1, delimiter = ',')  


# x轴的采样点
#x = zhuanzhi[0]
#y= zhuanzhi[1]
#z= zhuanzhi[2]

z_mean = np.mean(left_plane_1[:,2])



import matplotlib.pyplot as plt

upper_samples = []
lower_samples = []
upper_samples_c = []
lower_samples_c = []


for c,x, y, z in left_plane:
    # x_mean 作为判别平面
    if z > z_mean:
        upper_samples.append((x, y, z))
        upper_samples_c.append((c))
    else:
        lower_samples.append((x, y, z))
        lower_samples_c.append((c))
 
uppers = np.array(upper_samples)
lowers = np.array(lower_samples)

print("uppers len is:", np.size(uppers)) 
print("lower len is:", np.size(lowers))
print("left_plane descrip:",plane.describe() )
 
# '.'标明画散点图，每个散点的形状是个圆
plt.plot(left_plane_1[:,2], left_plane_1[:,0], '.')
plt.plot(left_plane_1[:,1], left_plane_1[:,2], '.')



#fig = plt.figure('3D scatter plot')
#ax = fig.add_subplot(111, projection='3d')

######


ax = plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程
#  将数据点分成三部分画，在颜色上有区分度
ax.scatter(uppers[:, 0], uppers[:, 1], uppers[:, 2], c=upper_samples_c, marker='o')
ax.scatter(lowers[:, 0], lowers[:, 1], lowers[:, 2], c=lower_samples_c, marker='^')


ax.set_zlabel('Z')  # 坐标轴
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()


# 将平面下移动一个单位， 因为点云的Z数据mean是1
# ax.scatter(plane1.x, plane1.y, plane1.z, c='b', marker='^')
 
plt.show()
