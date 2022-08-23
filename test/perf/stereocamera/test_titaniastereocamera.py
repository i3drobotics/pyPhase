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
from phase.pyphase.stereocamera import CameraDeviceInfo, createStereoCamera
from phase.pyphase.stereocamera import CameraDeviceType, CameraInterfaceType


def test_TitaniaStereoCamera_virtual_perf_data_capture():
    # Test performance of read data of virtual Titania stereo camera
    script_path = os.path.dirname(os.path.realpath(__file__))
    test_folder = os.path.join(
        script_path, "..", ".phase_test", "PylonStereoCamera_data_capture")
    if os.path.exists(test_folder):
        shutil.rmtree(test_folder)
    os.makedirs(test_folder)

    left_image_file = os.path.join(test_folder, "left.png")
    right_image_file = os.path.join(test_folder, "right.png")

    left_image = np.zeros((1024, 1040, 3), dtype=np.uint8)
    right_image = np.zeros((1024, 1040, 3), dtype=np.uint8)
    cv2.imwrite(left_image_file, left_image)
    cv2.imwrite(right_image_file, right_image)

    device_info = CameraDeviceInfo(
        "0815-0000", "0815-0001", "virtualtitania",
        CameraDeviceType.DEVICE_TYPE_TITANIA,
        CameraInterfaceType.INTERFACE_TYPE_VIRTUAL
    )
    cam = createStereoCamera(device_info)
    cam.setTestImagePaths(left_image_file, right_image_file)
    cam.enableDataCapture(True)
    cam.setDataCapturePath(test_folder)
    connected = cam.connect()
    if connected:
        cam.startCapture()
        start = time.time()
        result = cam.read()
        end = time.time()
        duration = end - start
        assert duration < 0.1
        cam.disconnect()