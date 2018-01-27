#!/usr/bin/env python
'''
import os, sys

for line in sys.stdin:
    print line

sys.exit(0)
'''

import numpy as np

f = open('check.txt')

emg = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[]}
ort = {'x':[],'y':[],'z':[],'w':[]}
acc = {'x':[],'y':[],'z':[]}
gyr = {'x':[],'y':[],'z':[]}

for line in f:
    line = line.rstrip().split(',')
    if line[0] == 'EMG':
        for i in range(1,8):
            emg[i-1].append(float(line[i]))

    elif line[0] == 'ORT':
        for i,j in zip(['x','y','z','w'],range(1,5)):
            ort[i].append(float(line[j]))

    elif line[0] == 'ACC':
        for i,j in zip(['x','y','z'],range(1,4)):
            acc[i].append(float(line[j]))

    elif line[0] == 'GYR':
        for i,j in zip(['x','y','z'],range(1,4)):
            gyr[i].append(float(line[j]))

for arr in [emg,ort,acc,gyr]:
    for key in arr.keys():
        arr[key] = np.array(arr[key])
            
print "ORT"
print "     | max      | avg     | min"
for direction in ['x','y','z','w']:
    print direction, '|', ort[direction].max(), '|', ort[direction].mean(), '|', ort[direction].min()



