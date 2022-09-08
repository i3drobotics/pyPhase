#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_pylonstereocamera.py
 @brief Unit tests for Pylon Stereo Camera class
 @details Unit tests for use with PyTest
"""
import os
import time
import shutil
from glob import glob
import numpy as np
import cv2
import phase.pyphase as phase


def test_PylonStereoCamera_setparams():
    # Test to set Pylon virtual stereo camera flip frame
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(script_path, "..", "..", "data")
    left_image_file = os.path.join(data_folder, "left.png")
    right_image_file = os.path.join(data_folder, "right.png")

    left_image = phase.readImage(left_image_file)
    right_image = phase.readImage(right_image_file)

    device_info = phase.stereocamera.CameraDeviceInfo(
        "abc123left", "abc123right", "abc123unique",
        phase.stereocamera.CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        phase.stereocamera.CameraInterfaceType.INTERFACE_TYPE_USB
    )

    cam = phase.stereocamera.createStereoCamera(device_info)
    cam.setTestImagePaths(left_image_file, right_image_file)

    frame_rate = 5
    exposure = 500
    hardware_trigger = False
    x_min = 10
    x_max = 100
    y_min = 10
    y_max = 100

    connected = cam.connect()
    if connected:
        cam.startCapture()
        cam.setExposure(exposure)
        cam.enableHardwareTrigger(hardware_trigger)
        cam.setFrameRate(frame_rate)
        cam.setLeftAOI(x_min, x_max, y_min, y_max)
        cam.setRightAOI(x_min, x_max, y_min, y_max)
        
        read_result = cam.read()
        # TODO fix setting frame rate for Pylon Cameras
        # assert cam.getFrameRate() == frame_rate

        # Test to check the AOI size
        assert read_result.left.shape[0] == x_max - x_min
        assert read_result.left.shape[1] == y_max - y_min
        assert read_result.right.shape[0] == x_max - x_min
        assert read_result.right.shape[1] == y_max - y_min

        # Test to check the flip functions
        cam.setLeftFlipX(True)
        read_result = cam.read()
        read_result_left = read_result.left
        assert left_image[0,0,0] != read_result_left[0,0,0]
        assert left_image[0,0,0] == read_result_left[2047,0,0]

        cam.setRightFlipX(True)
        read_result = cam.read()
        read_result_right = read_result.right
        assert right_image[0,0,0] != read_result_right[0,0,0]
        assert right_image[0,0,0] == read_result_right[2047,0,0]

        cam.setLeftFlipY(True)
        read_result = cam.read()
        read_result_left = read_result.left
        assert left_image[0,0,0] != read_result_left[0,0,0]
        assert left_image[0,0,0] == read_result_left[2047,2447,0]

        cam.setRightFlipY(True)
        read_result = cam.read()
        read_result_right = read_result.right
        assert right_image[0,0,0] != read_result_right[0,0,0]
        assert right_image[0,0,0] == read_result_right[2047,2447,0]

        cam.disconnect()


def test_PylonStereoCamera():
    # Test initalisation of PylonStereoCamera using CameraDeviceInfo
    device_info = phase.stereocamera.CameraDeviceInfo(
        "abc123left", "abc123right", "abc123unique",
        phase.stereocamera.CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        phase.stereocamera.CameraInterfaceType.INTERFACE_TYPE_USB
    )
    phase.stereocamera.createStereoCamera(device_info)


def test_PylonStereoCamera_isConnected_onInit():
    # Test if Pylon stereo camera is connected
    device_info = phase.stereocamera.CameraDeviceInfo(
        "abc123left", "abc123right", "abc123unique",
        phase.stereocamera.CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        phase.stereocamera.CameraInterfaceType.INTERFACE_TYPE_USB
    )
    cam = phase.stereocamera.createStereoCamera(device_info)
    assert not cam.isConnected()


def test_PylonStereoCamera_connect_onInit():
    # Test to connect Pylon stereo camera
    device_info = phase.stereocamera.CameraDeviceInfo(
        "abc123left", "abc123right", "abc123unique",
        phase.stereocamera.CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        phase.stereocamera.CameraInterfaceType.INTERFACE_TYPE_USB
    )
    cam = phase.stereocamera.createStereoCamera(device_info)
    assert not cam.connect()


def test_PylonStereoCamera_connect_virtual_onInit():
    # Test to connect virtual Pylon stereo camera
    device_info = phase.stereocamera.CameraDeviceInfo(
        "0815-0000", "0815-0001", "virtualpylon",
        phase.stereocamera.CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        phase.stereocamera.CameraInterfaceType.INTERFACE_TYPE_VIRTUAL
    )
    cam = phase.stereocamera.createStereoCamera(device_info)
    connected = cam.connect()
    if connected:
        cam.disconnect()
    assert connected


def test_PylonStereoCamera_connect_virtual_size():
    # Test to get the height and width of virtual Pylon stereo camera
    device_info = phase.stereocamera.CameraDeviceInfo(
        "0815-0000", "0815-0001", "virtualpylon",
        phase.stereocamera.CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        phase.stereocamera.CameraInterfaceType.INTERFACE_TYPE_VIRTUAL
    )
    cam = phase.stereocamera.createStereoCamera(device_info)
    connected = cam.connect()
    if connected:
        # assumes that default virtual camera image size
        # has not been modified before connecting
        assert(cam.getWidth() == 1024)
        assert(cam.getHeight() == 1040)
        cam.disconnect()
    assert connected


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

    device_info = phase.stereocamera.CameraDeviceInfo(
        "0815-0000", "0815-0001", "virtualpylon",
        phase.stereocamera.CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        phase.stereocamera.CameraInterfaceType.INTERFACE_TYPE_VIRTUAL
    )
    cam = phase.stereocamera.createStereoCamera(device_info)
    cam.setTestImagePaths(left_image_file, right_image_file)
    cam.enableDataCapture(True)
    cam.setDataCapturePath(test_folder)
    connected = cam.connect()
    if connected:
        cam.startCapture()
        result = cam.read()
        assert (result.valid)
        cam.disconnect()
    assert connected
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

    device_info = phase.stereocamera.CameraDeviceInfo(
        "0815-0000", "0815-0001", "virtualpylon",
        phase.stereocamera.CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        phase.stereocamera.CameraInterfaceType.INTERFACE_TYPE_VIRTUAL
    )
    cam = phase.stereocamera.createStereoCamera(device_info)
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
    assert connected


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

    device_info = phase.stereocamera.CameraDeviceInfo(
        "0815-0000", "0815-0001", "virtualpylon",
        phase.stereocamera.CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        phase.stereocamera.CameraInterfaceType.INTERFACE_TYPE_VIRTUAL
    )
    frames = 3
    cam = phase.stereocamera.createStereoCamera(device_info)
    cam.setTestImagePaths(left_image_file, right_image_file)
    cam.enableDataCapture(True)
    cam.setDataCapturePath(test_folder)
    connected = cam.connect()
    assert connected
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
        stop_start_time = time.time()
        max_stop_duration = 2
        while(cam.isContinousReadThreadRunning()):
            # wait for continous read thread to stop
            duration = time.time() - stop_start_time
            assert (duration < max_stop_duration)
            if (duration > max_stop_duration):
                break
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

    device_info = phase.stereocamera.CameraDeviceInfo(
        "0815-0000", "0815-0001", "virtualpylon",
        phase.stereocamera.CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON,
        phase.stereocamera.CameraInterfaceType.INTERFACE_TYPE_VIRTUAL
    )
    frames = 3
    cam = phase.stereocamera.createStereoCamera(device_info)
    cam.setTestImagePaths(left_image_file, right_image_file)
    cam.enableDataCapture(True)
    cam.setDataCapturePath(test_folder)

    def read_callback(result):
        assert (result.valid)

    cam.setReadThreadCallback(read_callback)
    connected = cam.connect()
    assert connected
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
        stop_start_time = time.time()
        max_stop_duration = 2
        while(cam.isContinousReadThreadRunning()):
            # wait for continous read thread to stop
            duration = time.time() - stop_start_time
            assert (duration < max_stop_duration)
            if (duration > max_stop_duration):
                break
        assert(cam.getCaptureCount() >= frames)
        cam.resetCaptureCount()
        assert(cam.getCaptureCount() == 0)
        cam.disconnect()
    left_glob_files = glob(os.path.join(test_folder, "*_l.png"))
    right_glob_files = glob(os.path.join(test_folder, "*_r.png"))
    assert len(left_glob_files) >= frames
    assert len(right_glob_files) >= frames
