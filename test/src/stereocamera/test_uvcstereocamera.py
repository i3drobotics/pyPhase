#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_uvcstereocamera.py
 @brief Unit tests for UVC Stereo Camera class
 @details Unit tests generated using PyTest
"""

import os
from phase.pyphase.stereocamera import UVCStereoCamera
from phase.pyphase.types import CameraDeviceInfo
from phase.pyphase.types import CameraDeviceType, CameraInterfaceType


def test_UVCStereoCamera():
    device_info = CameraDeviceInfo(
        "0", "0", "virtualuvc",
        CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        CameraInterfaceType.INTERFACE_TYPE_USB
    )
    UVCStereoCamera(device_info)


# def test_UVCStereoCamera_connect_onInit():
#     device_info = CameraDeviceInfo(
#         "0", "0", "virtualuvc",
#         CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
#         CameraInterfaceType.INTERFACE_TYPE_USB
#     )
#     cam = UVCStereoCamera(device_info)
#     assert cam.connect() is False


def test_UVCStereoCamera_connect_virtual_onInit():
    device_info = CameraDeviceInfo(
        "0", "0", "virtualuvc",
        CameraDeviceType.DEVICE_TYPE_GENERIC_UVC,
        CameraInterfaceType.INTERFACE_TYPE_VIRTUAL
    )
    cam = UVCStereoCamera(device_info)
    script_path = os.path.dirname(os.path.realpath(__file__))
    python_wrapper_proj_path = os.path.join(script_path, "../../../")
    phase_proj_path = os.path.join(python_wrapper_proj_path, "../../")
    resource_folder = os.path.join(phase_proj_path, "resources")
    left_image_file = os.path.join(
        resource_folder, "test/stereotheatresim/left.png")
    right_image_file = os.path.join(
        resource_folder, "test/stereotheatresim/right.png")
    cam.setTestImagePaths(left_image_file, right_image_file)
    connected = cam.connect()
    if connected:
        cam.disconnect()
    assert connected is True
