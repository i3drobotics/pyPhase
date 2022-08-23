#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2022-08-22
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_abstractstereocamera.py
 @brief Unit tests for AbstractStereoCamera
 @details Unit tests for use with PyTest
"""
import numpy as np
from phase.pyphase.stereocamera import CameraReadResult

def test_CameraReadResult_init():
    # Test initalisation of CameraReadResult
    left = np.zeros((10, 10, 3), dtype=np.uint8)
    right = np.zeros((10, 10, 3), dtype=np.uint8)
    valid = True
    result = CameraReadResult(valid, left, right)
    assert(result.left.shape == left.shape)
    assert(result.right.shape == right.shape)
    assert(result.valid == valid)
