#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_stereovision.py
 @brief Unit tests for Stereo Vision class
 @details Unit tests generated using PyTest
"""

from phase.pyphase import StereoVision
from phase.pyphase.types import CameraDeviceInfo
from phase.pyphase.types import StereoMatcherType
from phase.pyphase.types import CameraDeviceType, CameraInterfaceType


def test_StereoVision():
    # Load in virtual camera to test CameraDeviceInfo
    device_info = CameraDeviceInfo(
        "0815-0000", "0815-0001", "virtualpylon",
        CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        CameraInterfaceType.INTERFACE_TYPE_VIRTUAL
    )
    # TODO generate internal calibration from ideal for tests
    StereoVision(device_info, StereoMatcherType.STEREO_MATCHER_BM, "", "")
