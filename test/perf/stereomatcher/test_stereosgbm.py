#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_stereosgbm.py
 @brief Performance tests for Stereo Semi-Global Block Matcher class
 @details Performance tests generated using PyTest
"""
import time
import os
from phase.pyphase import readImage
from phase.pyphase.stereomatcher import StereoParams, StereoMatcherType
from phase.pyphase.stereomatcher import createStereoMatcher


def test_StereoSGBM_perf_compute():
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
    duration = end - start
    assert duration < 10