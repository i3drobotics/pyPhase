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
import shutil
from glob import glob
import numpy as np
import cv2

from phase.pyphase.stereocamera import PylonStereoCamera
from phase.pyphase.types import CameraDeviceInfo
from phase.pyphase.types import CameraDeviceType, CameraInterfaceType
from phase.pyphase.types import CameraReadResult


def test_PylonStereoCamera():
    # Test initalisation of PylonStereoCamera using CameraDeviceInfo
    device_info = CameraDeviceInfo(
        "abc123left", "abc123right", "abc123unique",
        CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        CameraInterfaceType.INTERFACE_TYPE_USB
    )
    PylonStereoCamera(device_info)


def test_PylonStereoCamera_isConnected_onInit():
    # Test if Pylon stereo camera is connected
    device_info = CameraDeviceInfo(
        "abc123left", "abc123right", "abc123unique",
        CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        CameraInterfaceType.INTERFACE_TYPE_USB
    )
    cam = PylonStereoCamera(device_info)
    assert cam.isConnected() is False


def test_PylonStereoCamera_connect_onInit():
    # Test to connect Pylon stereo camera
    device_info = CameraDeviceInfo(
        "abc123left", "abc123right", "abc123unique",
        CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        CameraInterfaceType.INTERFACE_TYPE_USB
    )
    cam = PylonStereoCamera(device_info)
    assert cam.connect() is False


def test_PylonStereoCamera_connect_virtual_onInit():
    # Test to connect virtual Pylon stereo camera
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


def test_PylonStereoCamera_connect_virtual_size():
    # Test to get the height and width of virtual Pylon stereo camera
    device_info = CameraDeviceInfo(
        "0815-0000", "0815-0001", "virtualpylon",
        CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        CameraInterfaceType.INTERFACE_TYPE_VIRTUAL
    )
    cam = PylonStereoCamera(device_info)
    connected = cam.connect()
    if connected:
        # assumes that default virtual camera image size
        # has not been modified before connecting
        assert(cam.getWidth() == 1024)
        assert(cam.getHeight() == 1040)
        cam.disconnect()
    assert connected is True


def test_PylonStereoCamera_virtual_data_capture():
    # Test to get the data capture of virtual Pylon stereo camera
    script_path = os.path.dirname(os.path.realpath(__file__))
    test_folder = os.path.join(
        script_path, "..", ".phase_test", "PylonStereoCamera_data_capture")
    if os.path.exists(test_folder):
        shutil.rmtree(test_folder)
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
    cam = PylonStereoCamera(device_info)
    cam.setTestImagePaths(left_image_file, right_image_file)
    cam.enableDataCapture(True)
    cam.setDataCapturePath(test_folder)
    connected = cam.connect()
    if connected:
        cam.startCapture()
        result = cam.read()
        assert (result.valid)
        cam.disconnect()
    assert connected is True
    left_glob_files = glob(os.path.join(test_folder, "*_l.png"))
    right_glob_files = glob(os.path.join(test_folder, "*_r.png"))
    assert len(left_glob_files) == 1
    assert len(right_glob_files) == 1


def test_PylonStereoCamera_virtual_capture_count():
    # Test to get the capture count of virtual Pylon stereo camera
    script_path = os.path.dirname(os.path.realpath(__file__))
    test_folder = os.path.join(
        script_path, "..", ".phase_test", "PylonStereoCamera_capture_count")

    if os.path.exists(test_folder):
        shutil.rmtree(test_folder)
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
    cam = PylonStereoCamera(device_info)
    frames = 3
    cam.setTestImagePaths(left_image_file, right_image_file)
    connected = cam.connect()
    if connected:
        cam.startCapture()
        print("Capturing frames...")
        for _ in range(frames):
            result = cam.read()
            assert (result.valid)
        assert cam.getCaptureCount() == frames
        print("Frame capture complete.")
        cam.resetCaptureCount()
        assert cam.getCaptureCount() == 0
        cam.disconnect()
    assert connected is True


def test_PylonStereoCamera_virtual_continous_read():
    # Test to read virtual Pylon stereo camera data continuously
    script_path = os.path.dirname(os.path.realpath(__file__))
    test_folder = os.path.join(
        script_path, "..", ".phase_test", "PylonStereoCamera_continous_read")

    if os.path.exists(test_folder):
        shutil.rmtree(test_folder)
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
    frames = 3
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
        max_read_duration = 10
        read_start = time.time()
        while(cam.getCaptureCount() < frames):
            count = cam.getCaptureCount()
            if (count > previous_count):
                result = cam.getReadThreadResult()
                assert (result.valid)
            # wait some time
            time.sleep(0.1)
            # check read is not taking too long
            read_end = time.time()
            duration = read_end - read_start
            assert (duration < max_read_duration)
            if (duration > max_read_duration):
                break
        print("Frame capture complete.")
        cam.stopContinousReadThread()
        assert(cam.getCaptureCount() >= frames)
        cam.resetCaptureCount()
        assert(cam.getCaptureCount() == 0)
        cam.disconnect()
    left_glob_files = glob(os.path.join(test_folder, "*_l.png"))
    right_glob_files = glob(os.path.join(test_folder, "*_r.png"))
    assert len(left_glob_files) >= frames
    assert len(right_glob_files) >= frames


def test_PylonStereoCamera_virtual_read_callback():
    # Test to get the data of virtual Pylon stereo camera by read callback
    script_path = os.path.dirname(os.path.realpath(__file__))
    test_folder = os.path.join(
        script_path, "..", ".phase_test", "PylonStereoCamera_read_callback")

    if os.path.exists(test_folder):
        shutil.rmtree(test_folder)
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
    frames = 3
    cam = PylonStereoCamera(device_info)
    cam.setTestImagePaths(left_image_file, right_image_file)
    cam.enableDataCapture(True)
    cam.setDataCapturePath(test_folder)

    def read_callback(result):
        assert (result.valid)

    cam.setReadThreadCallback(read_callback)
    connected = cam.connect()
    assert connected is True
    if connected:
        print("Capturing continous frames...")
        cam.startCapture()
        cam.startContinousReadThread()
        max_read_duration = 10
        read_start = time.time()
        while(cam.getCaptureCount() < frames):
            # wait some time
            time.sleep(0.1)
            # check read is not taking too long
            read_end = time.time()
            duration = read_end - read_start
            assert (duration < max_read_duration)
            if (duration > max_read_duration):
                break
        print("Frame capture complete.")
        cam.stopContinousReadThread()
        assert(cam.getCaptureCount() >= frames)
        cam.resetCaptureCount()
        assert(cam.getCaptureCount() == 0)
        cam.disconnect()
    left_glob_files = glob(os.path.join(test_folder, "*_l.png"))
    right_glob_files = glob(os.path.join(test_folder, "*_r.png"))
    assert len(left_glob_files) >= frames
    assert len(right_glob_files) >= frames


def test_PylonStereoCamera_virtual_camera_params():
    # Test to get the data capture of virtual Pylon stereo camera
    script_path = os.path.dirname(os.path.realpath(__file__))
    test_folder = os.path.join(
        script_path, "..", ".phase_test", "PylonStereoCamera_data_capture")
    if os.path.exists(test_folder):
        shutil.rmtree(test_folder)
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
    connected = cam.connect()
    if connected:
        cam.startCapture()
        cam.setExposure(5000)
        cam.setFrameRate(5)
        cam.setLeftAOI(0, 0, 20, 20)
        cam.setRightAOI(0, 0, 20, 20)
        assert cam.isCapturing() == 1
        while(cam.getCaptureCount() < frames):
            result = cam.read()
            assert (result.valid)
            # TODO test failed because cannot set framerate and AOI
            # TODO missing getExposure() function
            #assert cam.getFrameRate() == 5
            #assert (result.left.shape == (20,20,3))
        cam.disconnect()
    assert connected is True
