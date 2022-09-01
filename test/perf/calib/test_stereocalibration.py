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
    # Test rectification of image of size 2448x2048
    # using ‘rectify’ function is completed in less than 0.3s 
    timeout = 0.3 #second
    left_img = np.ones((2048, 2448, 3), dtype=np.uint8)
    right_img = np.ones((2048, 2448, 3), dtype=np.uint8)

    cal = StereoCameraCalibration.calibrationFromIdeal(2448, 2048, 0.00000345, 0.012, 0.1)
    if cal.isValid():

        start = time.time()
        rect = cal.rectify(left_img, right_img)
        end = time.time()
        duration = end - start

        assert duration < timeout