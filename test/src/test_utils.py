# #!/usr/bin/env python3

# """!
#  @authors Ben Knight (bknight@i3drobotics.com)
#  @date 2021-05-26
#  @copyright Copyright (c) I3D Robotics Ltd, 2021
#  @file test_utils.py
#  @brief Unit tests for Utility functions
#  @details Unit tests generated using PyTest
# """
# import os
# import shutil
# from phase.pyphase import scaleImage, normaliseDisparity
# from phase.pyphase import bgra2rgba, bgr2rgba, bgr2bgra
# from phase.pyphase import cvMatIsEqual
# from phase.pyphase import disparity2xyz, xyz2depth
# from phase.pyphase import processStereo, disparity2depth, depth2xyz, savePLY
# from phase.pyphase import readImage, flip
# from phase.pyphase.calib import StereoCameraCalibration
# from phase.pyphase.types import MatrixUInt8, StereoMatcherType
# from phase.pyphase.stereomatcher import StereoParams
# import numpy as np

# def test_Utils_checkEqualMat():
#     # Test if two matrices are equal
#     # Create equal matrices
#     mat_a = np.ones((3, 3, 1), dtype=np.float32)
#     mat_b = np.ones((3, 3, 1), dtype=np.float32)

#     # Check equal is equal check is correct
#     assert (cvMatIsEqual(mat_a, mat_b))

#     # Change one element to make it not equal
#     mat_a[0, 0] = 0.0

#     # Check is not equal check is correct
#     assert (not cvMatIsEqual(mat_a, mat_b))


# def test_Utils_savePly():
#     # Test of save point cloud
#     script_path = os.path.dirname(os.path.realpath(__file__))
#     test_folder = os.path.join(script_path, "..", ".phase_test")
#     left_yaml = os.path.join(test_folder, "left.yaml")
#     right_yaml = os.path.join(test_folder, "right.yaml")
#     out_ply = os.path.join(test_folder, "out.ply")

#     if not os.path.exists(test_folder):
#         os.makedirs(test_folder)

#     print("Generating test data...")
#     # Create calibration files
#     left_yaml_data = \
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
#     right_yaml_data = \
#         "image_width: 2448\n" \
#         "image_height: 2048\n" \
#         "camera_name: rightCamera\n" \
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
#         "   data: [ 3.4782608695652175e+03, 0., 1224., -3.4782608695652175e+02, 0., 3.4782608695652175e+03, 1024., 0., 0., 0., 1., 0. ]\n"

#     with open(left_yaml, "w+") as f:
#         f.writelines(left_yaml_data)
#     with open(right_yaml, "w+") as f:
#         f.writelines(right_yaml_data)

#     # Create stereo image pair
#     np_left_image = np.zeros((2048, 2448, 3), dtype=np.uint8)
#     np_right_image = np.zeros((2048, 2448, 3), dtype=np.uint8)

#     calibration = StereoCameraCalibration.calibrationFromYAML(
#         left_yaml, right_yaml)

#     rect_image_pair = calibration.rectify(np_left_image, np_right_image)

#     ph_left_image = MatrixUInt8(rect_image_pair.left)
#     ph_right_image = MatrixUInt8(rect_image_pair.right)

#     stereo_params = StereoParams(
#         StereoMatcherType.STEREO_MATCHER_BM,
#         11, 0, 25, False
#     )
#     ph_disparity = processStereo(
#         stereo_params, ph_left_image, ph_right_image, calibration, False
#     )

#     assert ph_disparity.isEmpty() is False

#     np_disparity = np.array(ph_disparity)

#     np_depth = disparity2depth(np_disparity, calibration.getQ())

#     assert np_depth.size != 0

#     xyz = depth2xyz(np_depth, calibration.getHFOV())

#     save_success = savePLY(out_ply, xyz, rect_image_pair.left)
#     assert (save_success)


# if __name__ == "__main__":
#     test_Utils_savePly()
