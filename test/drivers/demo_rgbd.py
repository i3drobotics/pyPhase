#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file demo_rgbd.py
 @brief Example application using I3DR Stereo Vision Python API
"""
import os
import sys
import cv2
import numpy as np
p = os.path.abspath('.')
sys.path.insert(1, p)
from phase.pyphase.types import MatrixUInt8, StereoMatcherType
from phase.pyphase.calib import StereoCameraCalibration
from phase.pyphase import processStereo, disparity2depth
from phase.pyphase import RGBDVideoWriter, RGBDVideoStream
from phase.pyphase.stereomatcher import StereoParams


script_path = os.path.dirname(os.path.realpath(__file__))
python_wrapper_proj_path = os.path.join(script_path, "../../")
phase_proj_path = os.path.join(python_wrapper_proj_path, "../../")
resource_folder = os.path.join(phase_proj_path, "resources")
out_folder = os.path.join(python_wrapper_proj_path, "out")
camera_name = "stereotheatresim"

# Define calibration files
left_yaml = os.path.join(
    resource_folder, "test", camera_name, "ros/left.yaml")
right_yaml = os.path.join(
    resource_folder, "test", camera_name, "ros/right.yaml")

# Define stereo image pair
left_image_file = os.path.join(
    resource_folder, "test", camera_name, "left.png")
right_image_file = os.path.join(
    resource_folder, "test", camera_name, "right.png")

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
    stereo_params,
    ph_left_image, ph_right_image, calibration, False
)

if ph_disparity.isEmpty():
    raise Exception("Failed to process stereo")

np_disparity = np.array(ph_disparity)

np_depth = disparity2depth(np_disparity, calibration.getQ())

if np_depth.size == 0:
    raise Exception("Failed to convert disparity to depth")

rgbdVideoWriter = RGBDVideoWriter(
    out_rgb_video, out_depth_video,
    ph_left_image.getColumns(), ph_left_image.getRows()
)

if not rgbdVideoWriter.isOpened():
    raise Exception("Failed to open RGBD video for writing")

for i in range(0, num_of_frames):
    rgbdVideoWriter.add(rect_image_pair.left, np_depth)

rgbdVideoWriter.saveThreaded()
while(rgbdVideoWriter.isSaveThreadRunning()):
    pass

if not rgbdVideoWriter.getSaveThreadResult():
    raise Exception("Error saving RGBD video")

rgbdVideoStream = RGBDVideoStream(
    out_rgb_video, out_depth_video
)

if not rgbdVideoStream.isOpened():
    raise Exception("Failed to open RGBD video stream")

rgbdVideoStream.loadThreaded()

while(rgbdVideoStream.isLoadThreadRunning()):
    pass

if not rgbdVideoStream.getLoadThreadResult():
    raise Exception("Failed to load RGBD video stream")

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
    if not np.array_equal(frame.depth, np_depth_sim_input):
        raise Exception("Depth loaded from RGBD video does not match origional depth")

rgbdVideoStream.close()
