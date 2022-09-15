#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_titaniastereocamera.py
 @brief Performance tests for Titania Stereo Camera class
 @details Performance tests generated using PyTest
"""
import time
import os
import shutil
import numpy as np
import cv2
import phase.pyphase as phase


def test_TitaniaStereoCamera_virtual_perf_data_capture():
    # Test reading of frame from virtual camera
    # using ‘read’ function is completed in less than 0.1s
    timeout = 0.1 #second
    device_info = phase.stereocamera.CameraDeviceInfo(
        "0815-0000", "0815-0001", "virtualtitania",
        phase.stereocamera.CameraDeviceType.DEVICE_TYPE_TITANIA,
        phase.stereocamera.CameraInterfaceType.INTERFACE_TYPE_VIRTUAL
    )

    cam = phase.stereocamera.createStereoCamera(device_info)
    connected = cam.connect()
    if connected:
        cam.startCapture()
        start = time.time()
        result = cam.read()
        end = time.time()
        duration = end - start
        assert duration < timeout
        cam.disconnect()