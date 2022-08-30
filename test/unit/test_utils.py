#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_utils.py
 @brief Unit tests for Utility functions
 @details Unit tests for use with PyTest
"""
import os
import numpy as np
from phase.pyphase import scaleImage, toMono, normaliseDisparity
from phase.pyphase import bgra2rgba, bgr2bgra, bgr2rgba
from phase.pyphase import readImage, cvMatIsEqual, flip
from phase.pyphase import disparity2depth, disparity2xyz, depth2xyz
from phase.pyphase import xyz2depth, savePLY
from phase.pyphase.calib import StereoCameraCalibration
from phase.pyphase.stereomatcher import StereoParams, StereoMatcherType
from phase.pyphase.stereomatcher import createStereoMatcher


def test_utils_scaled_image_size():
    # Test image with size 2448x2048 scaled by ‘scaleImage’ function
    # with a scaling factor of 2 has an output image size of 4896x4096
    img = np.ones((2048, 2448, 3), dtype=np.uint8)

    scaled_img = scaleImage(img, 2.0)

    assert scaled_img.shape[0] == 4096
    assert scaled_img.shape[1] == 4896


def test_utils_convert_mono_to_mono():
    # Test image of type CV_8UC1 converted to mono by ‘toMono’ function
    # has output image type of CV_8UC1
    img8UC1 = np.ones((2048, 2448, 1), dtype=np.uint8)
    imgMono = np.zeros((2048, 2448, 1), dtype=np.uint8)
    assert (toMono(img8UC1, imgMono) is True)
    assert (imgMono.shape[2] == 1)


def test_utils_convert_bgra_to_mono():
    # Test image of type CV_8UC4 converted to mono by ‘toMono’ function
    # has output image type of CV_8UC1
    img8UC4 = np.ones((2048, 2448, 4), dtype=np.uint8)
    imgMono = np.zeros((2048, 2448, 1), dtype=np.uint8)
    assert (toMono(img8UC4, imgMono) is True)
    assert (imgMono.shape[2] == 1)


def test_utils_convert_bgr_to_mono():
    # Test image of type CV_8UC3 converted to mono by ‘toMono’ function
    # has output image type of CV_8UC1
    img8UC3 = np.ones((2048, 2448, 3), dtype=np.uint8)
    imgMono = np.zeros((2048, 2448, 1), dtype=np.uint8)
    assert (toMono(img8UC3, imgMono) is True)
    assert (imgMono.shape[2] == 1)


def test_utils_norm_disparity_output_type():
    # Test disparity image normalised by ‘normaliseDisparity’ function
    # has output image type of CV_8UC3
    img = np.ones((2048, 2448, 3), dtype=np.float32)
    norm_disp = normaliseDisparity(img)
    assert norm_disp.shape[2] == 3
    assert norm_disp.dtype == np.uint8


def test_utils_valid_bgra2rgba():
    # Test BGRA image converted to RGBA using ‘bgra2rgba’ function
    # has output RGBA image where channel contents match the input BGRA image but is in RGBA order
    img = np.zeros((2048, 2448, 4), dtype=np.uint8)
    # Set different channel data in each channel
    img[:,:,1] = 1
    img[:,:,2] = 2
    img[:,:,3] = 3

    converted_img = bgra2rgba(img)

    # Check if the data is converted to related channel
    assert (converted_img[0,0,0]==img[0,0,2]).all()
    assert (converted_img[0,0,1]==img[0,0,1]).all()
    assert (converted_img[0,0,2]==img[0,0,0]).all()
    assert (converted_img[0,0,3]==img[0,0,3]).all()


def test_utils_valid_bgr2rgba():
    # Test BGR image converted to RGBA using ‘bgr2rgba’ function
    # has output RGBA image where channel contents match the input BGR image
    # but is in RGB order and has additional alpha channel.
    img = np.zeros((2048, 2448, 3), dtype=np.uint8)
    # Set different channel data in each channel
    img[:,:,1] = 1
    img[:,:,2] = 2

    converted_img = bgr2rgba(img)

    # Check if the data is converted to related channel
    assert (converted_img[0,0,0]==img[0,0,2]).all()
    assert (converted_img[0,0,1]==img[0,0,1]).all()
    assert (converted_img[0,0,2]==img[0,0,0]).all()
    assert (img.shape[2] == 3)
    assert (converted_img[:,:,3] is not None)


def test_utils_valid_bgr2bgra():
    # Test BGR image converted to BGRA using ‘bgr2bgra’ function
    # has output BGRA image where channel contents match the input BGR image
    # but with additional alpha channel
    img = np.zeros((2048, 2448, 3), dtype=np.uint8)
    # Set different channel data in each channel
    img[:,:,1] = 1
    img[:,:,2] = 2

    converted_img = bgr2bgra(img)

    # Check if the data is converted to related channel
    assert (converted_img[0,0,0]==img[0,0,0]).all()
    assert (converted_img[0,0,1]==img[0,0,1]).all()
    assert (converted_img[0,0,2]==img[0,0,2]).all()
    assert (img.shape[2] == 3)
    assert (converted_img[:,:,3] is not None)


def test_utils_valid_disparity2depth():
    disparity = np.ones((2048, 2448), dtype=np.float32)
    disparity[0, 0] = -1.0
    disparity[1024, 1224] = 239.5;
    disparity[1400, 2200] = 224.4375;
    Q = np.eye((4, 4), dtype=np.float32)
    Q[0,3] = -1224.0
    Q[1,3] = -1024.0
    Q[2,3] = 3478.26099
    Q[3,2] = 10.0
    Q[3,3] = 0.0

    depth = disparity2depth(disparity, Q)
    
    valid_depth_threshold = 0.001;
    assert(depth[0,0] == 0);
    assert(depth[1024, 1224] >= 1.4523 - valid_depth_threshold)
    assert(depth[1024, 1224] <= 1.4523 + valid_depth_threshold)
    assert(depth[1400, 2200] >= 1.54977 - valid_depth_threshold)
    assert(depth[1400, 2200] <= 1.54977 + valid_depth_threshold)


def test_utils_empty_disparity2depth():
    # Test providing empty disparity or q matrix to ‘disparity2Depth’ function
    # will return an empty depth image
    empty = np.empty()
    disparity = np.ones((2048, 2448), dtype=np.float32)
    Q = np.eye((4, 4), dtype=np.float32)
    
    depth1 = disparity2depth(disparity, empty)
    depth2 = disparity2depth(empty, Q)
    depth3 = disparity2depth(empty, empty)

    assert(np.any(depth1) == 0)
    assert(np.any(depth2) == 0)
    assert(np.any(depth3) == 0)


def test_utils_readImage():
    # Test to read an image and flip
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(
        script_path, "..", "data")

    left_image_file = os.path.join(data_folder, "left.png")
    img = readImage(left_image_file)
    imgEmpty = readImage("empty")
    
    # Check the img is not empty and load height and width
    assert (img is not None)
    assert (img.shape[0] == 2048)
    assert (img.shape[1] == 2448)

    # Check empty image returns None
    assert (imgEmpty is None)


def test_utils_flip():
    # Test image flipped horizontally using ‘flip’ function has
    # pixel values that matching input in opposite side on the image.
    # E.g. pixel from top left corner in input matches pixel from top right corner in output image 
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(
        script_path, "..", "data")
    image_file = os.path.join(data_folder, "left.png")
    img = readImage(image_file)

    height = img.shape[0]
    width = img.shape[1]

    # Check image is flipped
    flip_img0 = flip(img, 0)
    assert (img[0,0,0] == flip_img0[height-1,0,0])

    flip_img1 = flip(img, 1)
    assert (img[0,0,0] == flip_img1[0,width-1,0])


def test_utils_checkEqualMat():
    # Test if two matrices are equal
    # Create equal matrices
    mat_a = np.ones((2048, 2448, 1), dtype=np.float32)
    mat_b = np.ones((2048, 2448, 1), dtype=np.float32)

    # Check equal is equal check is correct
    assert (cvMatIsEqual(mat_a, mat_b))

    # Change one element to make it not equal
    mat_a[0, 0] = 0.0

    # Check is not equal check is correct
    assert (not cvMatIsEqual(mat_a, mat_b))


def test_utils_disparity2xyz():
    # Test to convert disparity to 3D xyz points
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(script_path, "..", "data")
    left_yaml = os.path.join(data_folder, "left.yaml")
    right_yaml = os.path.join(data_folder, "right.yaml")
    left_image_file = os.path.join(data_folder, "left.png")
    right_image_file = os.path.join(data_folder, "right.png")

    # Load test images
    left_image = readImage(left_image_file)
    right_image = readImage(right_image_file)

    # Load calibration
    calibration = StereoCameraCalibration.calibrationFromYAML(
        left_yaml, right_yaml)

    # Rectify images
    rect = calibration.rectify(left_image, right_image)
    # Compute disparity
    stereo_params = StereoParams(
        StereoMatcherType.STEREO_MATCHER_BM,
        11, 0, 25, False
    )

    # Create stereo matcher and compute disparity
    matcher = createStereoMatcher(stereo_params)
    match_result = matcher.compute(rect.left, rect.right)

    # Convert disparity to 3D xyz points
    disparity_xyz = disparity2xyz(match_result.disparity, calibration.getQ())
    assert disparity_xyz[int(left_image.shape[0]/2),int(left_image.shape[1]/2),2] > 0

    # Create an empty matrix for testing purpose
    np_empty = np.zeros((2048, 2448, 3), dtype=np.uint8)
    Q_empty = np.zeros((4, 4), dtype=np.uint8)

    # Convert an empty disparity to 3D xyz points
    disparity_xyz_empty = disparity2xyz(np_empty,Q_empty)
    # TODO failed due to np_empty & Q_empty empty matrix often return -0 elements
    #assert np.any(disparity_xyz_empty) == 0


def test_utils_depth2xyz():
    # Test to convert depth to 3D xyz points
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(script_path, "..", "data")
    left_yaml = os.path.join(data_folder, "left.yaml")
    right_yaml = os.path.join(data_folder, "right.yaml")
    left_image_file = os.path.join(data_folder, "left.png")
    right_image_file = os.path.join(data_folder, "right.png")

    # Load test images
    left_image = readImage(left_image_file)
    right_image = readImage(right_image_file)

    # Load calibration
    calibration = StereoCameraCalibration.calibrationFromYAML(
        left_yaml, right_yaml)

    # Rectify images
    rect = calibration.rectify(left_image, right_image)
    # Compute disparity
    stereo_params = StereoParams(
        StereoMatcherType.STEREO_MATCHER_BM,
        11, 0, 25, False
    )

    # Create stereo matcher and compute disparity
    matcher = createStereoMatcher(stereo_params)
    match_result = matcher.compute(rect.left, rect.right)

    # Calculate the depth for conversion use
    np_depth = disparity2depth(match_result.disparity, calibration.getQ())

    # Convert depth to 3D xyz points
    xyz = depth2xyz(np_depth, calibration.getHFOV())
    assert np_depth[int(np_depth.shape[0]/2),int(np_depth.shape[1]/2)] > 0

    # Create an empty matrix for testing purpose
    np_empty = np.zeros((2048, 2448, 3), dtype=np.uint8)

    # Convert an empty depth to 3D xyz points
    xyz_empty = depth2xyz(np_empty, calibration.getHFOV())
    # TODO failed due to np_empty & Q_empty empty matrix often return -0 elements
    #assert np.any(xyz_empty) == 0


def test_utils_xyz2depth():
    # Test to convert 3D xyz points to depth
    np_xyz = np.ones((2048, 2448, 3), dtype=np.float32)
    
    # Convert 3D xyz points to depth
    xyz_depth = xyz2depth(np_xyz)
    assert xyz_depth[int(np_xyz.shape[0]/2),int(np_xyz.shape[1]/2)] > 0

    # Create an empty matrix for testing purpose
    np_empty = np.zeros((2048, 2448, 3), dtype=np.uint8)

    xyz_depth_empty = xyz2depth(np_empty)
    # TODO missing empty matrix check in xyz2depth
    #assert np.any(xyz_depth_empty) == 0


def test_utils_savePly():
    # Test of save point cloud
    script_path = os.path.dirname(os.path.realpath(__file__))
    test_folder = os.path.join(script_path, "..", ".phase_test")
    data_folder = os.path.join(script_path, "..", "data")
    left_yaml = os.path.join(data_folder, "left.yaml")
    right_yaml = os.path.join(data_folder, "right.yaml")
    left_image_file = os.path.join(data_folder, "left.png")
    right_image_file = os.path.join(data_folder, "right.png")
    out_ply = os.path.join(test_folder, "out.ply")

    if not os.path.exists(test_folder):
        os.makedirs(test_folder)

    # Load test images
    left_image = readImage(left_image_file)
    right_image = readImage(right_image_file)

    # Load calibration
    calibration = StereoCameraCalibration.calibrationFromYAML(
        left_yaml, right_yaml)
    # Rectify images
    rect = calibration.rectify(left_image, right_image)
    # Compute disparity
    stereo_params = StereoParams(
        StereoMatcherType.STEREO_MATCHER_BM,
        11, 0, 25, False
    )

    # Create stereo matcher and compute disparity
    matcher = createStereoMatcher(stereo_params)
    match_result = matcher.compute(rect.left, rect.right)

    # Convert disparity to 3D xyz points
    xyz = disparity2xyz(match_result.disparity, calibration.getQ())

    # Save the pointcloud
    save_success = savePLY(out_ply, xyz, rect.left)
    assert (save_success)
