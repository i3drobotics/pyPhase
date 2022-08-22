#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_stereoi3drsgm.py
 @brief Unit tests for I3DR's Semi-Global Stereo Matcher class
 @details Unit tests generated using PyTest
"""

import os
import time
from phase.pyphase.types import CameraDeviceType, CameraInterfaceType
from phase.pyphase.types import CameraDeviceInfo, CameraReadResult
from phase.pyphase.types import StereoMatcherType
from phase.pyphase.stereomatcher import StereoParams, createStereoMatcher
from phase.pyphase.stereocamera import createStereoCamera
from phase.pyphase.stereomatcher import StereoI3DRSGM
from phase.pyphase import readImage


def test_StereoI3DRSGM():
    # Test initalisation of StereoI3DRSGM
    matcher = StereoI3DRSGM()
    del matcher


def test_StereoI3DRSGM_params():
    # Test setting StereoBM parameters
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(
        script_path, "..", "..", "data")

    left_image_file = os.path.join(data_folder, "left.png")
    right_image_file = os.path.join(data_folder, "right.png")

    left_image = readImage(left_image_file)
    right_image = readImage(right_image_file)

    license_valid = StereoI3DRSGM().isLicenseValid()
    # Check for I3DRSGM license
    if license_valid:
        stereo_params = StereoParams(
            StereoMatcherType.STEREO_MATCHER_I3DRSGM,
            9, 0, 49, False
    )
    else:
        stereo_params = StereoParams(
            StereoMatcherType.STEREO_MATCHER_BM,
            11, 0, 25, False
    )
    matcher = createStereoMatcher(stereo_params)

    match_result = matcher.compute(left_image, right_image)

    if not license_valid:
        assert match_result.disparity[0,0] == 0
        assert match_result.disparity[20,20] == 0
        assert match_result.disparity[222,222] > 0
    else:
        # TODO add disparity element checks for valid license compute
        pass

    del matcher


def test_StereoI3DRSGM_params_read_callback():
    # Test the StereoBM matcher virtual Pylon stereo camera by read callback
    left_serial = "0815-0000"
    right_serial = "0815-0001"
    device_type = CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON  # DEVICE_TYPE_TITANIA / DEVICE_TYPE_PHOBOS
    interface_type = CameraInterfaceType.INTERFACE_TYPE_VIRTUAL  # INTERFACE_TYPE_USB / INTERFACE_TYPE_GIGE

    device_info = CameraDeviceInfo(
        left_serial, right_serial, "virtual-camera",
        device_type,
        interface_type
    )

    cam = createStereoCamera(device_info)

    license_valid = StereoI3DRSGM().isLicenseValid()
    # Check for I3DRSGM license
    if license_valid:
        stereo_params = StereoParams(
            StereoMatcherType.STEREO_MATCHER_I3DRSGM,
            9, 0, 49, False
    )
    else:
        stereo_params = StereoParams(
            StereoMatcherType.STEREO_MATCHER_BM,
            11, 0, 25, False
    )

    matcher = createStereoMatcher(stereo_params)

    frames = 3
    connected = cam.connect()
    max_read_duration = 1
    assert connected is True
    if connected:
        print("Capturing continous frames...")
        cam.startCapture()
        while(cam.getCaptureCount() < frames):
            result = cam.read()
            matcher.startComputeThread(result.left, result.right)
            read_start = time.time()
            while matcher.isComputeThreadRunning():
                # To make sure function run something
                #print("Thread is computing")
                # check read is not taking too long
                read_end = time.time()
                duration = read_end - read_start
                assert (duration < max_read_duration)
                if (duration > max_read_duration):
                    break
            assert matcher.getComputeThreadResult().valid
            if not license_valid:
                assert matcher.getComputeThreadResult().disparity[0,0] == 0
                assert matcher.getComputeThreadResult().disparity[20,20] == 0
                assert matcher.getComputeThreadResult().disparity[222,222] == 0
            else:
                # TODO add disparity element checks for valid license compute
                pass