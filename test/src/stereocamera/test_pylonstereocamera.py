#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_pylonstereocamera.py
 @brief Unit tests for Pylon Stereo Camera class
 @details Unit tests generated using PyTest
"""
import os
import time
from glob import glob
import numpy as np
import cv2

from phase.pyphase.stereocamera import PylonStereoCamera
from phase.pyphase.types import CameraDeviceInfo
from phase.pyphase.types import CameraDeviceType, CameraInterfaceType
from phase.pyphase.types import CameraReadResult


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


def test_PylonStereoCamera_virtual_data_capture():
    script_path = os.path.dirname(os.path.realpath(__file__))
    test_folder = os.path.join(
        script_path, "..", ".phase_test", "PylonStereoCamera_data_capture")
    if not os.path.exists(test_folder):
        os.makedirs(test_folder)

    device_info = CameraDeviceInfo(
        "0815-0000", "0815-0001", "virtualpylon",
        CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        CameraInterfaceType.INTERFACE_TYPE_VIRTUAL
    )
    cam = PylonStereoCamera(device_info)
    cam.enableDataCapture(True)
    cam.setDataCapturePath(test_folder)
    connected = cam.connect()
    if connected:
        cam.startCapture()
        cam.read()
        cam.disconnect()
    assert connected is True
    left_glob_files = glob(os.path.join(test_folder, "*_l.png"))
    right_glob_files = glob(os.path.join(test_folder, "*_r.png"))
    assert len(left_glob_files) == 1
    assert len(right_glob_files) == 1


def test_PylonStereoCamera_virtual_capture_count():
    device_info = CameraDeviceInfo(
        "0815-0000", "0815-0001", "virtualpylon",
        CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        CameraInterfaceType.INTERFACE_TYPE_VIRTUAL
    )
    cam = PylonStereoCamera(device_info)
    frames = 10
    connected = cam.connect()
    if connected:
        cam.startCapture()
        print("Capturing frames...")
        for _ in range(frames):
            cam.read()
        assert cam.getCaptureCount() == frames
        print("Frame capture complete.")
        cam.resetCaptureCount()
        assert cam.getCaptureCount() == 0
        cam.disconnect()
    assert connected is True


def test_PylonStereoCamera_virtual_continous_read():
    script_path = os.path.dirname(os.path.realpath(__file__))
    test_folder = os.path.join(
        script_path, "..", ".phase_test", "PylonStereoCamera_continous_read")

    if not os.path.exists(test_folder):
        os.makedirs(test_folder)

    left_image_file = os.path.join(test_folder, "left.png")
    right_image_file = os.path.join(test_folder, "right.png")

    left_image = np.zeros((100, 100, 3), dtype=np.uint8)
    right_image = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite(left_image_file, left_image)
    cv2.imwrite(right_image_file, right_image)

    device_info = CameraDeviceInfo(
        "0815-0000", "0815-0001", "virtualpylon",
        CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        CameraInterfaceType.INTERFACE_TYPE_VIRTUAL
    )
    frames = 10
    cam = PylonStereoCamera(device_info)
    cam.setTestImagePaths(left_image_file, right_image_file)
    cam.enableDataCapture(True)
    cam.setDataCapturePath(test_folder)
    connected = cam.connect()
    assert connected is True
    if connected:
        print("Capturing continous frames...")
        cam.startCapture()
        cam.startContinousReadThread()
        previous_count = cam.getCaptureCount()
        while(cam.getCaptureCount() < frames):
            count = cam.getCaptureCount()
            if (count > previous_count):
                result = cam.getReadThreadResult()
                assert (np.any(result.left) == False)
            # wait some time
            time.sleep(0.1)
        print("Frame capture complete.")
        cam.stopContinousReadThread()
        assert(cam.getCaptureCount() == frames)
        cam.resetCaptureCount()
        assert(cam.getCaptureCount() == 0)
        cam.disconnect()
    left_glob_files = glob(os.path.join(test_folder, "*_l.png"))
    right_glob_files = glob(os.path.join(test_folder, "*_r.png"))
    assert len(left_glob_files) == frames
    assert len(right_glob_files) == frames
