#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_stereoi3drsgm.py
 @brief Unit tests for I3DR's Semi-Global Stereo Matcher class
 @details Unit tests generated using PyTest
"""


from phase.pyphase.stereomatcher import StereoI3DRSGM


def test_StereoI3DRSGM():
    #TODOC Description of the test
    matcher = StereoI3DRSGM()
    del matcher


def test_StereoI3DRSGM_params():
    #TODOC Description of the test
    valid = StereoI3DRSGM().isLicenseValid()
    if valid:
        matcher = StereoI3DRSGM()
        matcher.setWindowSize(11)
        matcher.setMinDisparity(0)
        matcher.setNumDisparities(16*300)
        matcher.enableSubpixel(False)
        matcher.enableInterpolation(False)
        del matcher
