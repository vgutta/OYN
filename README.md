# OYN
MYO gestures to speech

Includes almost everything required to get started with scripting on MYO

Install [Myo Connect](https://www.myo.com/start/) to get started

## Components

myo_collect.cpp: streams live data from the MYO wristband

gesture.py: gesture python class, used to create custom gestures from calibration data

main.py: our example containing basic gestures for [HoyaHacks 2018](http://www.hoyahacks.com/)

calibrate.sh: generate data traces from gestures used to instantiate gesture objects

start.sh: pipes data from `myo_collect` to `main.py`

