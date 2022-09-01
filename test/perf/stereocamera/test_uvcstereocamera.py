#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_uvcstereocamera.py
 @brief Performance tests for UVC Stereo Camera class
 @details Performance tests generated using PyTest
"""
import time
import os
import shutil
import numpy as np
import cv2
from phase.pyphase.stereocamera import CameraDeviceInfo, createStereoCamera
from phase.pyphase.stereocamera import CameraDeviceType, CameraInterfaceType


def test_UVCStereoCamera_virtual_perf_data_capture():
    # Test reading of frame from virtual camera
    # using ‘read’ function is completed in less than 0.1s
    timeout = 0.1 #second
    device_info = CameraDeviceInfo(
        "0", "0", "virtualuvc",
        CameraDeviceType.DEVICE_TYPE_GENERIC_UVC,
        CameraInterfaceType.INTERFACE_TYPE_VIRTUAL
    )

    cam = createStereoCamera(device_info)

    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(
        script_path, "..", "..", "data")

    left_image_file = os.path.join(data_folder, "left.png")
    right_image_file = os.path.join(data_folder, "right.png")

    cam.setTestImagePaths(left_image_file, right_image_file)
    connected = cam.connect()
    if connected:
        cam.startCapture()
        start = time.time()
        result = cam.read()
        end = time.time()
        duration = end - start
        assert duration < timeout
        cam.disconnect()
