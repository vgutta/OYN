#!/usr/bin/env python

################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

import os ,sys, thread, time
src_dir = os.getcwd()
print src_dir
lib_dir = os.path.abspath(os.path.join(src_dir,'lib'))
print lib_dir
sys.path.insert(0, lib_dir)
import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture


class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']
    
    def on_init(self, controller):
        print "Initialized"
        self.lock = time.time()

    def on_connect(self, controller):
        print "Connected"

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()

#        print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
#              frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))

        # Get hands
        for hand in frame.hands:

            handType = "Left hand" if hand.is_left else "Right hand"

#            print "  %s, id %d, position: %s" % (
#                handType, hand.id, hand.palm_position)

            # Get the hand's normal vector and direction
            normal = hand.palm_normal
            direction = hand.direction

            # Calculate the hand's pitch, roll, and yaw angles
#            print "  pitch: %f degrees, roll: %f degrees, yaw: %f degrees" % (
#                direction.pitch * Leap.RAD_TO_DEG,
#                normal.roll * Leap.RAD_TO_DEG,
#                direction.yaw * Leap.RAD_TO_DEG)

            # Get arm bone
            arm = hand.arm
#            print "  Arm direction: %s, wrist position: %s, elbow position: %s" % (
#                arm.direction,
#                arm.wrist_position,
#                arm.elbow_position)
        if self.lock < time.time() - 1.5:
            if len(frame.hands) == 1:
                hand = frame.hands[0]
                if hand.is_right:
                    x = hand.direction.x
                    y = hand.direction.y
                    z = hand.direction.z
                    if hand.grab_strength == 1.0:
                        print 'a'
                    elif x > -0.15 and x < -0.14 and \
                         z < -0.98:
                        print 'b'
                    self.lock = time.time()
                    
            
        # Get tools
#        for tool in frame.tools:

#            print "  Tool id: %d, position: %s, direction: %s" % (
#                tool.id, tool.tip_position, tool.direction)


#        if not (frame.hands.is_empty and frame.gestures().is_empty):
#            print ""

    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
