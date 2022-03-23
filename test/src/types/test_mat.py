#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-06-28
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_mat.py
 @brief Unit tests for Mat class
 @details Unit tests generated using PyTest
"""
import cv2
import numpy as np
from phase.pyphase.types import MatrixUInt8, MatrixFloat


def test_Mat():
    # generate numpy matrices
    np_float = np.zeros((10, 10, 3), dtype=np.float32)
    np_uint8 = np.zeros((10, 10, 3), dtype=np.uint8)

    # convert to phase matrix types
    ph_float = MatrixFloat(np_float)
    ph_uint8 = MatrixUInt8(np_uint8)

    # convert back to np
    np_float_out = np.array(ph_float)
    np_uint8_out = np.array(ph_uint8)

    # assert equal after conversion
    assert np.array_equal(np_float, np_float_out)
    assert np.array_equal(np_uint8, np_uint8_out)
