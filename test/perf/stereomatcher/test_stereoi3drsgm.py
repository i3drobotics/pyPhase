#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_stereoi3drsgm.py
 @brief Performance tests for I3DR's Semi-Global Stereo Matcher class
 @details Performance tests generated using PyTest
"""
import time
import os
from phase.pyphase import readImage
from phase.pyphase.stereomatcher import StereoParams, StereoMatcherType
from phase.pyphase.stereomatcher import createStereoMatcher
from phase.pyphase.stereomatcher import StereoI3DRSGM


def test_StereoI3DRSGM_perf_compute():
    # Test generation of disparity from stereo image pair
    # with image size of 2448x2048 is computed using ‘compute’ function
    # in 5s
    licensed_timeout = 5 #seconds
    unlicensed_timeout = 3 #seconds
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(
        script_path, "..", "..", "data")

    stereo_params = StereoParams(
        StereoMatcherType.STEREO_MATCHER_I3DRSGM,
        9, 0, 49, True)

    matcher = createStereoMatcher(stereo_params)

    left_image_file = os.path.join(data_folder, "left.png")
    right_image_file = os.path.join(data_folder, "right.png")

    left_image = readImage(left_image_file)
    right_image = readImage(right_image_file)

    start = time.time()
    match_result = matcher.compute(left_image, right_image)
    end = time.time()
    duration = end - start

    license_valid = StereoI3DRSGM().isLicenseValid()
    if license_valid:
        assert match_result.valid
        assert duration < licensed_timeout
    else:
        assert not match_result.valid
        assert duration < unlicensed_timeout

    del matcher