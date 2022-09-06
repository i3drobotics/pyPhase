#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_stereosgbm.py
 @brief Unit tests for Stereo Semi-Global Block Matcher class
 @details Unit tests for use with PyTest
"""
import os
import time
import phase.pyphase as phase


def test_StereoSGBM_get_set_params():
    # Test matcher parameters can be set and get functions return expected values
    window_size = 11
    min_disparity = 0
    num_disparities = 25
    matcher = phase.stereomatcher.StereoSGBM()
    matcher.setWindowSize(window_size)
    matcher.setMinDisparity(min_disparity)
    matcher.setNumDisparities(num_disparities)

    assert matcher.getWindowSize() == window_size
    assert matcher.getMinDisparity() == min_disparity
    assert matcher.getNumDisparities() == num_disparities


def test_StereoSGBM_init_params():
    # Test matcher parameters defined at initialisation respond with correct values when using get functions 
    window_size = 11
    min_disparity = 0
    num_disparities = 25
    stereo_params = phase.stereomatcher.StereoParams(
        phase.stereomatcher.StereoMatcherType.STEREO_MATCHER_SGBM,
        window_size, min_disparity, num_disparities, True)
    matcher = phase.stereomatcher.StereoSGBM(stereo_params)

    assert matcher.getWindowSize() == window_size
    assert matcher.getMinDisparity() == min_disparity
    assert matcher.getNumDisparities() == num_disparities


def test_StereoSGBM_compute():
    # Test disparity image can be computed from ‘compute’ function
    # when given known sample stereo image pair.
    # Will verify 3 pixel locations in the disparity image.
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(
        script_path, "..", "..", "data")

    left_image_file = os.path.join(data_folder, "left.png")
    right_image_file = os.path.join(data_folder, "right.png")

    left_image = phase.readImage(left_image_file)
    right_image = phase.readImage(right_image_file)

    assert left_image.size > 0
    assert right_image.size > 0

    stereo_params = phase.stereomatcher.StereoParams(StereoMatcherType.STEREO_MATCHER_SGBM,
        11, 0, 25, True)
    matcher = phase.stereomatcher.createStereoMatcher(stereo_params)

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


def test_StereoSGBM_threaded_compute():
    # Test disparity image can be computed in thread from ‘startThreadedCompute’ function
    # when given known sample stereo image pair.
    # Will verify 3 pixel locations in the disparity image.
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(
        script_path, "..", "..", "data")

    left_image_file = os.path.join(data_folder, "left.png")
    right_image_file = os.path.join(data_folder, "right.png")

    left_image = phase.readImage(left_image_file)
    right_image = phase.readImage(right_image_file)

    assert left_image.size > 0
    assert right_image.size > 0

    stereo_params = phase.stereomatcher.StereoParams(StereoMatcherType.STEREO_MATCHER_SGBM,
        11, 0, 25, True)

    matcher = phase.stereomatcher.createStereoMatcher(stereo_params)
    max_compute_duration = 30
    
    matcher.startComputeThread(left_image, right_image)
    read_start = time.time()
    while matcher.isComputeThreadRunning():
        # To make sure function run something
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
