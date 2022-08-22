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
import cv2
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
        assert match_result.disparity[0,0] == -16
        assert match_result.disparity[20,20] == -16
        assert match_result.disparity[222,222] == -16
    else:
        # TODO add disparity element checks for valid license compute
        pass

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
    start = time.time()
    match_result = matcher.compute(left_image, right_image)
    end = time.time()
    assert end-start < 0.5

    del matcher


def test_StereoI3DRSGM_params_read_callback():
    # Test the StereoI3DRSGM matcher virtual Pylon stereo camera by read callback
    script_path = os.path.dirname(os.path.realpath(__file__))
    test_folder = os.path.join(
        script_path, "..", "..", "data")

    left_image_file = os.path.join(test_folder, "left.png")
    right_image_file = os.path.join(test_folder, "right.png")

    left_image = cv2.imread(left_image_file)
    right_image = cv2.imread(right_image_file)

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
    max_read_duration = 2
    
    matcher.startComputeThread(left_image, right_image)
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
        assert matcher.getComputeThreadResult().disparity[0,0] == -16
        assert matcher.getComputeThreadResult().disparity[20,20] == -16
        assert matcher.getComputeThreadResult().disparity[222,222] == -16
    else:
        # TODO add disparity element checks for valid license compute
        pass