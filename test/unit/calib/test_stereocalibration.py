#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-06-28
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_stereocalibration.py
 @brief Unit tests for StereoCameraCalibration class
 @details Unit tests for use with PyTest
"""
import os
import numpy as np
from phase.pyphase import readImage
from phase.pyphase.calib import StereoCameraCalibration, CalibrationBoardType
from phase.pyphase.calib import CalibrationFileType


def test_Calibration_from_images():
    # Test if calibrate stereo camera from a serie of images is valid
    # load 13 checkerboard image pairs from folder
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(
        script_path, "..", "..", "data", "checker_sample")

    left_cal_folder = data_folder
    right_cal_folder = data_folder

    left_img_wildcard = "*_l.png"
    right_img_wildcard = "*_r.png"
    image_type = CalibrationBoardType.CHECKERBOARD

    # Load calibration from images
    cal = StereoCameraCalibration.calibrationFromImages(
        left_cal_folder, right_cal_folder,
        left_img_wildcard, right_img_wildcard,
        image_type, 10, 6, 0.039)

    assert cal.isValid()


def test_lr_access():
    # Test access to left and right calibration data from StereoCameraCalibration
    script_path = os.path.dirname(os.path.realpath(__file__))
    test_folder = os.path.join(script_path, "..", "..", ".phase_test")
    left_ros_yaml = os.path.join(test_folder, "left_ros.yaml")
    right_ros_yaml = os.path.join(test_folder, "right_ros.yaml")

    if not os.path.exists(test_folder):
        os.makedirs(test_folder)

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
    right_ros_yaml_data = \
        "image_width: 2448\n" \
        "image_height: 2048\n" \
        "camera_name: rightCamera\n" \
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
        "   data: [ 3.4782608695652175e+03, 0., 1224., -3.4782608695652175e+02, 0., 3.4782608695652175e+03, 1024., 0., 0., 0., 1., 0. ]\n"

    with open(left_ros_yaml, 'w') as f:
        f.writelines(left_ros_yaml_data)
    with open(right_ros_yaml, 'w') as f:
        f.writelines(right_ros_yaml_data)

    cal_ros = StereoCameraCalibration.calibrationFromYAML(
        left_ros_yaml, right_ros_yaml)
    assert(cal_ros.isValid())

    # Test lr calibration access
    assert(cal_ros.left_calibration)
    assert(cal_ros.right_calibration)
    assert(len(cal_ros.left_calibration.getCameraMatrix()) > 0)
    assert(len(cal_ros.left_calibration.getDistortionCoefficients()) > 0)
    assert(len(cal_ros.left_calibration.getRectificationMatrix()) > 0)
    assert(len(cal_ros.left_calibration.getProjectionMatrix()) > 0)


def test_LoadCalibration():
    # Test loading calibration from file
    script_path = os.path.dirname(os.path.realpath(__file__))
    test_folder = os.path.join(script_path, "..", "..", ".phase_test")
    left_ros_yaml = os.path.join(test_folder, "left_ros.yaml")
    right_ros_yaml = os.path.join(test_folder, "right_ros.yaml")
    left_cv_yaml = os.path.join(test_folder, "left_cv.yaml")
    right_cv_yaml = os.path.join(test_folder, "right_cv.yaml")

    if not os.path.exists(test_folder):
        os.makedirs(test_folder)

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
    right_ros_yaml_data = \
        "image_width: 2448\n" \
        "image_height: 2048\n" \
        "camera_name: rightCamera\n" \
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
        "   data: [ 3.4782608695652175e+03, 0., 1224., -3.4782608695652175e+02, 0., 3.4782608695652175e+03, 1024., 0., 0., 0., 1., 0. ]\n"
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
    right_cv_yaml_data = \
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
        "   data: [ 3.4782608695652175e+03, 0., 1224., -3.4782608695652175e+02, 0., 3.4782608695652175e+03, 1024., 0., 0., 0., 1., 0. ]\n" \
        "rms_error: ""\n"

    with open(left_ros_yaml, 'w') as f:
        f.writelines(left_ros_yaml_data)
    with open(right_ros_yaml, 'w') as f:
        f.writelines(right_ros_yaml_data)
    with open(left_cv_yaml, "w+") as f:
        f.writelines(left_cv_yaml_data)
    with open(right_cv_yaml, "w+") as f:
        f.writelines(right_cv_yaml_data)

    cal_ros = StereoCameraCalibration.calibrationFromYAML(
        left_ros_yaml, right_ros_yaml)
    assert(cal_ros.isValid())

    cal_cv = StereoCameraCalibration.calibrationFromYAML(
        left_cv_yaml, right_cv_yaml)
    assert(cal_cv.isValid())


def test_SaveCalibration():
    # Test saving calibration files
    script_path = os.path.dirname(os.path.realpath(__file__))
    test_folder = os.path.join(script_path, "..", "..", ".phase_test")
    left_yaml = os.path.join(test_folder, "left.yaml")
    right_yaml = os.path.join(test_folder, "right.yaml")

    print("Generating test data...")
    # Create calibration files
    left_yaml_data = \
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
    right_yaml_data = \
        "image_width: 2448\n" \
        "image_height: 2048\n" \
        "camera_name: rightCamera\n" \
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
        "   data: [ 3.4782608695652175e+03, 0., 1224., -3.4782608695652175e+02, 0., 3.4782608695652175e+03, 1024., 0., 0., 0., 1., 0. ]\n"

    with open(left_yaml, "w+") as f:
        f.writelines(left_yaml_data)
    with open(right_yaml, "w+") as f:
        f.writelines(right_yaml_data)

    cal = StereoCameraCalibration.calibrationFromYAML(left_yaml, right_yaml)
    assert(cal.isValid())

    assert cal.saveToYAML(
        os.path.join(test_folder, "left_ros.yaml"),
        os.path.join(test_folder, "right_ros.yaml"),
        CalibrationFileType.ROS_YAML) == 1
    assert cal.saveToYAML(
        os.path.join(test_folder, "left_cv.yaml"),
        os.path.join(test_folder, "right_cv.yaml"),
        CalibrationFileType.OPENCV_YAML) == 1


def test_calibrationFromIdeal():
    # Test access to left and right calibration data from StereoCameraCalibration
    cal = StereoCameraCalibration.calibrationFromIdeal(2448, 2048, 0.00000345, 0.012, 0.1)
    assert(cal.isValid())

    assert cal.getBaseline() > 0
    

def test_Rectify():
    # Test access to left and right calibration data from StereoCameraCalibration
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(script_path, "..", "..", "data")
    left_ros_yaml = os.path.join(data_folder, "left.yaml")
    right_ros_yaml = os.path.join(data_folder, "right.yaml")
    
    # Test loading of image data from file
    left_image_file = os.path.join(data_folder, "left.png")
    left_image = readImage(left_image_file)
    right_image_file = os.path.join(data_folder, "right.png")
    right_image = readImage(right_image_file)
    left_image_empty = np.zeros_like(left_image)
    right_image_empty = np.zeros_like(right_image)

    cal = StereoCameraCalibration.calibrationFromYAML(
    left_ros_yaml, right_ros_yaml)

    rect = cal.rectify(left_image, right_image)
    assert np.count_nonzero(rect.left) > 0

    rect_empty = cal.rectify(left_image_empty, right_image_empty)
    assert np.any(rect_empty.left) == 0
