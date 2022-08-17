#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_abstractstereocamera.py
 @brief Unit tests for Abstract Stereo Camera class
 @details Unit tests generated using PyTest
"""

from phase.pyphase.stereocamera import CameraDeviceInfo
from phase.pyphase.stereocamera import CameraDeviceType, CameraInterfaceType
from phase.pyphase.stereocamera import CameraReadResult
import numpy as np


def test_CameraDeviceInfo():
    # Test initalisation of camera device info
    CameraDeviceInfo(
        "abc123left", "abc123right", "abc123unique",
        CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        CameraInterfaceType.INTERFACE_TYPE_USB
    )

def test_CameraReadResult_init():
    # Test initalisation of CameraReadResult
    left = np.zeros((10, 10, 3), dtype=np.uint8)
    right = np.zeros((10, 10, 3), dtype=np.uint8)
    valid = True
    result = CameraReadResult(valid, left, right)
    assert(result.left.shape == left.shape)
    assert(result.right.shape == right.shape)
    assert(result.valid == valid)