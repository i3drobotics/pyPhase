#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_phobosstereocamera.py
 @brief Performance tests for Phobos Stereo Camera class
 @details Performance tests generated using PyTest
"""
import time
import os
import shutil
import numpy as np
import cv2
from phase.pyphase.stereocamera import CameraDeviceInfo, createStereoCamera
from phase.pyphase.stereocamera import CameraDeviceType, CameraInterfaceType


def test_PhobosStereoCamera_virtual_perf_data_capture():
    # Test reading of frame from virtual camera
    # using ‘read’ function is completed in less than 0.1s
    timeout = 0.1
    device_info = CameraDeviceInfo(
        "0815-0000", "0815-0001", "virtualphobos",
        CameraDeviceType.DEVICE_TYPE_PHOBOS,
        CameraInterfaceType.INTERFACE_TYPE_VIRTUAL
    )

    cam = createStereoCamera(device_info)
    connected = cam.connect()
    if connected:
        cam.startCapture()
        start = time.time()
        result = cam.read()
        end = time.time()
        duration = end - start
        assert duration < timeout
        cam.disconnect()