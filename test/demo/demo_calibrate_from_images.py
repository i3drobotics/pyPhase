#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2022-09-06
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file demo_calibrate_from_images.py
 @brief Example application using pyPhase generate calibration from images
"""
import os
import phase.pyphase as phase


# Define data paths
script_path = os.path.dirname(os.path.realpath(__file__))
test_folder = os.path.join(script_path, "..", ".phase_test")
data_folder = os.path.join(
    script_path, "..", "data", "checker_sample")
left_cal_folder = data_folder
right_cal_folder = data_folder
output_folder = os.path.join(test_folder, "cal")

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Define calibration files
left_yaml = os.path.join(output_folder, "left.yaml")
right_yaml = os.path.join(output_folder, "right.yaml")
left_img_wildcard = "*_l.png"
right_img_wildcard = "*_r.png"
image_type = phase.calib.CalibrationBoardType.CHECKERBOARD

# Load calibration from images
cal = phase.calib.StereoCameraCalibration.calibrationFromImages(
    left_cal_folder, right_cal_folder,
    left_img_wildcard, right_img_wildcard,
    image_type, 10, 6, 0.039)

if not cal.isValid():
    print("Calibration is invalid")

# Save calibration to YAML
save_success = cal.saveToYAML(
    left_yaml, right_yaml,
    phase.calib.CalibrationFileType.ROS_YAML)
if not save_success:
    print("Failed to save calibration to YAML")
