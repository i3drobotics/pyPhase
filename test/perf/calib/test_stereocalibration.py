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
import phase.pyphase as phase


def test_perf_Calibration_from_images():
    # Test performance of calibrate stereo camera from 13 image pairs
    # calibrate completed in less than 5s
    timeout = 5 #second

    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(
        script_path, "..", "..", "data", "checker_sample")

    left_cal_folder = data_folder
    right_cal_folder = data_folder

    left_img_wildcard = "*_l.png"
    right_img_wildcard = "*_r.png"
    image_type = phase.calib.CalibrationBoardType.CHECKERBOARD

    start = time.time()
    # Load calibration from images
    cal = phase.calib.StereoCameraCalibration.calibrationFromImages(
        left_cal_folder, right_cal_folder,
        left_img_wildcard, right_img_wildcard,
        image_type, 10, 6, 0.039)
    end = time.time()
    duration = end - start

    assert cal.isValid()
    assert duration < timeout

def test_perf_Rectify():
    # Test rectification of image of size 2448x2048
    # using ‘rectify’ function is completed in less than 0.3s 

    timeout = 0.3 #second
    left_img = np.ones((2048, 2448, 3), dtype=np.uint8)
    right_img = np.ones((2048, 2448, 3), dtype=np.uint8)

    cal = phase.calib.StereoCameraCalibration.calibrationFromIdeal(
        2448, 2048, 0.00000345, 0.012, 0.1)
    if cal.isValid():

        start = time.time()
        rect = cal.rectify(left_img, right_img)
        end = time.time()
        duration = end - start

        assert duration < timeout