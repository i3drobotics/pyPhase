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
import math
import numpy as np
from phase.pyphase import scaleImage, toMono, normaliseDisparity
from phase.pyphase import bgra2rgba, bgr2bgra, bgr2rgba
from phase.pyphase import readImage, cvMatIsEqual, flip
from phase.pyphase import disparity2depth, disparity2xyz, depth2xyz
from phase.pyphase import xyz2depth, savePLY


def test_utils_scaled_image_size():
    # Test image with size 2448x2048 scaled by ‘scaleImage’ function
    # with a scaling factor of 2 has an output image size of 4896x4096
    img = np.ones((2048, 2448, 3), dtype=np.uint8)
    scaling_factor = 2.0
    scaled_img = scaleImage(img, scaling_factor)

    assert scaled_img.shape[0] == 4096
    assert scaled_img.shape[1] == 4896


def test_utils_convert_mono_to_mono():
    # Test image of type CV_8UC1 converted to mono by ‘toMono’ function
    # has output image type of CV_8UC1
    img8UC1 = np.ones((2048, 2448, 1), dtype=np.uint8)
    imgMono = np.zeros((2048, 2448, 1), dtype=np.uint8)
    assert toMono(img8UC1, imgMono)
    assert imgMono.shape[2] == 1
    assert imgMono.dtype == np.uint8
    
def test_utils_valid_bgr2rgba():
    # Test image of type CV_8UC3 converted to mono by ‘toMono’ function
    # has output image type of CV_8UC1
    img8UC3 = np.ones((2048, 2448, 3), dtype=np.uint8)
    imgMono = np.zeros((2048, 2448, 1), dtype=np.uint8)
    assert toMono(img8UC3, imgMono)
    assert imgMono.shape[2] == 1
    assert imgMono.dtype == np.uint8

def test_utils_convert_bgra_to_mono():
    # Test image of type CV_8UC4 converted to mono by ‘toMono’ function
    # has output image type of CV_8UC1
    img8UC4 = np.ones((2048, 2448, 4), dtype=np.uint8)
    imgMono = np.zeros((2048, 2448, 1), dtype=np.uint8)
    assert toMono(img8UC4, imgMono)
    assert imgMono.shape[2] == 1
    assert imgMono.dtype == np.uint8


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
    # Test disparity image converted to depth by ‘disparity2Depth’ function
    # has output depth values that match expected values
    disparity = np.ones((2048, 2448, 1), dtype=np.float32)
    disparity[0,0] = -1.0
    disparity[1024,1224] = 239.5
    disparity[1400,2200] = 224.4375
    Q = np.eye(4, dtype=np.float32)

    Q[0,3] = -1224.0
    Q[1,3] = -1024.0
    Q[2,3] = 3478.26099
    Q[3,2] = 10.0
    Q[3,3] = 0.0

    depth = disparity2depth(disparity, Q)

    valid_depth_threshold = 0.001

    assert depth[0, 0] == 0
    assert depth[1024, 1224] >= 1.4523 - valid_depth_threshold
    assert depth[1024, 1224] <= 1.4523 + valid_depth_threshold
    assert depth[1400, 2200] >= 1.54977 - valid_depth_threshold
    assert depth[1400, 2200] <= 1.54977 + valid_depth_threshold


def test_utils_empty_disparity2depth():
    # Test providing empty disparity or q matrix to ‘disparity2Depth’ function
    # will return an empty depth image
    # Create an empty matrix for testing purpose
    empty = np.array([])
    disparity = np.zeros((2048, 2448), dtype=np.uint8)
    Q = np.zeros((4, 4), dtype=np.float32)

    # Convert an empty disparity/ empty Q matrix to depth
    depth1 = disparity2depth(disparity, empty)
    depth2 = disparity2depth(empty, Q)
    depth3 = disparity2depth(empty, empty)
    assert depth1 == None
    assert depth2 == None
    assert depth3 == None


def test_utils_valid_disparity2xyz():
    # Test disparity image converted to depth by ‘disparity2Xyz’ function
    # has output xyz values that match expected values
    disparity = np.ones((2048, 2448, 1), dtype=np.float32)
    disparity[0,0] = -1.0
    disparity[1024,1224] = 239.5
    disparity[1400,2200] = 224.4375
    Q = np.eye(4, dtype=np.float32)

    Q[0,3] = -1224.0
    Q[1,3] = -1024.0
    Q[2,3] = 3478.26099
    Q[3,2] = 10.0
    Q[3,3] = 0.0

    xyz = disparity2xyz(disparity, Q)

    valid_xyz_threshold = 0.001

    assert xyz[0,0,0] == 0
    assert xyz[0,0,1] == 0
    assert xyz[0,0,2] == 0
    assert xyz[1024,1224,0] >= 0 - valid_xyz_threshold
    assert xyz[1024,1224,0] <= 0 + valid_xyz_threshold
    assert xyz[1024,1224,1] >= 0 - valid_xyz_threshold
    assert xyz[1024,1224,1] <= 0 + valid_xyz_threshold    
    assert xyz[1024,1224,2] >= 1.4523 - valid_xyz_threshold
    assert xyz[1024,1224,2] <= 1.4523 + valid_xyz_threshold
    assert xyz[1400,2200,0] >= 0.43486 - valid_xyz_threshold
    assert xyz[1400,2200,0] <= 0.43486 + valid_xyz_threshold
    assert xyz[1400,2200,1] >= 0.16753 - valid_xyz_threshold
    assert xyz[1400,2200,1] <= 0.16753 + valid_xyz_threshold    
    assert xyz[1400,2200,2] >= 1.54977 - valid_xyz_threshold
    assert xyz[1400,2200,2] <= 1.54977 + valid_xyz_threshold


def test_utils_empty_disparity2xyz():
    # Test providing empty disparity or q matrix to ‘disparity2xyz’ function
    # will return an empty xyz image
    # Create an empty matrix for testing purpose
    empty = np.array([])
    disparity = np.zeros((2048, 2448), dtype=np.uint8)
    Q = np.zeros((4, 4), dtype=np.float32)

    # Convert an empty disparity/ empty Q matrix to 3D xyz points
    xyz1 = disparity2xyz(disparity, empty)
    xyz2 = disparity2xyz(empty, Q)
    xyz3 = disparity2xyz(empty, empty)
    assert xyz1 == None
    assert xyz2 == None
    assert xyz3 == None


def test_utils_valid_depth2xyz():
    # Test depth image converted to depth by ‘depth2Xyz’ function
    # has output xyz values that match expected values
    depth = np.ones((2048, 2448, 1), dtype=np.float32)
    depth[0,0] = 0.0
    depth[1024,1224] = 1.4523
    depth[1400,2200] = 1.54977

    hfov = 2*math.atan(1224/3478.26099)

    xyz = depth2xyz(depth, hfov)

    valid_xyz_threshold = 0.001

    assert xyz[0,0,0] == 0
    assert xyz[0,0,1] == 0
    assert xyz[0,0,2] == 0
    assert xyz[1024,1224,0] >= 0 - valid_xyz_threshold
    assert xyz[1024,1224,0] <= 0 + valid_xyz_threshold
    assert xyz[1024,1224,1] >= 0 - valid_xyz_threshold
    assert xyz[1024,1224,1] <= 0 + valid_xyz_threshold    
    assert xyz[1024,1224,2] >= 1.4523 - valid_xyz_threshold
    assert xyz[1024,1224,2] <= 1.4523 + valid_xyz_threshold
    assert xyz[1400,2200,0] >= 0.41309 - valid_xyz_threshold
    assert xyz[1400,2200,0] <= 0.41309 + valid_xyz_threshold
    assert xyz[1400,2200,1] >= 0.1608 - valid_xyz_threshold
    assert xyz[1400,2200,1] <= 0.1608 + valid_xyz_threshold    
    assert xyz[1400,2200,2] >= 1.54977 - valid_xyz_threshold
    assert xyz[1400,2200,2] <= 1.54977 + valid_xyz_threshold


def test_utils_empty_depth2xyz():
    # Test providing empty depth or q matrix to ‘depth2Xyz’ function
    # will return an empty xyz image
    empty = np.array([])

    # Convert an empty depth to 3D xyz points
    xyz = depth2xyz(empty, 20)
    assert xyz == None


def test_utils_valid_xyz2depth():
    # Test xyz image converted to depth by ‘xyz2Depth’ function
    # has output depth values that match expected values
    xyz = np.ones((2048, 2448, 3), dtype=np.float32)
    xyz[0,0,:] = [0,0,0]
    xyz[1024,1224,:] = [0,0,1.4523]
    xyz[1400,2200,:] = [0.41309,0.1608,1.54977]

    valid_depth_threshold = 0.001
    
    # Convert 3D xyz points to depth
    depth = xyz2depth(xyz)
    assert depth[0, 0] == 0
    assert depth[1024, 1224] >= 1.4523 - valid_depth_threshold
    assert depth[1024, 1224] <= 1.4523 + valid_depth_threshold
    assert depth[1400, 2200] >= 1.54977 - valid_depth_threshold
    assert depth[1400, 2200] <= 1.54977 + valid_depth_threshold


def test_utils_empty_xyz2depth():
    # Test providing empty xyz to ‘xyz2Depth’ function
    # will return an empty depth image
    empty = np.array([])

    depth = xyz2depth(empty)
    assert depth == None


def test_utils_valid_readImage():
    # Test trying to read image that does not exist
    # using ‘readImage’ function results in empty image
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(
        script_path, "..", "data")

    left_image_file = os.path.join(data_folder, "left.png")
    image = readImage(left_image_file)
    
    # Check the img is not empty and load height and width
    assert image is not None
    assert image.shape[0] == 2048
    assert image.shape[1] == 2448

    
def test_utils_empty_readImage():
    # Test trying to read image that does not exist
    # using ‘readImage’ function results in empty image
    image = readImage("invalid/file/path")

    # Check empty image returns None
    assert image is None


def test_utils_flip_horizontal():
    # Test image flipped horizontally using ‘flip’ function has
    # pixel values that matching input in opposite side on the image.
    # E.g. pixel from top left corner in input matches pixel from top right corner in output image 
    img = np.random.random((10,10))

    # Check image is flipped
    flipped_img = flip(img, 0)
    orig_top_left = img[0,0]
    flipped_top_right = flipped_img[flipped_img.shape[1]-1,0]
    assert orig_top_left == flipped_top_right


def test_utils_flip_vertical():
    # Test image flipped vertically using ‘flip’ function has pixel values pixel values
    # that matching input in opposite side on the image.
    # E.g. pixel from top left corner in input matches pixel from cornerbottom left in output image 
    img = np.random.random((10,10))

    # Check image is flipped
    flipped_img = flip(img, 1)
    orig_top_left = img[0,0]
    flipped_bottom_left = flipped_img[0,flipped_img.shape[0]-1]
    assert orig_top_left == flipped_bottom_left


def test_utils_savePly():
    # Test point cloud data represented as RGB color and XYZ images that are saved
    # to PLY using ‘savePLY’ function result in PLY file in expected output location
    xyz = np.ones((2048, 2448, 3), dtype=np.float32)
    rgb = np.ones((2048, 2448, 3), dtype=np.uint8)

    script_path = os.path.dirname(os.path.realpath(__file__))
    test_folder = os.path.join(script_path, "..", ".phase_test")
    out_ply = os.path.join(test_folder, "out.ply")

    # Save the pointcloud
    save_success = savePLY(out_ply, xyz, rgb)
    assert (save_success)


def test_utils_checkEqualMat():
    # Test two cv::Mat’s that are equal are reported as equal by ‘cvMatIsEqual’ function
    # Create equal matrices
    mat_a = np.ones((2048, 2448, 1), dtype=np.float32)
    mat_b = np.ones((2048, 2448, 1), dtype=np.float32)

    # Check equal is equal check is correct
    assert (cvMatIsEqual(mat_a, mat_b))

    # Change one element to make it not equal
    mat_a[0, 0] = 0.0

    # Check is not equal check is correct
    assert (not cvMatIsEqual(mat_a, mat_b))