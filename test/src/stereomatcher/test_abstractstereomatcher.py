#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_abstractstereomatcher.py
 @brief Unit tests for Abstract Stereo Matcher class
 @details Unit tests generated using PyTest
"""
from phase.pyphase.stereomatcher import StereoMatcherComputeResult
import numpy as np

def test_AbstractStereoMatcher():
    # TODO add tests for AbstractStereoMatcher
    pass

def test_StereoMatcherComputeResult_init():
    # Test initalisation of StereoMatcherComputeResult
    disparity = np.zeros((10, 10, 1), dtype=np.float32)
    valid = True
    result = StereoMatcherComputeResult(valid, disparity)
    assert(result.disparity.shape == disparity.shape)
    assert(result.valid == valid)