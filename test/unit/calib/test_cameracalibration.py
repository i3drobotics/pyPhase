#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-06-28
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_cameracalibration.py
 @brief Unit tests for CameraCalibration class
 @details Unit tests for use with PyTest
"""
import os
import numpy as np
from phase.pyphase import readImage
from phase.pyphase.calib import CameraCalibration


def test_CameraCalibration():
    # Test loading of calibration data from file
    script_path = os.path.dirname(os.path.realpath(__file__))
    test_folder = os.path.join(script_path, "..", "..", ".phase_test")
    left_ros_yaml = os.path.join(test_folder, "left_ros.yaml")
    left_cv_yaml = os.path.join(test_folder, "left_cv.yaml")

    print("Generating test data...")
    # Create calibration files
    left_ros_yaml_data = \
        "image_width: 2448\n" \
        "image_height: 2048\n" \
        "camera_name: leftCamera\n" \
        "camera_matrix:\n" \
        "   rows: 3\n" \
        "   cols: 3\n" \
        "   data: [ 3.4782608695652175e+03, 0., 1224., 0., 3.4782608695652175e+03, 1024., 0., 0., 1. ]\n" \
        "distortion_model: plumb_bob\n" \
        "distortion_coefficients:\n" \
        "   rows: 1\n" \
        "   cols: 5\n" \
        "   data: [ 0., 0., 0., 0., 0. ]\n" \
        "rectification_matrix:\n" \
        "   rows: 3\n" \
        "   cols: 3\n" \
        "   data: [1., 0., 0., 0., 1., 0., 0., 0., 1.]\n" \
        "projection_matrix:\n" \
        "   rows: 3\n" \
        "   cols: 4\n" \
        "   data: [ 3.4782608695652175e+03, 0., 1224., 0., 0., 3.4782608695652175e+03, 1024., 0., 0., 0., 1., 0. ]\n"

    left_cv_yaml_data = \
        "%YAML:1.0\n" \
        "---\n" \
        "image_width: 2448\n" \
        "image_height: 2048\n" \
        "camera_name: leftCamera\n" \
        "camera_matrix: !!opencv-matrix\n" \
        "   rows: 3\n" \
        "   cols: 3\n" \
        "   dt: d\n" \
        "   data: [ 3.4782608695652175e+03, 0., 1224., 0., 3.4782608695652175e+03, 1024., 0., 0., 1. ]\n" \
        "distortion_model: plumb_bob\n" \
        "distortion_coefficients: !!opencv-matrix\n" \
        "   rows: 1\n" \
        "   cols: 5\n" \
        "   dt: d\n" \
        "   data: [ 0., 0., 0., 0., 0. ]\n" \
        "rectification_matrix: !!opencv-matrix\n" \
        "   rows: 3\n" \
        "   cols: 3\n" \
        "   dt: d\n" \
        "   data: [1., 0., 0., 0., 1., 0., 0., 0., 1.]\n" \
        "projection_matrix: !!opencv-matrix\n" \
        "   rows: 3\n" \
        "   cols: 4\n" \
        "   dt: d\n" \
        "   data: [ 3.4782608695652175e+03, 0., 1224., 0., 0., 3.4782608695652175e+03, 1024., 0., 0., 0., 1., 0. ]\n" \
        "rms_error: ""\n"

    with open(left_ros_yaml, 'w') as f:
        f.writelines(left_ros_yaml_data)

    cal_ros = CameraCalibration(left_ros_yaml)
    assert(cal_ros.isValid())

    with open(left_cv_yaml, "w+") as f:
        f.writelines(left_cv_yaml_data)

    cal_cv = CameraCalibration(left_cv_yaml)
    assert(cal_cv.isValid())

    # Test calibration access
    assert(len(cal_ros.getCameraMatrix()) > 0)
    assert(len(cal_ros.getDistortionCoefficients()) > 0)
    assert(len(cal_ros.getRectificationMatrix()) > 0)
    assert(len(cal_ros.getProjectionMatrix()) > 0)

    assert(len(cal_cv.getCameraMatrix()) > 0)
    assert(len(cal_cv.getDistortionCoefficients()) > 0)
    assert(len(cal_cv.getRectificationMatrix()) > 0)
    assert(len(cal_cv.getProjectionMatrix()) > 0)

def test_Rectify():
    # Test access to left and right calibration data from StereoCameraCalibration
    script_path = os.path.dirname(os.path.realpath(__file__))
    test_folder = os.path.join(script_path, "..", "..", ".phase_test")
    left_ros_yaml = os.path.join(test_folder, "left_ros.yaml")
    data_folder = os.path.join(script_path, "..", "..", "data")
    
    # Test loading of image data from file
    left_image_file = os.path.join(data_folder, "left.png")
    left_image = readImage(left_image_file)
    rect_image = np.zeros_like(left_image)
    left_image_empty = np.zeros_like(left_image)

    if not os.path.exists(test_folder):
        os.makedirs(test_folder)

    cal = CameraCalibration(left_ros_yaml)

    cal.rectify(left_image, rect_image)
    assert np.count_nonzero(rect_image) > 0

    cal.rectify(left_image_empty, rect_image)
    assert np.any(rect_image) == 0

def test_calibrationFromIdeal():
    # Test access to left and right calibration data from StereoCameraCalibration
    cal = CameraCalibration.calibrationFromIdeal(2448, 2048, 2, 2, 2, 2)
    assert(cal.isValid())
    
    assert cal.getImageHeight() > 0
