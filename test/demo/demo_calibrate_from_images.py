#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2022-05-05
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file demo_read.py
 @brief Example application using pyPhase
"""

import os
from phase.pyphase.calib import StereoCameraCalibration, CalibrationBoardType
from phase.pyphase.calib import CalibrationFileType

script_path = os.path.dirname(os.path.realpath(__file__))
data_folder = os.path.join(
    script_path, "..", "data", "checker_sample")

left_cal_folder = data_folder
right_cal_folder = data_folder

output_folder = "cal"
left_yaml = output_folder + "/left.yaml"
right_yaml = output_folder + "/right.yaml"
left_img_wildcard = "*_l.png"
right_img_wildcard = "*_r.png"
image_type = CalibrationBoardType.CHECKERBOARD

# Load calibration from images
cal = StereoCameraCalibration.calibrationFromImages(
    left_cal_folder, right_cal_folder,
    left_img_wildcard, right_img_wildcard,
    image_type, 10, 6, 0.039)

if not cal.isValid():
    print("Calibration is invalid")

# Save calibration to YAML
save_success = cal.saveToYAML(
    left_yaml, right_yaml,
    CalibrationFileType.ROS_YAML)
if not save_success:
    print("Failed to save calibration to YAML")
