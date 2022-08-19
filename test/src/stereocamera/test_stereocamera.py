#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_stereocamera.py
 @brief Unit tests for Stereo Camera class
 @details Unit tests generated using PyTest
"""

from phase.pyphase.stereocamera import createStereoCamera
from phase.pyphase.stereocamera import CameraDeviceInfo
from phase.pyphase.stereocamera import CameraDeviceType, CameraInterfaceType


def test_StereoCamera():
    # Test initalisation of stereo camera using CameraDeviceInfo
    device_info = CameraDeviceInfo(
        "abc123left", "abc123right", "abc123unique",
        CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        CameraInterfaceType.INTERFACE_TYPE_USB
    )
    createStereoCamera(device_info)


def test_StereoCamera_isConnected_onInit():
    # Test if stereo camera is connected
    device_info = CameraDeviceInfo(
        "abc123left", "abc123right", "abc123unique",
        CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        CameraInterfaceType.INTERFACE_TYPE_USB
    )
    cam = createStereoCamera(device_info)
    assert cam.isConnected() is False


def test_StereoCamera_connect_onInit():
    # Test to connect stereo camera
    device_info = CameraDeviceInfo(
        "abc123left", "abc123right", "abc123unique",
        CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        CameraInterfaceType.INTERFACE_TYPE_USB
    )
    cam = createStereoCamera(device_info)
    assert cam.connect() is False
