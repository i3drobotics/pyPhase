#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_utils.py
 @brief Unit tests for Utility functions
 @details Unit tests generated using PyTest
"""
import os
import random
from phase.pyphase import scaleImage, toMono, normaliseDisparity
from phase.pyphase import bgra2rgba, bgr2rgba, bgr2bgra
from phase.pyphase import cvMatIsEqual
from phase.pyphase import disparity2xyz, xyz2depth
from phase.pyphase import disparity2depth, depth2xyz, savePLY
from phase.pyphase import readImage, flip
from phase.pyphase.calib import StereoCameraCalibration
from phase.pyphase.types import MatrixUInt8, StereoMatcherType
from phase.pyphase.stereomatcher import StereoParams, createStereoMatcher

import numpy as np

def test_utils_scaleImage():
    # Test to scale image by twice the width and height
    img = np.ones((1080, 1920, 3), dtype=np.uint8)

    scaled_img = scaleImage(img, 2.0)

    assert scaled_img.shape[0] == 1080*2
    assert scaled_img.shape[1] == 1920*2

def test_utils_toMono():
    img8UC1 = np.ones((1080, 1920, 1), dtype=np.uint8)
    imgMono = np.zeros((1080, 1920, 1), dtype=np.uint8)
    assert (toMono(img8UC1, imgMono) is True)
    
    img8UC3 = np.ones((1080, 1920, 3), dtype=np.uint8)
    assert (toMono(img8UC3, imgMono) is True)

    img8UC4 = np.ones((1080, 1920, 4), dtype=np.uint8)
    assert (toMono(img8UC4, imgMono) is True)

def test_utils_normaliseDisparity():
    # Test normalise disparity matrix
    img = np.ones((1080, 1920, 3), dtype=np.uint8)

    assert (not normaliseDisparity(img).shape[2] == 1)

def test_utils_bgra2rgba():
    # Test convert bgra2rgba
    img = np.zeros((1080, 1920, 4), dtype=np.uint8)
    img[:,:,1] = 1
    img[:,:,2] = 2
    img[:,:,3] = 3

    converted_img = bgra2rgba(img)
    assert (converted_img[0,0,0]==img[0,0,2]).all()
    assert (converted_img[0,0,1]==img[0,0,1]).all()
    assert (converted_img[0,0,2]==img[0,0,0]).all()
    assert (converted_img[0,0,3]==img[0,0,3]).all()

def test_utils_bgr2bgra():
    # Test convert bgr2bgra
    img = np.zeros((1080, 1920, 3), dtype=np.uint8)
    img[:,:,1] = 1
    img[:,:,2] = 2

    converted_img = bgr2bgra(img)

    assert (converted_img[0,0,0]==img[0,0,0]).all()
    assert (converted_img[0,0,1]==img[0,0,1]).all()
    assert (converted_img[0,0,2]==img[0,0,2]).all()
    assert (img.shape[2] == 3)
    assert (not converted_img[:,:,3] is None)

def test_utils_bgr2rgba():
    # Test convert bgr2rgba
    img = np.zeros((1080, 1920, 3), dtype=np.uint8)
    img[:,:,1] = 1
    img[:,:,2] = 2

    converted_img = bgr2rgba(img)

    assert (converted_img[0,0,0]==img[0,0,2]).all()
    assert (converted_img[0,0,1]==img[0,0,1]).all()
    assert (converted_img[0,0,2]==img[0,0,0]).all()
    assert (img.shape[2] == 3)
    assert (not converted_img[:,:,3] is None)

#def test_utils_disparity2xyz
def test_Utils_readImage():
    # Test to read an image and flip
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(
        script_path, "..", "data")

    left_image_file = os.path.join(data_folder, "left.png")
    img = readImage(left_image_file)
    imgEmpty = readImage("empty")
    
    assert (not img is None)
    assert (img.shape[0] == 2048)
    assert (img.shape[1] == 2448)

    assert (imgEmpty is None)
    height = img.shape[0]
    width = img.shape[1]
    flip_img0 = flip(img, 0)

    assert (img[0,0,0] == flip_img0[height-1,0,0])

    flip_img1 = flip(img, 1)

    assert (img[0,0,0] == flip_img1[0,width-1,0])


def test_Utils_checkEqualMat():
    # Test if two matrices are equal
    # Create equal matrices
    mat_a = np.ones((3, 3, 1), dtype=np.float32)
    mat_b = np.ones((3, 3, 1), dtype=np.float32)

    # Check equal is equal check is correct
    assert (cvMatIsEqual(mat_a, mat_b))

    # Change one element to make it not equal
    mat_a[0, 0] = 0.0

    # Check is not equal check is correct
    assert (not cvMatIsEqual(mat_a, mat_b))


def test_Utils_savePly():
    # Test of save point cloud
    script_path = os.path.dirname(os.path.realpath(__file__))
    test_folder = os.path.join(script_path, "..", ".phase_test")
    left_yaml = os.path.join(test_folder, "left.yaml")
    right_yaml = os.path.join(test_folder, "right.yaml")
    out_ply = os.path.join(test_folder, "out.ply")

    if not os.path.exists(test_folder):
        os.makedirs(test_folder)

    print("Generating test data...")
    # Create calibration files
    left_yaml_data = \
        "image_width: 2448\n" \
        "image_height: 2048\n" \
        "camera_name: leftCamera\n" \
        "camera_matrix:\n" \
        "   rows: 3\n" \
        "   cols: 3\n" \
        "   data: [ 3.4782608695652175e+03, 0., 1224., 0., 3.4782608695652175e+03, 1024., 0., 0., 1. ]\n" \
        "distortion_model: plumb_bob\n" \
        "distortion_coefficients:\n" \
        "   rows: 1\n" \
        "   cols: 5\n" \
        "   data: [ 0., 0., 0., 0., 0. ]\n" \
        "rectification_matrix:\n" \
        "   rows: 3\n" \
        "   cols: 3\n" \
        "   data: [1., 0., 0., 0., 1., 0., 0., 0., 1.]\n" \
        "projection_matrix:\n" \
        "   rows: 3\n" \
        "   cols: 4\n" \
        "   data: [ 3.4782608695652175e+03, 0., 1224., 0., 0., 3.4782608695652175e+03, 1024., 0., 0., 0., 1., 0. ]\n"
    right_yaml_data = \
        "image_width: 2448\n" \
        "image_height: 2048\n" \
        "camera_name: rightCamera\n" \
        "camera_matrix:\n" \
        "   rows: 3\n" \
        "   cols: 3\n" \
        "   data: [ 3.4782608695652175e+03, 0., 1224., 0., 3.4782608695652175e+03, 1024., 0., 0., 1. ]\n" \
        "distortion_model: plumb_bob\n" \
        "distortion_coefficients:\n" \
        "   rows: 1\n" \
        "   cols: 5\n" \
        "   data: [ 0., 0., 0., 0., 0. ]\n" \
        "rectification_matrix:\n" \
        "   rows: 3\n" \
        "   cols: 3\n" \
        "   data: [1., 0., 0., 0., 1., 0., 0., 0., 1.]\n" \
        "projection_matrix:\n" \
        "   rows: 3\n" \
        "   cols: 4\n" \
        "   data: [ 3.4782608695652175e+03, 0., 1224., -3.4782608695652175e+02, 0., 3.4782608695652175e+03, 1024., 0., 0., 0., 1., 0. ]\n"

    with open(left_yaml, "w+") as f:
        f.writelines(left_yaml_data)
    with open(right_yaml, "w+") as f:
        f.writelines(right_yaml_data)
        
    # Load in default test images
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(
        script_path, "..", "data")

    left_image_file = os.path.join(data_folder, "left.png")
    right_image_file = os.path.join(data_folder, "right.png")
    left_image = readImage(left_image_file)
    right_image = readImage(right_image_file)

    # Create stereo image pair
    np_left_image = np.zeros((2048, 2448, 3), dtype=np.uint8)
    np_right_image = np.zeros((2048, 2448, 3), dtype=np.uint8)

    # Create an empty matrix for testing purpose
    np_empty = np.zeros((2048, 2448, 3), dtype=np.float32)
    Q_empty = np.zeros((4, 4), dtype=np.float32)
    
    calibration = StereoCameraCalibration.calibrationFromYAML(
        left_yaml, right_yaml)
    
    rect = calibration.rectify(left_image, right_image)

    stereo_params = StereoParams(
        StereoMatcherType.STEREO_MATCHER_BM,
        11, 0, 25, False
    )

    matcher = createStereoMatcher(stereo_params)
    
    match_result = matcher.compute(rect.left, rect.right)

    np_depth = disparity2depth(match_result.disparity, calibration.getQ())
    assert np_depth.size != 0
    assert np_depth[int(left_image.shape[0]/2),int(left_image.shape[1]/2)] > 0

    np_depth_empty = disparity2depth(match_result.disparity, Q_empty)
    #assert np.all((np_depth_empty==0)) == 1 
    assert np.all((np_depth_empty == 0))

    disparity_xyz = disparity2xyz(match_result.disparity, calibration.getQ())
    assert disparity_xyz[int(left_image.shape[0]/2),int(left_image.shape[1]/2),2] > 0

    disparity_xyz_empty = disparity2xyz(np_empty,Q_empty)
    assert np.any(disparity_xyz_empty) == 0

    xyz = depth2xyz(np_depth, calibration.getHFOV())
    assert np_depth[int(left_image.shape[0]/2),int(left_image.shape[1]/2)] > 0

    xyz_empty = depth2xyz(np_empty, calibration.getHFOV())
    assert np.any(xyz_empty) == 0

    xyz_depth = xyz2depth(xyz)
    assert xyz_depth[int(left_image.shape[0]/2),int(left_image.shape[1]/2)] > 0

    xyz_depth_empty = xyz2depth(np_empty)
    #assert np.any(xyz_depth_empty) == 0

    save_success = savePLY(out_ply, xyz, rect.left)
    assert (save_success)


if __name__ == "__main__":
    test_Utils_savePly()
