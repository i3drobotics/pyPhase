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
from phase.pyphase.stereomatcher import StereoMatcherType
from phase.pyphase.stereomatcher import StereoParams, createStereoMatcher
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
        script_path, "..", "..", "data")

    left_image_file = os.path.join(data_folder, "left.png")
    right_image_file = os.path.join(data_folder, "right.png")

    left_image = readImage(left_image_file)
    right_image = readImage(right_image_file)

    assert left_image.size > 0
    assert right_image.size > 0

    stereo_params = StereoParams(StereoMatcherType.STEREO_MATCHER_SGBM,
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


def test_StereoSGBM_params_read_callback():
    # Test the StereoSGBM matcher virtual Pylon stereo camera by read callback
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(
        script_path, "..", "..", "data")

    left_image_file = os.path.join(data_folder, "left.png")
    right_image_file = os.path.join(data_folder, "right.png")

    left_image = readImage(left_image_file)
    right_image = readImage(right_image_file)

    assert left_image.size > 0
    assert right_image.size > 0

    stereo_params = StereoParams(StereoMatcherType.STEREO_MATCHER_SGBM,
        11, 0, 25, True)

    matcher = createStereoMatcher(stereo_params)
    max_compute_duration = 10
    
    matcher.startComputeThread(left_image, right_image)
    read_start = time.time()
    while matcher.isComputeThreadRunning():
        # To make sure function run something
        #print("Thread is computing")
        # check read is not taking too long
        read_end = time.time()
        duration = read_end - read_start
        assert (duration < max_compute_duration)
        if (duration > max_compute_duration):
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

def test_StereoSGBM_perf_params():
    # Test performance of computing StereoSGBM disparity
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(
        script_path, "..", "..", "data")

    left_image_file = os.path.join(data_folder, "left.png")
    right_image_file = os.path.join(data_folder, "right.png")

    left_image = readImage(left_image_file)
    right_image = readImage(right_image_file)

    stereo_params = StereoParams(StereoMatcherType.STEREO_MATCHER_SGBM,
        11, 0, 25, False)

    matcher = createStereoMatcher(stereo_params)
    start = time.time()
    match_result = matcher.compute(left_image, right_image)
    end = time.time()
    assert end-start < 10