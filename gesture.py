#!/usr/bin/env python3

import numpy as np
import time

class Gesture:
    def __init__(self, filename):
        emg = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[]}
        ort = {'x':[],'y':[],'z':[],'w':[]}
        acc = {'x':[],'y':[],'z':[]}
        gyr = {'x':[],'y':[],'z':[]}
        self.lock = time.time()
        self.name = filename[:-4]
        self.filename = filename
        print(self.name)
        f = open(filename)
        for line in f:
            line = line.rstrip().split(',')
            if line[0] == 'EMG':
                for i in range(1,9):
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

        self.ort = ort
        self.emg = emg
        self.acc = acc
        self.gyr = gyr

        for i in range(8):
            print(self.emg[i].max(),self.emg[i].mean(),self.emg[i].min())
                
    def in_position(self,x,y,z):
        return x <= self.ort['x'].max() and \
            x >= self.ort['x'].min() and \
            y <= self.ort['y'].max() and \
            y >= self.ort['y'].min() and \
            z <= self.ort['z'].max() and \
            z >= self.ort['z'].min()

    def in_flex(self,emg):
        valid = True
        for sensor,config in zip(emg,self.emg.keys()):
            valid = valid and \
                    sensor <= self.emg[config].max() and \
                    sensor >= self.emg[config].min()

        return valid
