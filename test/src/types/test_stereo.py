#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-06-28
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_common.py
 @brief Unit tests for common types
 @details Unit tests generated using PyTest
"""
import numpy as np
from phase.pyphase.types import StereoImagePair
from phase.pyphase.stereocamera import CameraReadResult
from phase.pyphase.stereomatcher import StereoMatcherComputeResult

def test_StereoImagePair_init():
    # Test initalisation of StereoImagePair
    left = np.zeros((10, 10, 3), dtype=np.uint8)
    right = np.zeros((10, 10, 3), dtype=np.uint8)
    pair = StereoImagePair(left, right)
    assert(pair.left.shape == left.shape)
    assert(pair.right.shape == right.shape)


def test_CameraReadResult_init():
    # Test initalisation of CameraReadResult
    left = np.zeros((10, 10, 3), dtype=np.uint8)
    right = np.zeros((10, 10, 3), dtype=np.uint8)
    valid = True
    result = CameraReadResult(valid, left, right)
    assert(result.left.shape == left.shape)
    assert(result.right.shape == right.shape)
    assert(result.valid == valid)


def test_StereoMatcherComputeResult_init():
    # Test initalisation of StereoMatcherComputeResult
    disparity = np.zeros((10, 10, 1), dtype=np.float32)
    valid = True
    result = StereoMatcherComputeResult(valid, disparity)
    assert(result.disparity.shape == disparity.shape)
    assert(result.valid == valid)
