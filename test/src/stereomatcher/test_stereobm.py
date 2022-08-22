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
from phase.pyphase.stereomatcher import StereoMatcherType
from phase.pyphase.stereocamera import CameraDeviceInfo
from phase.pyphase.stereocamera import CameraDeviceType, CameraInterfaceType
from phase.pyphase.stereocamera import createStereoCamera
from phase.pyphase.stereomatcher import StereoParams, createStereoMatcher
from phase.pyphase.stereomatcher import StereoBM
from phase.pyphase import readImage, normaliseDisparity

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

    assert left_image.size > 0
    assert right_image.size > 0

    stereo_params = StereoParams(StereoMatcherType.STEREO_MATCHER_BM,
        11, 0, 25, True)

    matcher = createStereoMatcher(stereo_params)

    match_result = matcher.compute(left_image, right_image)
    assert match_result.valid
    # verify known unmatched point
    assert match_result.disparity[0,0] == -1.0
    valid_disp_threshold = 0.5
    # disparity values should match expected within threshold
    assert match_result.disparity[1024,1224] >= 239.5 - valid_disp_threshold
    assert match_result.disparity[1024,1224] <= 239.5 + valid_disp_threshold
    assert match_result.disparity[1400,2200] >= 224.4375 - valid_disp_threshold
    assert match_result.disparity[1400,2200] <= 224.4375 + valid_disp_threshold

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

    assert left_image.size > 0
    assert right_image.size > 0

    stereo_params = StereoParams(StereoMatcherType.STEREO_MATCHER_BM,
        11, 0, 25, True)

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

    match_result = matcher.getComputeThreadResult()

    assert match_result.valid
    # verify known unmatched point
    assert match_result.disparity[0,0] == -1.0
    valid_disp_threshold = 0.1
    # disparity values should match expected within threshold
    assert match_result.disparity[1024,1224] >= 239.5 - valid_disp_threshold
    assert match_result.disparity[1024,1224] <= 239.5 + valid_disp_threshold
    assert match_result.disparity[1400,2200] >= 224.4375 - valid_disp_threshold
    assert match_result.disparity[1400,2200] <= 224.4375 + valid_disp_threshold
