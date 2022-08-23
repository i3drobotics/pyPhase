#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2022-08-23
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file test_utils.py
 @brief Perf tests for Utility functions
 @details Perf tests generated using PyTest
"""
import time
import os
import numpy as np
from phase.pyphase import toMono, cvMatIsEqual, scaleImage
from phase.pyphase import bgra2rgba, bgr2bgra, bgr2rgba
from phase.pyphase import disparity2depth, disparity2xyz, depth2xyz
from phase.pyphase import xyz2depth, savePLY
from phase.pyphase import readImage, flip
from phase.pyphase.calib import StereoCameraCalibration
from phase.pyphase.stereomatcher import StereoParams, StereoMatcherType
from phase.pyphase.stereomatcher import createStereoMatcher


def test_utils_perf_scaleImage():
    # Test performance of scaleImage
    img = np.ones((480, 640, 3), dtype=np.uint8)
    start = time.time()

    scaled_img = scaleImage(img, 2.0)

    end = time.time()
    duration = end - start
    assert duration < 0.1

    img2 = np.ones((2048, 2448, 3), dtype=np.uint8)

    start = time.time()

    scaled_img = scaleImage(img2, 2.0)

    end = time.time()
    duration = end - start
    assert duration < 0.5


def test_utils_perf_toMono():
    # Test performance of convert toMono
    imgMono = np.zeros((2048, 2448, 1), dtype=np.uint8)
    img8UC3 = np.ones((2048, 2448, 3), dtype=np.uint8)

    start = time.time()
    assert (toMono(img8UC3, imgMono) is True)
    end = time.time()
    duration = end - start
    assert duration < 0.1


def test_utils_perf_bgra2rgba():
    # Test performance of convert bgra2rgba
    img = np.zeros((2048, 2448, 4), dtype=np.uint8)

    start = time.time()
    converted_img = bgra2rgba(img)
    end = time.time()
    duration = end - start
    assert duration < 0.1


def test_utils_perf_bgr2bgra():
    # Test performance of convert bgr2bgra
    img = np.zeros((2048, 2448, 3), dtype=np.uint8)

    start = time.time()
    converted_img = bgr2bgra(img)
    end = time.time()
    duration = end - start
    assert duration < 0.5
    

def test_utils_perf_bgr2rgba():
    # Test performance of convert bgr2rgba
    img = np.zeros((2048, 2448, 3), dtype=np.uint8)
    
    start = time.time()
    converted_img = bgr2rgba(img)
    end = time.time()
    duration = end - start
    assert duration < 0.5


def test_Utils_perf_readImage():
    # Test performance of read an image and flip
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(
        script_path, "..", "data")

    left_image_file = os.path.join(data_folder, "left.png")
    start = time.time()
    img = readImage(left_image_file)
    end = time.time()
    duration = end - start
    assert duration < 0.2
    
    
def test_Utils_perf_flip():
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(
        script_path, "..", "data")
    image_file = os.path.join(data_folder, "left.png")
    img = readImage(image_file)

    # Flip image
    start = time.time()
    flip_img0 = flip(img, 0)
    end = time.time()
    duration = end - start
    assert duration < 0.1


def test_Utils_perf_checkEqualMat():
    # Test performance of two matrices are equal
    # Create equal matrices
    mat_a = np.ones((2048, 2448, 1), dtype=np.float32)
    mat_b = np.ones((2048, 2448, 1), dtype=np.float32)

    start = time.time()
    # Check equal is equal check is correct
    assert (cvMatIsEqual(mat_a, mat_b))
    end = time.time()
    duration = end - start
    assert duration < 0.1


def test_Utils_perf_disparity2depth():
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

    matcher = createStereoMatcher(stereo_params)
    match_result = matcher.compute(rect.left, rect.right)

    start = time.time()
    np_depth = disparity2depth(match_result.disparity, calibration.getQ())
    end = time.time()
    duration = end - start
    assert duration < 0.1


def test_Utils_perf_disparity2xyz():
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

    matcher = createStereoMatcher(stereo_params)
    match_result = matcher.compute(rect.left, rect.right)

    start = time.time()
    disparity_xyz = disparity2xyz(match_result.disparity, calibration.getQ())
    end = time.time()
    duration = end - start
    assert duration < 0.3


def test_Utils_perf_depth2xyz():
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

    matcher = createStereoMatcher(stereo_params)
    match_result = matcher.compute(rect.left, rect.right)

    np_depth = disparity2depth(match_result.disparity, calibration.getQ())

    start = time.time()
    xyz = depth2xyz(np_depth, calibration.getHFOV())
    end = time.time()
    duration = end - start
    assert duration < 0.5


def test_Utils_perf_xyz2depth():
    np_xyz = np.ones((2048, 2448, 3), dtype=np.float32)

    start = time.time()
    xyz_depth = xyz2depth(np_xyz)
    end = time.time()
    duration = end - start
    assert duration < 0.1


def test_Utils_perf_savePly():
    # Test performance of save point cloud
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

    # Create stereo image pair
    np_left_image = np.zeros((1080, 1920, 3), dtype=np.uint8)
    np_right_image = np.zeros((1080, 1920, 3), dtype=np.uint8)
    
    calibration = StereoCameraCalibration.calibrationFromYAML(
        left_yaml, right_yaml)
    

    stereo_params = StereoParams(
        StereoMatcherType.STEREO_MATCHER_BM,
        11, 0, 25, False
    )

    matcher = createStereoMatcher(stereo_params)
    
    match_result = matcher.compute(np_left_image, np_right_image)
    xyz = disparity2xyz(match_result.disparity, calibration.getQ())

    start = time.time()
    save_success = savePLY(out_ply, xyz, np_left_image)
    end = time.time()
    duration = end - start
    assert duration < 2

    assert (save_success)
