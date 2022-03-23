#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file demo_3d_from_image_files.py
 @brief Example application using I3DR Stereo Vision Python API
"""
import os
import sys
import cv2
import numpy as np
p = os.path.abspath('.')
sys.path.insert(1, p)
from phase.pyphase.types import CameraDeviceType, CameraInterfaceType
from phase.pyphase.types import StereoMatcherType, MatrixUInt8
from phase.pyphase.stereomatcher import StereoI3DRSGM, StereoParams
from phase.pyphase.calib import StereoCameraCalibration
from phase.pyphase import processStereo, disparity2depth


license_valid = StereoI3DRSGM().isLicenseValid()
if license_valid:
    print("I3DRSGM license accepted")
else:
    print("Missing or invalid I3DRSGM license")

script_path = os.path.dirname(os.path.realpath(__file__))
python_wrapper_proj_path = os.path.join(script_path, "../../")
phase_proj_path = os.path.join(python_wrapper_proj_path, "../../")
resource_folder = os.path.join(phase_proj_path, "resources")
# Define camera info (virtual camera for loading image files)
camera_name = "stereotheatresim"
left_serial = "0815-0000"
right_serial = "0815-0001"
device_type = CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON
interface_type = CameraInterfaceType.INTERFACE_TYPE_VIRTUAL

downsample_factor = 1.0
display_downsample = 0.25
capture_count = 5

# Define calibration files
left_yaml = os.path.join(
    resource_folder, "test", camera_name, "ros/left.yaml")
right_yaml = os.path.join(
    resource_folder, "test", camera_name, "ros/right.yaml")

# Define stereo image pair
left_image_file = os.path.join(
    resource_folder, "test", camera_name, "left.png")
right_image_file = os.path.join(
    resource_folder, "test", camera_name, "right.png")

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

# Read stereo image pair
np_left_image = cv2.imread(left_image_file, cv2.IMREAD_UNCHANGED)
np_right_image = cv2.imread(right_image_file, cv2.IMREAD_UNCHANGED)

# Convert numpy to Mat images
left_image = MatrixUInt8(np_left_image)
right_image = MatrixUInt8(np_right_image)

# Load calibration
calibration = StereoCameraCalibration.calibrationFromYAML(
    left_yaml, right_yaml)

# Process stereo
disparity = processStereo(
    stereo_params, left_image, right_image, calibration
)
if disparity.isEmpty():
    raise Exception("Failed to process stereo")

# Convert disparity to depth
np_disparity = np.array(disparity)
np_depth = disparity2depth(np_disparity, calibration.getQ())
if np_depth.size == 0:
    raise Exception("Failed to convert disparity to depth")
