#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_stereomatcher.py
 @brief Unit tests for Stereo Matcher class
 @details Unit tests generated using PyTest
"""

from phase.pyphase.types import StereoMatcherType
from phase.pyphase.stereomatcher import createStereoMatcher


def test_StereoMatcher():
    #TODOC Description of the test
    matcher = createStereoMatcher(StereoMatcherType.STEREO_MATCHER_BM)
    del matcher