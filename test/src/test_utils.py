#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_utils.py
 @brief Unit tests for Utility functions
 @details Unit tests generated using PyTest
"""
import os
import numpy as np
import cv2
from phase.pyphase import cvMatIsEqual
from phase.pyphase import processStereo, disparity2depth, depth2xyz, savePLY
from phase.pyphase.calib import StereoCameraCalibration
from phase.pyphase.types import MatrixUInt8, StereoMatcherType
from phase.pyphase.stereomatcher import StereoParams


def test_Utils_checkEqualMat():
    # Create equal matrices
    mat_a = np.ones((3, 3, 1), dtype=np.float32)
    mat_b = np.ones((3, 3, 1), dtype=np.float32)

    # Check equal is equal check is correct
    assert (cvMatIsEqual(mat_a, mat_b))

    # Change one element to make it not equal
    mat_a[0, 0] = 0.0

    # Check is not equal check is correct
    assert (not cvMatIsEqual(mat_a, mat_b))


def test_Utils_savePly():
    script_path = os.path.dirname(os.path.realpath(__file__))
    python_wrapper_proj_path = os.path.join(script_path, "../../")
    phase_proj_path = os.path.join(python_wrapper_proj_path, "../../")
    resource_folder = os.path.join(phase_proj_path, "resources")
    out_folder = os.path.join(python_wrapper_proj_path, "out")
    camera_name = "stereotheatresim"
    cal_type = "ros"
    cam_folder = os.path.join(resource_folder, "test", camera_name)
    left_yaml = os.path.join(cam_folder, cal_type, "left.yaml")
    right_yaml = os.path.join(cam_folder, cal_type, "right.yaml")
    left_image_file = os.path.join(cam_folder, "left.png")
    right_image_file = os.path.join(cam_folder, "right.png")
    out_ply = os.path.join(out_folder, "out.ply")

    if not os.path.exists(out_folder):
        os.makedirs(out_folder)

    np_left_image = cv2.imread(left_image_file, cv2.IMREAD_UNCHANGED)
    np_right_image = cv2.imread(right_image_file, cv2.IMREAD_UNCHANGED)

    calibration = StereoCameraCalibration.calibrationFromYAML(
        left_yaml, right_yaml)

    rect_image_pair = calibration.rectify(np_left_image, np_right_image)

    ph_left_image = MatrixUInt8(rect_image_pair.left)
    ph_right_image = MatrixUInt8(rect_image_pair.right)

    stereo_params = StereoParams(
        StereoMatcherType.STEREO_MATCHER_BM,
        11, 0, 25, False
    )
    ph_disparity = processStereo(
        stereo_params, ph_left_image, ph_right_image, calibration, False
    )

    assert ph_disparity.isEmpty() is False

    np_disparity = np.array(ph_disparity)

    np_depth = disparity2depth(np_disparity, calibration.getQ())

    assert np_depth.size != 0

    xyz = depth2xyz(np_depth, calibration.getHFOV())

    save_success = savePLY(out_ply, xyz, rect_image_pair.left)
    assert (save_success)
