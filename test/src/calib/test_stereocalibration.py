#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-06-28
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_stereocalibration.py
 @brief Unit tests for StereoCameraCalibration class
 @details Unit tests generated using PyTest
"""
import os
from phase.pyphase.calib import StereoCameraCalibration, CalibrationFileType


def test_LoadCalibration():
    script_path = os.path.dirname(os.path.realpath(__file__))
    python_wrapper_proj_path = os.path.join(script_path, "../../../")
    phase_proj_path = os.path.join(python_wrapper_proj_path, "../../")
    resource_folder = os.path.join(phase_proj_path, "resources")
    camera_name = "stereotheatresim"
    cam_folder = os.path.join(resource_folder, "test", camera_name)
    left_ros_yaml = os.path.join(cam_folder, "ros/left.yaml")
    right_ros_yaml = os.path.join(cam_folder, "ros/right.yaml")
    left_cv_yaml = os.path.join(cam_folder, "cv/left.yaml")
    right_cv_yaml = os.path.join(cam_folder, "cv/right.yaml")

    cal_ros = StereoCameraCalibration.calibrationFromYAML(
        left_ros_yaml, right_ros_yaml)
    assert(cal_ros.isValid())

    cal_cv = StereoCameraCalibration.calibrationFromYAML(
        left_cv_yaml, right_cv_yaml)
    assert(cal_cv.isValid())


def test_SaveCalibration():
    script_path = os.path.dirname(os.path.realpath(__file__))
    python_wrapper_proj_path = os.path.join(script_path, "../../../")
    phase_proj_path = os.path.join(python_wrapper_proj_path, "../../")
    resource_folder = os.path.join(phase_proj_path, "resources")
    out_folder = os.path.join(python_wrapper_proj_path, "out")
    camera_name = "stereotheatresim"
    cam_folder = os.path.join(resource_folder, "test", camera_name)
    left_yaml = os.path.join(cam_folder, "ros/left.yaml")
    right_yaml = os.path.join(cam_folder, "ros/right.yaml")

    cal = StereoCameraCalibration.calibrationFromYAML(left_yaml, right_yaml)
    assert(cal.isValid())

    cal.saveToYAML(
        os.path.join(out_folder, "left_ros.yaml"),
        os.path.join(out_folder, "right_ros.yaml"),
        CalibrationFileType.ROS_YAML)
    cal.saveToYAML(
        os.path.join(out_folder, "left_cv.yaml"),
        os.path.join(out_folder, "right_cv.yaml"),
        CalibrationFileType.OPENCV_YAML)
