#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file demo_read.py
 @brief Example application using pyPhase
"""
import cv2
from phase.pyphase.types import CameraDeviceType, CameraInterfaceType
from phase.pyphase.types import CameraDeviceInfo
from phase.pyphase.stereocamera import createStereoCamera
from phase.pyphase import scaleImage


left_serial = "0815-0000"
right_serial = "0815-0001"
device_type = CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON
interface_type = CameraInterfaceType.INTERFACE_TYPE_VIRTUAL

downsample_factor = 1.0
display_downsample = 0.25
capture_count = 20

device_info = CameraDeviceInfo(
    left_serial, right_serial, "virtual-camera",
    device_type,
    interface_type
)

cam = createStereoCamera(device_info)

print("Connecting to camera...")
ret = cam.connect()
if (ret):
    cam.startCapture()
    print("Running non-threaded camera capture...")
    for i in range(0, capture_count):
        read_result = cam.read()
        if (read_result.valid):
            print("Stereo result received")
            print("Framerate: {}".format(cam.getFrameRate()))
            if display_downsample != 1.0:
                img_left = scaleImage(
                    read_result.left, display_downsample)
                img_right = scaleImage(
                    read_result.right, display_downsample)
            else:
                img_left = read_result.left
                img_right = read_result.right
            cv2.imshow("left", img_left)
            cv2.imshow("right", img_right)
            cv2.waitKey(1)
        else:
            cam.disconnect()
            raise Exception("Failed to read stereo result")
