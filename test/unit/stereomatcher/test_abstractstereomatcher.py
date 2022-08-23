#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2022-08-22
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_abstractstereomatcher.py
 @brief Unit tests for AbstractStereoMatcher
 @details Unit tests for use with PyTest
"""
import numpy as np
from phase.pyphase.stereomatcher import StereoMatcherComputeResult


def test_StereoMatcherComputeResult_init():
    # Test initalisation of StereoMatcherComputeResult
    disparity = np.zeros((10, 10, 1), dtype=np.float32)
    valid = True
    result = StereoMatcherComputeResult(valid, disparity)
    assert(result.disparity.shape == disparity.shape)
    assert(result.valid == valid)