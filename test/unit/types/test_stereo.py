#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2022-08-22
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_stereo.py
 @brief Unit tests for stereo types
 @details Unit tests for use with PyTest
"""
import numpy as np
from phase.pyphase.types import StereoImagePair

def test_StereoImagePair_init():
    # Test initalisation of StereoImagePair
    left = np.zeros((10, 10, 3), dtype=np.uint8)
    right = np.zeros((10, 10, 3), dtype=np.uint8)
    pair = StereoImagePair(left, right)
    assert(pair.left.shape == left.shape)
    assert(pair.right.shape == right.shape)

