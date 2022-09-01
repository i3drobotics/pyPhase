#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-06-28
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_cameracalibration.py
 @brief Performance tests for CameraCalibration class
 @details Performance tests generated using PyTest
"""
import time
import os
import numpy as np
from phase.pyphase import readImage
from phase.pyphase.calib import CameraCalibration


def test_perf_Rectify():
    # Test performance of rectify 
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

    start = time.time()
    cal.rectify(left_image, rect_image)
    end = time.time()
    duration = end - start

    assert duration < 0.2