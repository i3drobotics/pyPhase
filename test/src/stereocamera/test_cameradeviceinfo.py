#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-06-28
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_cameradeviceinfo.py
 @brief Unit tests for Camera Device Info class
 @details Unit tests generated using PyTest
"""

from phase.pyphase.stereocamera import CameraDeviceInfo
from phase.pyphase.stereocamera import CameraDeviceType, CameraInterfaceType

def test_CameraDeviceInfo():
    # Test initalisation of camera device info
    CameraDeviceInfo(
        "abc123left", "abc123right", "abc123unique",
        CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        CameraInterfaceType.INTERFACE_TYPE_USB
    )
