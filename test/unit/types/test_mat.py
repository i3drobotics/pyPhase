#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-06-28
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_mat.py
 @brief Unit tests for Mat class
 @details Unit tests for use with PyTest
"""
import numpy as np
import phase.pyphase as phase


def test_MatrixFloat_creation():
    # Test MatrixFloat created with 10 rows, 10 columns, 2 layers
    # has specified number of rows, columns, and layers 
    rows = 10
    cols = 10
    layers = 2
    mat = phase.types.MatrixFloat(rows, cols, layers)
    assert mat.getColumns() == rows
    assert mat.getRows() == cols
    assert mat.getLayers() == layers


def test_MatrixUInt8_creation():
    # Test MatrixUInt8 created with 10 rows, 10 columns, 2 layers
    # has specified number of rows, columns, and layers 
    rows = 10
    cols = 10
    layers = 2
    mat = phase.types.MatrixUInt8(rows, cols, layers)
    assert mat.getColumns() == rows
    assert mat.getRows() == cols
    assert mat.getLayers() == layers


def test_MatrixFloat_set_element():
    # Test MatrixFloat element can be set to specific value
    # and value can be read back and responds with new value 
    mat = phase.types.MatrixFloat(10, 10, 2)
    value = 5
    row = 3
    col = 3
    layer = 1
    mat.setAt(row, col, layer, value)
    assert mat.getAt(row, col, layer) == value


def test_MatrixUInt8_set_element():
    # Test MatrixUInt8 element can be set to specific value
    # and value can be read back and responds with new value 
    mat = phase.types.MatrixUInt8(10, 10, 2)
    value = 5
    row = 3
    col = 3
    layer = 1
    mat.setAt(row, col, layer, value)
    assert mat.getAt(row, col, layer) == value


def test_MatrixFloat_empty():
    # Test a MatrixFloat that is empty reports as empty using ‘isEmpty’ function 
    mat = phase.types.MatrixFloat()
    assert mat.isEmpty()


def test_MatrixUInt8_empty():
    # Test a MatrixUInt8 that is empty reports as empty using ‘isEmpty’ function 
    mat = phase.types.MatrixUInt8()
    assert mat.isEmpty()
