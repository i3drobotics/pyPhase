#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2022-05-05
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file demo_match_thread.py
 @brief Example application using pyPhase
"""
#TODOC Description of the demo program
import os
import time
import datetime
import cv2
from phase.pyphase.types import CameraDeviceType, CameraInterfaceType
from phase.pyphase.types import CameraDeviceInfo, StereoMatcherType
from phase.pyphase.types import CameraReadResult
from phase.pyphase.stereocamera import createStereoCamera
from phase.pyphase.calib import StereoCameraCalibration
from phase.pyphase.stereomatcher import StereoParams, createStereoMatcher
from phase.pyphase.stereomatcher import StereoI3DRSGM
from phase.pyphase import scaleImage, normaliseDisparity


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

script_path = os.path.dirname(os.path.realpath(__file__))
data_folder = os.path.join(script_path, "..", "data")
left_yaml = os.path.join(data_folder, "left.yaml")
right_yaml = os.path.join(data_folder, "right.yaml")

license_valid = StereoI3DRSGM().isLicenseValid()
if license_valid:
    print("I3DRSGM license accepted")
else:
    print("Missing or invalid I3DRSGM license")
# Check for I3DRSGM license
if license_valid:
    stereo_params = StereoParams(
        StereoMatcherType.STEREO_MATCHER_I3DRSGM,
        9, 0, 49, False
    )
else:
    stereo_params = StereoParams(
        StereoMatcherType.STEREO_MATCHER_BM,
        11, 0, 25, False
    )

cam = createStereoCamera(device_info)
calibration = StereoCameraCalibration.calibrationFromYAML(
    left_yaml, right_yaml)
matcher = createStereoMatcher(stereo_params)

busy = False


def read_callback(read_result: CameraReadResult):
    global busy, matcher, calibration
    if not busy:
        busy = True
        if (read_result.valid):
            print("Stereo result received")
            rect = calibration.rectify(read_result.left, read_result.right)
            match_result = matcher.compute(rect.left, rect.right)
            if display_downsample != 1.0:
                img_left = scaleImage(
                    rect.left, display_downsample)
                img_right = scaleImage(
                    rect.right, display_downsample)
                img_disp = scaleImage(
                    normaliseDisparity(
                        match_result.disparity), display_downsample)
            else:
                img_left = rect.left
                img_right = rect.right
                img_disp = normaliseDisparity(match_result.disparity)
            cv2.imshow("left", img_left)
            cv2.imshow("right", img_right)
            cv2.imshow("disparity", img_disp)
            cv2.waitKey(1)
        busy = False


# cam.setReadThreadCallback(read_callback)

print("Connecting to camera...")
ret = cam.connect()
if (ret):
    cam.startCapture()
    print("Running threaded camera capture...")
    cam.startContinousReadThread()
    start = datetime.datetime.now()
    while True:
        time.sleep(1)
        capture_count = cam.getCaptureCount()
        frame_rate = cam.getFrameRate()
        print("Count {}".format(capture_count))
        print("Internal framerate {}".format(frame_rate))
        end = datetime.datetime.now()
        duration = (end - start).total_seconds()
        if duration > timeout:
            break
        if capture_count > frames:
            break
    cam.stopContinousReadThread()
    cam.disconnect()
