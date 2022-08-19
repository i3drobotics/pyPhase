#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_stereomatcher.py
 @brief Unit tests for Stereo Matcher class
 @details Unit tests generated using PyTest
"""

from phase.pyphase.stereomatcher import StereoMatcherType, StereoParams
from phase.pyphase.stereomatcher import createStereoMatcher

# TODO fix segmentation fault in createStereoMatcher
def test_StereoMatcher():
    # Test creation of stereo matcher using createStereoMatcher function
    matcher_type = StereoMatcherType.STEREO_MATCHER_BM
    stereo_params = StereoParams(
        matcher_type,
        11, 0, 25, False
    )
    # matcher = createStereoMatcher(StereoMatcherType.STEREO_MATCHER_BM)
    # matcher = createStereoMatcher(stereo_params)
    # del matcher
