#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_stereosgbm.py
 @brief Unit tests for Stereo Semi-Global Block Matcher class
 @details Unit tests generated using PyTest
"""

import os
import time
from phase.pyphase.types import CameraDeviceType, CameraInterfaceType
from phase.pyphase.types import CameraDeviceInfo, CameraReadResult
from phase.pyphase.stereocamera import createStereoCamera
from phase.pyphase.stereomatcher import StereoSGBM
from phase.pyphase import readImage

def test_StereoSGBM():
    # Test initalisation of StereoSGBM stereo matcher
    matcher = StereoSGBM()
    del matcher

def test_StereoSGBM_params():
    # Test setting StereoBM parameters
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(
        script_path, "..", "data")

    left_image_file = os.path.join(data_folder, "left.png")
    right_image_file = os.path.join(data_folder, "right.png")

    left_image = readImage(left_image_file)
    right_image = readImage(right_image_file)
    
    matcher = StereoSGBM()
    matcher.setWindowSize(11)
    matcher.setMinDisparity(0)
    matcher.setNumDisparities(16*300)

    match_result = matcher.compute(left_image, right_image)

    del matcher

def test_StereoBM_params_read_callback():
    # Test the StereoBM matcher virtual Pylon stereo camera by read callback
    left_serial = "0815-0000"
    right_serial = "0815-0001"
    device_type = CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON  # DEVICE_TYPE_TITANIA / DEVICE_TYPE_PHOBOS
    interface_type = CameraInterfaceType.INTERFACE_TYPE_VIRTUAL  # INTERFACE_TYPE_USB / INTERFACE_TYPE_GIGE

    downsample_factor = 1.0
    display_downsample = 0.25
    frames = 20
    timeout = 30
    waitkey_delay = 1

    device_info = CameraDeviceInfo(
        left_serial, right_serial, "virtual-camera",
        device_type,
        interface_type
    )

    cam = createStereoCamera(device_info)

    def read_callback(read_result: CameraReadResult):
        if read_result.valid:
            matcher = StereoSGBM()
            matcher.setWindowSize(11)
            matcher.setMinDisparity(0)
            matcher.setNumDisparities(16*300)

            match_result = matcher.startComputeThread(read_result.left_image, read_result.right_image)

    cam.setReadThreadCallback(read_callback)

    print("Connecting to camera...")
    ret = cam.connect()
    if (ret):
        cam.startCapture()
        cam.startContinousReadThread()
        max_read_duration = 10
        read_start = time.time()
        capture_count = cam.getCaptureCount()
        while(cam.getCaptureCount() < frames):
            # wait some time
            time.sleep(0.1)
            # check read is not taking too long
            read_end = time.time()
            duration = read_end - read_start
            assert (duration < max_read_duration)
            if (duration > max_read_duration):
                break
            time.sleep(1)
        cam.stopContinousReadThread()
        cam.disconnect()