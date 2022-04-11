#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-06-28
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_rgbdvideowriter.py
 @brief Unit tests for RGBD Video Writer class
 @details Unit tests generated using PyTest
"""
import os
import time
import numpy as np
from phase.pyphase.types import MatrixUInt8, StereoMatcherType
from phase.pyphase.calib import StereoCameraCalibration
from phase.pyphase import processStereo, disparity2depth
from phase.pyphase import RGBDVideoWriter
from phase.pyphase.stereomatcher import StereoParams


def test_RGBDVideoWriter():
    script_path = os.path.dirname(os.path.realpath(__file__))
    test_folder = os.path.join(script_path, "..", ".phase_test")
    left_yaml = os.path.join(test_folder, "left.yaml")
    right_yaml = os.path.join(test_folder, "right.yaml")
    out_rgb_video = os.path.join(test_folder, "rgb.mp4")
    out_depth_video = os.path.join(test_folder, "depth.avi")

    if not os.path.exists(test_folder):
        os.makedirs(test_folder)

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

    # Create stereo image pair
    np_left_image = np.zeros((2048, 2448, 3), dtype=np.uint8)
    np_right_image = np.zeros((2048, 2448, 3), dtype=np.uint8)

    num_of_frames = 1

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

    rgbdVideoWriter = RGBDVideoWriter(
        out_rgb_video, out_depth_video,
        ph_left_image.getColumns(), ph_left_image.getRows()
    )

    assert rgbdVideoWriter.isOpened()

    for i in range(0, num_of_frames):
        rgbdVideoWriter.add(rect_image_pair.left, np_depth)

    rgbdVideoWriter.saveThreaded()
    max_save_duration = 10
    save_start = time.time()
    while(rgbdVideoWriter.isSaveThreadRunning()):
        # wait some time
        time.sleep(0.1)
        # check read is not taking too long
        save_end = time.time()
        duration = save_end - save_start
        assert (duration < max_save_duration)
        if (duration > max_save_duration):
            break

    assert rgbdVideoWriter.getSaveThreadResult()
