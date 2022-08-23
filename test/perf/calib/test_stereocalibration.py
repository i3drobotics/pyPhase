#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-06-28
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_stereocalibration.py
 @brief Performance tests for StereoCameraCalibration class
 @details Performance tests generated using PyTest
"""
import time
import os
import numpy as np
from phase.pyphase import readImage
from phase.pyphase.calib import StereoCameraCalibration


def test_perf_Rectify():
    # Test performance of rectify 
    script_path = os.path.dirname(os.path.realpath(__file__))
    test_folder = os.path.join(script_path, "..", "..", ".phase_test")
    data_folder = os.path.join(script_path, "..", "..", "data")
    left_ros_yaml = os.path.join(test_folder, "left_ros.yaml")
    right_ros_yaml = os.path.join(test_folder, "right_ros.yaml")
    
    # Test loading of image data from file
    left_image_file = os.path.join(data_folder, "left.png")
    left_image = readImage(left_image_file)
    right_image_file = os.path.join(data_folder, "right.png")
    right_image = readImage(right_image_file)
    left_image_empty = np.zeros_like(left_image)
    right_image_empty = np.zeros_like(right_image)

    cal = StereoCameraCalibration.calibrationFromYAML(
    left_ros_yaml, right_ros_yaml)

    start = time.time()
    rect = cal.rectify(left_image, right_image)
    end = time.time()
    duration = end - start
    # TODO investigate why rectification is slow
    assert duration < 0.3