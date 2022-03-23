#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file demo_mat_numpy_conversion.py
 @brief Example application using I3DR Stereo Vision Python API
"""
import os
import sys
import cv2
import numpy as np
p = os.path.abspath('.')
sys.path.insert(1, p)
from phase.pyphase.types import MatrixUInt8, StereoMatcherType
from phase.pyphase.calib import StereoCameraCalibration
from phase.pyphase.stereomatcher import StereoParams
from phase.pyphase import processStereo


script_path = os.path.dirname(os.path.realpath(__file__))
python_wrapper_proj_path = os.path.join(script_path, "../../")
phase_proj_path = os.path.join(python_wrapper_proj_path, "../../")
resource_folder = os.path.join(phase_proj_path, "resources")
camera_name = "stereotheatresim"

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

np_left_image = cv2.imread(left_image_file, cv2.IMREAD_UNCHANGED)
np_right_image = cv2.imread(right_image_file, cv2.IMREAD_UNCHANGED)

ph_left_image = MatrixUInt8(np_left_image)
ph_right_image = MatrixUInt8(np_right_image)

# Load calibration
calibration = StereoCameraCalibration.calibrationFromYAML(
    left_yaml, right_yaml)

stereo_params = StereoParams(
    StereoMatcherType.STEREO_MATCHER_BM,
    11, 0, 25, False
)
ph_disparity = processStereo(
    stereo_params,
    ph_left_image, ph_right_image, calibration
)

np_disparity = np.array(ph_disparity)
