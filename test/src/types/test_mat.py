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
    # Test of python matrix generation
    # generate numpy matrices
    np_float = np.zeros((10, 10, 2), dtype=np.float32)
    np_uint8 = np.zeros((10, 10, 2), dtype=np.uint8)

    # convert to phase matrix types
    ph_float = MatrixFloat(np_float)
    ph_uint8 = MatrixUInt8(np_uint8)

    # convert back to np
    np_float_out = np.array(ph_float)
    np_uint8_out = np.array(ph_uint8)

    # get column, row and layer info of the matrix
    assert ph_float.getColumns() == 10
    assert ph_float.getRows() == 10
    assert ph_float.getLayers() == 2
    assert ph_uint8.getColumns() == 10
    assert ph_uint8.getRows() == 10
    assert ph_uint8.getLayers() == 2

    # assert equal after conversion
    assert np.array_equal(np_float, np_float_out)
    assert np.array_equal(np_uint8, np_uint8_out)

    # set value to matrix element and check if the value is set
    ph_float.setAt(3,3,1,5)
    assert ph_float.getAt(3,3,1) == 5
    ph_uint8.setAt(5,3,2,7)
    assert ph_uint8.getAt(5,3,2) == 7

    np_empty = np.empty([10, 10, 2], dtype=np.float32)
    #np_empty[:] = 0
    ph_float_empty = MatrixFloat(np_empty)
    #assert ph_float_empty.isEmpty() == 1
