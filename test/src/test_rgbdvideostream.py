#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-06-28
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_rgbdvideostream.py
 @brief Unit tests for RGBD Video Stream class
 @details Unit tests generated using PyTest
"""
import os
import cv2
import numpy as np
from phase.pyphase.types import MatrixUInt8, StereoMatcherType
from phase.pyphase.calib import StereoCameraCalibration
from phase.pyphase import processStereo, disparity2depth
from phase.pyphase import RGBDVideoWriter, RGBDVideoStream
from phase.pyphase.stereomatcher import StereoParams


def test_RGBDVideoStream():
    script_path = os.path.dirname(os.path.realpath(__file__))
    python_wrapper_proj_path = os.path.join(script_path, "../../")
    phase_proj_path = os.path.join(python_wrapper_proj_path, "../../")
    resource_folder = os.path.join(phase_proj_path, "resources")
    out_folder = os.path.join(python_wrapper_proj_path, "out")
    camera_name = "stereotheatresim"
    cal_type = "ros"
    cam_folder = os.path.join(resource_folder, "test", camera_name)
    left_yaml = os.path.join(cam_folder, cal_type, "left.yaml")
    right_yaml = os.path.join(cam_folder, cal_type, "right.yaml")
    left_image_file = os.path.join(cam_folder, "left.png")
    right_image_file = os.path.join(cam_folder, "right.png")
    out_rgb_video = os.path.join(out_folder, "rgb.mp4")
    out_depth_video = os.path.join(out_folder, "depth.avi")
    num_of_frames = 1

    if not os.path.exists(out_folder):
        os.makedirs(out_folder)

    np_left_image = cv2.imread(left_image_file, cv2.IMREAD_UNCHANGED)
    np_right_image = cv2.imread(right_image_file, cv2.IMREAD_UNCHANGED)

    calibration = StereoCameraCalibration.calibrationFromYAML(
        left_yaml, right_yaml)

    rect_image_pair = calibration.rectify(np_left_image, np_right_image)

    ph_left_image = MatrixUInt8(rect_image_pair.left)
    ph_right_image = MatrixUInt8(rect_image_pair.right)

    stereo_params = StereoParams(
        StereoMatcherType.STEREO_MATCHER_BM,
        11, 0, 25, False
    )
    ph_disparity = processStereo(
        stereo_params, ph_left_image, ph_right_image, calibration, False
    )

    assert ph_disparity.isEmpty() is False

    np_disparity = np.array(ph_disparity)

    np_depth = disparity2depth(np_disparity, calibration.getQ())

    assert np_depth.size != 0

    rgbdVideoWriter = RGBDVideoWriter(
        out_rgb_video, out_depth_video,
        ph_left_image.getColumns(), ph_left_image.getRows()
    )

    assert rgbdVideoWriter.isOpened()

    for i in range(0, num_of_frames):
        rgbdVideoWriter.add(rect_image_pair.left, np_depth)

    rgbdVideoWriter.saveThreaded()
    while(rgbdVideoWriter.isSaveThreadRunning()):
        pass

    assert rgbdVideoWriter.getSaveThreadResult()

    rgbdVideoStream = RGBDVideoStream(
        out_rgb_video, out_depth_video
    )

    assert rgbdVideoStream.isOpened()

    rgbdVideoStream.loadThreaded()

    while(rgbdVideoStream.isLoadThreadRunning()):
        pass

    assert rgbdVideoStream.getLoadThreadResult()

    # depth is coverted to scaled ushort for storage
    # so some precision is lost
    # for equality check need to have the same precision
    np_depth_sim_input = np_depth*6553.5
    # rounding needed as opencv will round rather than floor when converting
    np_depth_sim_input = np.around(np_depth_sim_input)
    np_depth_sim_input = np_depth_sim_input.astype(np.ushort)
    np_depth_sim_input = np_depth_sim_input.astype(np.float32)
    np_depth_sim_input = np_depth_sim_input*(1.0/6553.5)

    while (not rgbdVideoStream.isFinished()):
        frame = rgbdVideoStream.read()
        assert np.array_equal(frame.depth, np_depth_sim_input)

    rgbdVideoStream.close()


if __name__ == "__main__":
    test_RGBDVideoStream()
