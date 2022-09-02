#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2022-05-05
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file demo_match.py
 @brief Example application using pyPhase
"""
# Demo program load stereo matching for virtual Pylon camera
import os
import cv2
from phase.pyphase.stereocamera import CameraDeviceType, CameraInterfaceType
from phase.pyphase.stereocamera import CameraDeviceInfo
from phase.pyphase.stereocamera import createStereoCamera
from phase.pyphase.calib import StereoCameraCalibration
from phase.pyphase.stereomatcher import StereoParams, createStereoMatcher
from phase.pyphase.stereomatcher import StereoI3DRSGM, StereoMatcherType
from phase.pyphase import scaleImage, normaliseDisparity, disparity2depth

# Information of the virtual camera
left_serial = "0815-0000"
right_serial = "0815-0001"
device_type = CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON
interface_type = CameraInterfaceType.INTERFACE_TYPE_VIRTUAL

# Parameters for read and display 20 frames
downsample_factor = 1.0
display_downsample = 0.25
capture_count = 20

# Create a stereo camera type variable for camera connection
device_info = CameraDeviceInfo(
    left_serial, right_serial, "virtual-camera",
    device_type,
    interface_type
)

cam = createStereoCamera(device_info)

# Define calibration files path
script_path = os.path.dirname(os.path.realpath(__file__))
data_folder = os.path.join(script_path, "..", "data")
left_yaml = os.path.join(data_folder, "left.yaml")
right_yaml = os.path.join(data_folder, "right.yaml")

# Check for I3DRSGM license
license_valid = StereoI3DRSGM().isLicenseValid()
if license_valid:
    print("I3DRSGM license accepted")
else:
    print("Missing or invalid I3DRSGM license")

# If I3DRSGM license is valid, use I3DRSGM matcher, else use OpenCV matcher
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

# Load calibration and create a stereo matcher 
calibration = StereoCameraCalibration.calibrationFromYAML(
    left_yaml, right_yaml)
matcher = createStereoMatcher(stereo_params)

# Connect camera and start data capture
print("Connecting to camera...")
ret = cam.connect()
# If camera is connected, start data capture
if (ret):
    cam.startCapture()
    print("Running non-threaded camera capture...")
    for i in range(0, capture_count):
        # Read function to read stereo pair
        read_result = cam.read()
        # Check if the stereo image pair is valid, computer matcher if valid
        if (read_result.valid):
            print("Stereo result received")
            rect = calibration.rectify(read_result.left, read_result.right)
            print("Framerate: {}".format(cam.getFrameRate()))
            match_result = matcher.compute(rect.left, rect.right)
            depth = disparity2depth(match_result.disparity, calibration.getQ())
            if depth.size == 0:
                print("Failed to convert disparity to depth")

            # Display downsampled stereo images and disparity map
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
            c = cv2.waitKey(1)
            if c == ord('q'):
                break
        else:
            cam.disconnect()
            raise Exception("Failed to read stereo result")
