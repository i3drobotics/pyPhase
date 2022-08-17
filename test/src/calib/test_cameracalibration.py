# #!/usr/bin/env python3

# """!
#  @authors Ben Knight (bknight@i3drobotics.com)
#  @date 2021-06-28
#  @copyright Copyright (c) I3D Robotics Ltd, 2021
#  @file test_cameracalibration.py
#  @brief Unit tests for CameraCalibration class
#  @details Unit tests generated using PyTest
# """
# import os
# import time

# from phase.pyphase.calib import CameraCalibration


# def test_CameraCalibration():
#     # Test loading of calibration data from file
#     script_path = os.path.dirname(os.path.realpath(__file__))
#     test_folder = os.path.join(script_path, "..", "..", ".phase_test")
#     left_ros_yaml = os.path.join(test_folder, "left_ros.yaml")

#     if not os.path.exists(test_folder):
#         os.makedirs(test_folder)
#     start = time.time()
#     print("Generating test data...")
#     # Create calibration files
#     left_ros_yaml_data = \
#         "image_width: 2448\n" \
#         "image_height: 2048\n" \
#         "camera_name: leftCamera\n" \
#         "camera_matrix:\n" \
#         "   rows: 3\n" \
#         "   cols: 3\n" \
#         "   data: [ 3.4782608695652175e+03, 0., 1224., 0., 3.4782608695652175e+03, 1024., 0., 0., 1. ]\n" \
#         "distortion_model: plumb_bob\n" \
#         "distortion_coefficients:\n" \
#         "   rows: 1\n" \
#         "   cols: 5\n" \
#         "   data: [ 0., 0., 0., 0., 0. ]\n" \
#         "rectification_matrix:\n" \
#         "   rows: 3\n" \
#         "   cols: 3\n" \
#         "   data: [1., 0., 0., 0., 1., 0., 0., 0., 1.]\n" \
#         "projection_matrix:\n" \
#         "   rows: 3\n" \
#         "   cols: 4\n" \
#         "   data: [ 3.4782608695652175e+03, 0., 1224., 0., 0., 3.4782608695652175e+03, 1024., 0., 0., 0., 1., 0. ]\n"

#     with open(left_ros_yaml, 'w') as f:
#         f.writelines(left_ros_yaml_data)

#     cal_ros = CameraCalibration(left_ros_yaml)
#     assert(cal_ros.isValid())

#     # Test calibration access
#     assert(len(cal_ros.getCameraMatrix()) > 0)
#     assert(len(cal_ros.getDistortionCoefficients()) > 0)
#     assert(len(cal_ros.getRectificationMatrix()) > 0)
#     assert(len(cal_ros.getProjectionMatrix()) > 0)

#     end = time.time()

#     print("test_CameraCalibration finished in "+ str(end - start) + "seconds")
