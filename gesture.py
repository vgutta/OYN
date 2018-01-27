#!/usr/bin/env python3

import os, sys, time
import numpy as np

# ACC 0
# EMG 1
# EUL 2
# GYR 3
# ORT 4

f = open('check.txt')

emg = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[]}
ort = {'x':[],'y':[],'z':[],'w':[]}
acc = {'x':[],'y':[],'z':[]}
gyr = {'x':[],'y':[],'z':[]}
eur = {'r':[],'p':[],'y':[]}

for line in f:
    line = line.rstrip().split(',')
    if line[0] == '1':
        for i in range(1,8):
            emg[i-1].append(float(line[i]))

    elif line[0] == '4':
        for i,j in zip(['x','y','z','w'],range(1,5)):
            ort[i].append(float(line[j]))

    elif line[0] == '0':
        for i,j in zip(['x','y','z'],range(1,4)):
            acc[i].append(float(line[j]))

    elif line[0] == '3':
        for i,j in zip(['x','y','z'],range(1,4)):
            gyr[i].append(float(line[j]))

    elif line[0] == '2':
        for i,j in zip(['r','p','y']):
            eur[i].append(float(line[j]))

for arr in [emg,ort,acc,gyr,eur]:
    for key in arr.keys():
        arr[key] = np.array(arr[key])
            
print ("ORT")
print ("     | max      | avg     | min")
for direction in ['x','y','z','w']:
    print(direction, '|', ort[direction].max(), '|', ort[direction].mean(), '|', ort[direction].min())

lock = time.time()
    
for line in sys.stdin:
    line = line.rstrip().split(',')
    if line[0] == '3':
        if float(line[1]) <= ort['x'].max() and \
           float(line[1]) >= ort['x'].min() and \
           float(line[2]) <= ort['y'].max() and \
           float(line[2]) >= ort['y'].min() and \
           float(line[3]) <= ort['z'].max() and \
           float(line[3]) >= ort['z'].min():
            if lock < time.time()-1.5:
               os.system("say it is now `date +%I`, `date +%M`")
               print("1")
               lock = time.time()

        

sys.exit(0)


