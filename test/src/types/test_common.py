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
from phase.pyphase.types import Point2d, Point2f, Point2i
from phase.pyphase.types import StereoImagePair, CameraReadResult
from phase.pyphase.types import StereoMatcherComputeResult


def test_Point2d_init():
    # Test initalisation of point2 in double type
    point = Point2d(1.0, 2.0)
    assert(point.x == 1.0)
    assert(point.y == 2.0)


def test_Point2f_init():
    # Test initalisation of point2 in float type
    point = Point2f(1.0, 2.0)
    assert(point.x == 1.0)
    assert(point.y == 2.0)


def test_Point2i_init():
    # Test initalisation of point2 in int type
    point = Point2i(1, 2)
    assert(point.x == 1)
    assert(point.y == 2)


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
