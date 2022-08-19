#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_abstractstereomatcher.py
 @brief Unit tests for Abstract Stereo Matcher class
 @details Unit tests generated using PyTest
"""

import os
from phase.pyphase import readImage
from phase.pyphase.calib import StereoCameraCalibration
from phase.pyphase.types import StereoMatcherType
from phase.pyphase.stereomatcher import StereoI3DRSGM
from phase.pyphase.stereomatcher import StereoParams, createStereoMatcher

def test_AbstractStereoMatcher():
    # TODO add tests for AbstractStereoMatcher
    
    # Load in default test images
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(
        script_path, "..", "data")

    left_image_file = os.path.join(data_folder, "left.png")
    right_image_file = os.path.join(data_folder, "right.png")
    left_yaml = os.path.join(data_folder, "left.yaml")
    right_yaml = os.path.join(data_folder, "right.yaml")

    left_image = readImage(left_image_file)
    right_image = readImage(right_image_file)

    license_valid = StereoI3DRSGM().isLicenseValid()
    if license_valid:
        print("I3DRSGM license accepted")
    else:
        print("Missing or invalid I3DRSGM license")
    # Check for I3DRSGM license
    if license_valid:
        stereo_params = StereoParams(
            StereoMatcherType.STEREO_MATCHER_I3DRSGM,
            9, 0, 49, False
        )
    
    calibration = StereoCameraCalibration.calibrationFromYAML(
    left_yaml, right_yaml)

    matcher = createStereoMatcher(stereo_params)

    #rect = calibration.rectify(left_image, right_image)
    match_result = matcher.compute(left_image, right_image)

    assert match_result.valid == 1