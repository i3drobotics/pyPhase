#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-06-28
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_cameracalibration.py
 @brief Performance tests for CameraCalibration class
 @details Performance tests generated using PyTest
"""
from pickletools import uint8
import time
import os
import numpy as np
from phase.pyphase import readImage
from phase.pyphase.calib import CameraCalibration


def test_perf_Rectify():
    # Test rectification of image of size 2448x2048
    # using ‘rectify’ function is completed in less than 0.2s
    timeout = 0.3 # second
    img = np.ones((2048, 2448, 3), dtype=np.uint8)

    cal = CameraCalibration.calibrationFromIdeal(2448, 2048, 0.00000345, 0.012, 0.1, 0.0)
    if cal.isValid():
        rect_image = np.zeros((2048, 2448, 3), dtype=np.uint8)

        start = time.time()
        cal.rectify(img, rect_image)
        end = time.time()
        duration = end - start
        assert duration < timeout