#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2022-05-05
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file demo_match_thread.py
 @brief Example application using pyPhase
"""
import phase.pyphase as phase

device_infos = phase.stereocamera.availableDevices()
if len(device_infos) <= 0:
    print("No devices found")

for device_info in device_infos:
    print("*****************************")
    print("Camera Name: " + device_info.getUniqueSerial())
    print("Left Serial: " + device_info.getLeftCameraSerial())
    print("Right Serial: " + device_info.getRightCameraSerial())
