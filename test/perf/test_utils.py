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
import phase.pyphase as phase


def test_utils_perf_scaleImage_small():
    # Test image with size 640x480 scaled by ‘scaleImage’ function
    # with a scaling factor of 2 in less than 0.1s
    timeout = 0.1 #second
    img = np.ones((480, 640, 3), dtype=np.uint8)
    start = time.time()

    scaled_img = phase.scaleImage(img, 2.0)

    end = time.time()
    duration = end - start
    assert duration < timeout


def test_utils_perf_scaleImage_large():
    # Test image with size 2448x2048 scaled by ‘scaleImage’ function
    # with a scaling factor of 2 in less than 0.2s
    timeout = 0.2 #second
    img2 = np.ones((2048, 2448, 3), dtype=np.uint8)

    start = time.time()

    scaled_img = phase.scaleImage(img2, 2.0)

    end = time.time()
    duration = end - start
    assert duration < timeout


def test_utils_perf_toMono():
    # Test image of type CV_8UC3 converted to mono
    # by ‘toMono’ function in less than 0.1s
    timeout = 0.1 #second
    imgMono = np.zeros((2048, 2448, 1), dtype=np.uint8)
    img8UC3 = np.ones((2048, 2448, 3), dtype=np.uint8)

    start = time.time()
    assert phase.toMono(img8UC3, imgMono)
    end = time.time()
    duration = end - start
    assert duration < timeout


def test_utils_perf_bgra2rgba():
    # Test BGRA image converted to RGBA using ‘bgra2rgba’ function in less than 1.0s
    timeout = 1 #second
    img = np.zeros((2048, 2448, 4), dtype=np.uint8)

    start = time.time()
    converted_img = phase.bgra2rgba(img)
    end = time.time()
    duration = end - start
    assert duration < timeout


def test_utils_perf_bgr2rgba():
    # Test BGR image converted to RGBA using ‘bgr2rgba’ function in less than 1.0s
    timeout = 1 #second
    img = np.zeros((2048, 2448, 3), dtype=np.uint8)
    
    start = time.time()
    converted_img = phase.bgr2rgba(img)
    end = time.time()
    duration = end - start
    assert duration < timeout


def test_utils_perf_bgr2bgra():
    # Test BGR image converted to BGRA using ‘bgr2bgra’ function in less than 1.0s
    timeout = 1 #second
    img = np.zeros((2048, 2448, 3), dtype=np.uint8)

    start = time.time()
    converted_img = phase.bgr2bgra(img)
    end = time.time()
    duration = end - start
    assert duration < timeout


def test_utils_perf_disparity2depth():
    # Test disparity image of size 2448x2048 converted to depth
    # by ‘disparity2Depth’ function in less than 1.0s
    timeout = 1 #second
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(script_path, "..", "data")
    left_yaml = os.path.join(data_folder, "left.yaml")
    right_yaml = os.path.join(data_folder, "right.yaml")
    left_image_file = os.path.join(data_folder, "left.png")
    right_image_file = os.path.join(data_folder, "right.png")

    # Load test images
    left_image = phase.readImage(left_image_file)
    right_image = phase.readImage(right_image_file)

    # Load calibration
    calibration = phase.calib.StereoCameraCalibration.calibrationFromYAML(
        left_yaml, right_yaml)

    # Rectify images
    rect = calibration.rectify(left_image, right_image)
    # Compute disparity
    stereo_params = phase.stereomatcher.StereoParams(
        phase.stereomatcher.StereoMatcherType.STEREO_MATCHER_BM,
        11, 0, 25, False
    )

    matcher = phase.stereomatcher.createStereoMatcher(stereo_params)
    match_result = matcher.compute(rect.left, rect.right)

    start = time.time()
    np_depth = phase.disparity2depth(match_result.disparity, calibration.getQ())
    end = time.time()
    duration = end - start
    assert duration < timeout


def test_utils_perf_disparity2xyz():
    # Test disparity image of size 2448x2048 converted to xyz image
    # by ‘disparity2xyz’ function in less than 2.0s
    timeout = 2 #seconds
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(script_path, "..", "data")
    left_yaml = os.path.join(data_folder, "left.yaml")
    right_yaml = os.path.join(data_folder, "right.yaml")
    left_image_file = os.path.join(data_folder, "left.png")
    right_image_file = os.path.join(data_folder, "right.png")

    # Load test images
    left_image = phase.readImage(left_image_file)
    right_image = phase.readImage(right_image_file)

    # Load calibration
    calibration = phase.calib.StereoCameraCalibration.calibrationFromYAML(
        left_yaml, right_yaml)

    # Rectify images
    rect = calibration.rectify(left_image, right_image)
    # Compute disparity
    stereo_params = phase.stereomatcher.StereoParams(
        phase.stereomatcher.StereoMatcherType.STEREO_MATCHER_BM,
        11, 0, 25, False
    )

    matcher = phase.stereomatcher.createStereoMatcher(stereo_params)
    match_result = matcher.compute(rect.left, rect.right)

    start = time.time()
    disparity_xyz = phase.disparity2xyz(match_result.disparity, calibration.getQ())
    end = time.time()
    duration = end - start
    assert duration < timeout


def test_utils_perf_depth2xyz():
    # Test depth image of size 2448x2048 converted to xyz image
    # by ‘depth2xyz’ function in less than 1.0s
    timeout = 1 #second
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(script_path, "..", "data")
    left_yaml = os.path.join(data_folder, "left.yaml")
    right_yaml = os.path.join(data_folder, "right.yaml")
    left_image_file = os.path.join(data_folder, "left.png")
    right_image_file = os.path.join(data_folder, "right.png")

    # Load test images
    left_image = phase.readImage(left_image_file)
    right_image = phase.readImage(right_image_file)

    # Load calibration
    calibration = phase.calib.StereoCameraCalibration.calibrationFromYAML(
        left_yaml, right_yaml)

    # Rectify images
    rect = calibration.rectify(left_image, right_image)
    # Compute disparity
    stereo_params = phase.stereomatcher.StereoParams(
        phase.stereomatcher.StereoMatcherType.STEREO_MATCHER_BM,
        11, 0, 25, False
    )

    matcher = phase.stereomatcher.createStereoMatcher(stereo_params)
    match_result = matcher.compute(rect.left, rect.right)

    np_depth = phase.disparity2depth(match_result.disparity, calibration.getQ())

    start = time.time()
    xyz = phase.depth2xyz(np_depth, calibration.getHFOV())
    end = time.time()
    duration = end - start
    assert duration < timeout


def test_utils_perf_xyz2depth():
    # Test XYZ image of size 2448x2048 converted to depth image
    # by ‘xyz2depth’ function in less than 0.1s
    timeout = 0.1 #second
    np_xyz = np.ones((2048, 2448, 3), dtype=np.float32)

    start = time.time()
    xyz_depth = phase.xyz2depth(np_xyz)
    end = time.time()
    duration = end - start
    assert duration < timeout


def test_utils_perf_readImage():
    # Test read image of size 2448x2048 using ‘readImage’ function in less than 0.2s
    timeout = 0.2 #second
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(
        script_path, "..", "data")

    left_image_file = os.path.join(data_folder, "left.png")
    start = time.time()
    img = phase.readImage(left_image_file)
    end = time.time()
    duration = end - start
    assert duration < timeout
    
    
def test_utils_perf_flip():
    # Test flip image of size 2448x2048 horizontally using ‘flip’ function in less than 0.1s
    timeout = 0.1 #second
    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(
        script_path, "..", "data")
    image_file = os.path.join(data_folder, "left.png")
    img = phase.readImage(image_file)

    # Flip image
    start = time.time()
    flip_img0 = phase.flip(img, 0)
    end = time.time()
    duration = end - start
    assert duration < timeout


def test_utils_perf_savePly():
    # Test save RGB and XYZ image of size 2448x2048 as point cloud
    # in PLY format using ‘savePLY’ function in less than 5s
    timeout = 5 #seconds
    xyz1 = np.ones((2048, 2448, 3), dtype=float)
    rgb = np.ones((2048, 2448, 3), dtype=np.uint8)
    script_path = os.path.dirname(os.path.realpath(__file__))
    test_folder = os.path.join(script_path, "..", ".phase_test")
    out_ply = os.path.join(test_folder, "out.ply")

    start = time.time()
    save_success = phase.savePLY(out_ply, xyz1, rgb)
    end = time.time()
    duration = end - start
    assert duration < timeout

    assert (save_success)


def test_utils_perf_checkEqualMat():
    # Test performance of two matrices are equal
    # Create equal matrices
    timeout = 0.1 #second
    mat_a = np.ones((2048, 2448, 1), dtype=np.float32)
    mat_b = np.ones((2048, 2448, 1), dtype=np.float32)

    start = time.time()
    # Check equal is equal check is correct
    assert (phase.cvMatIsEqual(mat_a, mat_b))
    end = time.time()
    duration = end - start
    assert duration < timeout
