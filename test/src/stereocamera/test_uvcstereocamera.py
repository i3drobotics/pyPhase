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
import cv2
import numpy as np
from phase.pyphase.stereocamera import UVCStereoCamera
from phase.pyphase.types import CameraDeviceInfo
from phase.pyphase.types import CameraDeviceType, CameraInterfaceType


def test_UVCStereoCamera():
    #TODOC Description of the test
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
    #TODOC Description of the test
    script_path = os.path.dirname(os.path.realpath(__file__))
    test_folder = os.path.join(script_path, "..", "..", ".phase_test")
    left_image_file = os.path.join(test_folder, "left.png")
    right_image_file = os.path.join(test_folder, "right.png")

    if not os.path.exists(test_folder):
        os.makedirs(test_folder)

    np_left_image = np.zeros((2048, 2448), dtype=np.uint8)
    np_right_image = np.zeros((2048, 2448), dtype=np.uint8)
    cv2.imwrite(left_image_file, np_left_image)
    cv2.imwrite(right_image_file, np_right_image)

    device_info = CameraDeviceInfo(
        "0", "0", "virtualuvc",
        CameraDeviceType.DEVICE_TYPE_GENERIC_UVC,
        CameraInterfaceType.INTERFACE_TYPE_VIRTUAL
    )
    cam = UVCStereoCamera(device_info)
    cam.setTestImagePaths(left_image_file, right_image_file)
    connected = cam.connect()
    if connected:
        cam.disconnect()
    assert connected is True
