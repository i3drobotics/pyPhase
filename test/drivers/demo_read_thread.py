#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2022-05-05
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file demo_read_thread.py
 @brief Example application using pyPhase
"""
import time
import datetime
import cv2
from phase.pyphase.types import CameraDeviceType, CameraInterfaceType
from phase.pyphase.types import CameraDeviceInfo, CameraReadResult
from phase.pyphase.stereocamera import createStereoCamera
from phase.pyphase import scaleImage


left_serial = "0815-0000"
right_serial = "0815-0001"
device_type = CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON
interface_type = CameraInterfaceType.INTERFACE_TYPE_VIRTUAL

downsample_factor = 1.0
display_downsample = 0.25
frames = 20
timeout = 30
waitkey_delay = 1

device_info = CameraDeviceInfo(
    left_serial, right_serial, "virtual-camera",
    device_type,
    interface_type
)

cam = createStereoCamera(device_info)


def read_callback(read_result: CameraReadResult):
    if read_result.valid:
        print("Stereo result received")
        disp_image_left = scaleImage(read_result.left, 0.25)
        disp_image_right = scaleImage(read_result.right, 0.25)
        cv2.imshow("left", disp_image_left)
        cv2.imshow("right", disp_image_right)
        cv2.waitKey(waitkey_delay)
    else:
        print("Failed to read stereo result")


cam.setReadThreadCallback(read_callback)

print("Connecting to camera...")
ret = cam.connect()
if (ret):
    cam.startCapture()
    print("Running threaded camera capture...")
    cam.startContinousReadThread()
    start = datetime.datetime.now()
    capture_count = cam.getCaptureCount()
    while capture_count < frames:
        capture_count = cam.getCaptureCount()
        frame_rate = cam.getFrameRate()
        print("Count {}".format(capture_count))
        print("Internal framerate {}".format(frame_rate))
        end = datetime.datetime.now()
        duration = (end - start).total_seconds()
        if duration > timeout:
            break
        time.sleep(1)
    cam.stopContinousReadThread()
    cam.disconnect()
