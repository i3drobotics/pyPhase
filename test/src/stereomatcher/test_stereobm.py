#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_stereobm.py
 @brief Unit tests for Stereo Block Matcher class
 @details Unit tests generated using PyTest
"""

import os
import time
import cv2
from phase.pyphase.types import StereoMatcherType
from phase.pyphase.types import CameraDeviceInfo
from phase.pyphase.types import CameraDeviceType, CameraInterfaceType
from phase.pyphase.stereocamera import createStereoCamera
from phase.pyphase.stereomatcher import StereoParams, createStereoMatcher
from phase.pyphase.stereomatcher import StereoBM
from phase.pyphase import readImage

def test_StereoBM():
    # Test initalisation of StereoBM
    matcher = StereoBM()
    del matcher

def test_StereoBM_params():
    # Test setting StereoBM parameters
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(
        script_path, "..", "..", "data")

    left_image_file = os.path.join(data_folder, "left.png")
    right_image_file = os.path.join(data_folder, "right.png")

    left_image = readImage(left_image_file)
    right_image = readImage(right_image_file)

    stereo_params = StereoParams(StereoMatcherType.STEREO_MATCHER_BM,
        11, 0, 25, False)

    matcher = createStereoMatcher(stereo_params)

    match_result = matcher.compute(left_image, right_image)
    assert match_result.disparity[0,0] == -16
    assert match_result.disparity[20,20] == -16
    assert match_result.disparity[222,222] == -16

    del matcher

def test_StereoBM_params_read_callback():
    # Test the StereoBM matcher virtual Pylon stereo camera by read callback
    script_path = os.path.dirname(os.path.realpath(__file__))
    test_folder = os.path.join(
        script_path, "..", "..", "data")

    left_image_file = os.path.join(test_folder, "left.png")
    right_image_file = os.path.join(test_folder, "right.png")

    left_image = cv2.imread(left_image_file)
    right_image = cv2.imread(right_image_file)

    stereo_params = StereoParams(StereoMatcherType.STEREO_MATCHER_BM,
        11, 0, 25, False)

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

    assert matcher.getComputeThreadResult().disparity[0,0] == -16
    assert matcher.getComputeThreadResult().disparity[20,20] == -16
    assert matcher.getComputeThreadResult().disparity[222,222] == -16
