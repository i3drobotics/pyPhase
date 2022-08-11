#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_stereobm.py
 @brief Unit tests for Stereo Block Matcher class
 @details Unit tests generated using PyTest
"""

from phase.pyphase.stereomatcher import StereoBM


def test_StereoBM():
    # Test StereoBM stereo matcher
    matcher = StereoBM()
    del matcher
