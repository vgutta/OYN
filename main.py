#!/usr/bin/env python3

import os, sys, time
import numpy as np
from gesture import Gesture

pos_files = [x for x in os.listdir(os.getcwd()) if ".pos" in x]

print(pos_files)

gestures = []

for pos in pos_files:
    gestures.append(Gesture(pos))

for gesture in gestures:
    print(gesture.name, gesture.filename)
    
lock = time.time()
    
for line in sys.stdin:
    line = line.rstrip().split(',')
    if line[0] == 'ORT':
        for gesture in gestures:
            if gesture.in_gesture(float(line[1]),float(line[2]),float(line[3])):
                if time.time()-1.5 > gesture.lock:
                    if gesture.name == 'time':
                        os.system("say it is now `date +%I`, `date +%M`")
                        print('time gesture')
                    elif gesture.name == 'dab':
                        os.system("afplay air_horn.mp3")
                        print('dab gesture')
                    elif gesture.name == 'rest':
                        print('rest gesture')
                    gesture.lock = time.time()

        
sys.exit(0)

