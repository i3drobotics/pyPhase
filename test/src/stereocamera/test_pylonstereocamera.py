#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_pylonstereocamera.py
 @brief Unit tests for Pylon Stereo Camera class
 @details Unit tests generated using PyTest
"""

from phase.pyphase.stereocamera import PylonStereoCamera
from phase.pyphase.types import CameraDeviceInfo
from phase.pyphase.types import CameraDeviceType, CameraInterfaceType


def test_PylonStereoCamera():
    device_info = CameraDeviceInfo(
        "abc123left", "abc123right", "abc123unique",
        CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        CameraInterfaceType.INTERFACE_TYPE_USB
    )
    PylonStereoCamera(device_info)


def test_PylonStereoCamera_isConnected_onInit():
    device_info = CameraDeviceInfo(
        "abc123left", "abc123right", "abc123unique",
        CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        CameraInterfaceType.INTERFACE_TYPE_USB
    )
    cam = PylonStereoCamera(device_info)
    assert cam.isConnected() is False


def test_PylonStereoCamera_connect_onInit():
    device_info = CameraDeviceInfo(
        "abc123left", "abc123right", "abc123unique",
        CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        CameraInterfaceType.INTERFACE_TYPE_USB
    )
    cam = PylonStereoCamera(device_info)
    assert cam.connect() is False


def test_PylonStereoCamera_connect_virtual_onInit():
    device_info = CameraDeviceInfo(
        "0815-0000", "0815-0001", "virtualpylon",
        CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        CameraInterfaceType.INTERFACE_TYPE_VIRTUAL
    )
    cam = PylonStereoCamera(device_info)
    connected = cam.connect()
    if connected:
        cam.disconnect()
    assert connected is True
