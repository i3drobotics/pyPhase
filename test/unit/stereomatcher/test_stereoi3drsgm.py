#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_stereoi3drsgm.py
 @brief Unit tests for I3DR's Semi-Global Stereo Matcher class
 @details Unit tests for use with PyTest
"""
import os
import time
from phase.pyphase.stereomatcher import StereoI3DRSGM, StereoParams
from phase.pyphase.stereomatcher import createStereoMatcher, StereoMatcherType
from phase.pyphase import readImage


def test_StereoI3DRSGM_get_set_params():
    # Test matcher parameters can be set and get functions return expected values
    matcher = StereoI3DRSGM()
    matcher.setWindowSize(11)
    matcher.setMinDisparity(0)
    matcher.setNumDisparities(25)

    # TODO get functions missing in pyphase binding
    assert matcher.getWindowSize() == 11
    assert matcher.getMinDisparity() == 0
    assert matcher.getNumDisparities() == 25


def test_StereoI3DRSGM_init_params():
    # Test matcher parameters defined at initialisation respond with correct values when using get functions 
    window_size = 11
    min_disparity = 0
    num_disparities = 25
    stereo_params = StereoParams(
        StereoMatcherType.STEREO_MATCHER_I3DRSGM, window_size, min_disparity, num_disparities, True)
    stereo_params = StereoParams(
        StereoMatcherType.STEREO_MATCHER_I3DRSGM, 11, 0, 25, True)
    matcher = StereoI3DRSGM(stereo_params)

    assert matcher.getWindowSize() == 11
    assert matcher.getMinDisparity() == 0
    assert matcher.getNumDisparities() == 25


def test_StereoI3DRSGM_compute():
    # Test disparity image can be computed from ‘compute’ function
    # when given known sample stereo image pair.
    # Will verify 3 pixel locations in the disparity image.
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(
        script_path, "..", "..", "data")

    left_image_file = os.path.join(data_folder, "left.png")
    right_image_file = os.path.join(data_folder, "right.png")

    left_image = readImage(left_image_file)
    right_image = readImage(right_image_file)

    assert left_image.size > 0
    assert right_image.size > 0
    
    stereo_params = StereoParams(
        StereoMatcherType.STEREO_MATCHER_I3DRSGM,
        9, 0, 49, True)
    matcher = createStereoMatcher(stereo_params)
    match_result = matcher.compute(left_image, right_image)

    license_valid = StereoI3DRSGM().isLicenseValid()
    if not license_valid:
        assert not match_result.valid
        assert match_result.disparity[0,0] == 0.0
        assert match_result.disparity[20,20] == 0.0
        assert match_result.disparity[222,222] == 0.0
    else:
        assert match_result.valid
        # TODO add disparity element checks for valid license compute

    del matcher


def test_StereoI3DRSGM_compute_threaded():
    # Test disparity image can be computed in thread from ‘startThreadedCompute’ function
    # when given known sample stereo image pair.
    # Will verify 3 pixel locations in the disparity image.
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(
        script_path, "..", "..", "data")

    left_image_file = os.path.join(data_folder, "left.png")
    right_image_file = os.path.join(data_folder, "right.png")

    left_image = readImage(left_image_file)
    right_image = readImage(right_image_file)

    assert left_image.size > 0
    assert right_image.size > 0

    stereo_params = StereoParams(
        StereoMatcherType.STEREO_MATCHER_I3DRSGM,
        9, 0, 49, True)
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

    license_valid = StereoI3DRSGM().isLicenseValid()
    if not license_valid:
        assert not match_result.valid
        assert match_result.disparity[0,0] == 0.0
        assert match_result.disparity[20,20] == 0.0
        assert match_result.disparity[222,222] == 0.0
    else:
        assert match_result.valid
        # TODO adjust disparity element checks for valid license compute
        # verify known unmatched point
        assert match_result.disparity[0,0] == -1.0
        valid_disp_threshold = 0.1
        # disparity values should match expected within threshold
        assert match_result.disparity[1024,1224] >= 239.5 - valid_disp_threshold
        assert match_result.disparity[1024,1224] <= 239.5 + valid_disp_threshold
        assert match_result.disparity[1400,2200] >= 224.4375 - valid_disp_threshold
        assert match_result.disparity[1400,2200] <= 224.4375 + valid_disp_threshold
