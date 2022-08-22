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
from phase.pyphase.types import StereoMatcherType
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
        script_path, "..", "..", ".phase_test")

    left_image_file = os.path.join(data_folder, "left.png")
    left_image = readImage(left_image_file)
    right_image_file = os.path.join(data_folder, "right.png")
    right_image = readImage(right_image_file)

    stereo_params = StereoParams(StereoMatcherType.STEREO_MATCHER_SGBM,
        11, 0, 25, False)

    matcher = createStereoMatcher(stereo_params)

    match_result = matcher.compute(left_image, right_image)
    assert match_result.disparity[0,0] == -16
    assert match_result.disparity[20,20] == -16
    assert match_result.disparity[222,222] == -16

    del matcher


def test_StereoSGBM_params_read_callback():
    # Test the StereoSGBM matcher virtual Pylon stereo camera by read callback
    script_path = os.path.dirname(os.path.realpath(__file__))
    test_folder = os.path.join(
        script_path, "..", "..", "data")

    left_image_file = os.path.join(test_folder, "left.png")
    right_image_file = os.path.join(test_folder, "right.png")

    left_image = readImage(left_image_file)
    right_image = readImage(right_image_file)

    stereo_params = StereoParams(StereoMatcherType.STEREO_MATCHER_SGBM,
        11, 0, 25, False)

    matcher = createStereoMatcher(stereo_params)
    max_read_duration = 10
    
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