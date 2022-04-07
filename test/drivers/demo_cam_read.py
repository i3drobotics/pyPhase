#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file demo_cam_read.py
 @brief Example application using pyPhase
"""
import os
import cv2
from phase.pyphase import StereoVision
from phase.pyphase.types import CameraDeviceType, CameraInterfaceType
from phase.pyphase.types import CameraDeviceInfo, StereoMatcherType
from phase.pyphase.stereomatcher import StereoI3DRSGM
from phase.pyphase import scaleImage, normaliseDisparity


i3drsgm = StereoI3DRSGM()
license_valid = i3drsgm.isLicenseValid()
if license_valid:
    print("I3DRSGM license accepted")
else:
    print("Missing or invalid I3DRSGM license")

script_path = os.path.dirname(os.path.realpath(__file__))
data_folder = os.path.join(script_path, "..", "data")
left_yaml = os.path.join(data_folder, "left.yaml")
right_yaml = os.path.join(data_folder, "right.yaml")
left_image_file = os.path.join(data_folder, "left.png")
right_image_file = os.path.join(data_folder, "right.png")
left_serial = "0815-0000"
right_serial = "0815-0001"
device_type = CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON
interface_type = CameraInterfaceType.INTERFACE_TYPE_VIRTUAL

downsample_factor = 1.0
display_downsample = 0.25
use_test_image = True
capture_count = 1

device_info = CameraDeviceInfo(
    left_serial, right_serial, "virtual-camera",
    device_type,
    interface_type
)

if license_valid:
    matcher_type = StereoMatcherType.STEREO_MATCHER_I3DRSGM
else:
    matcher_type = StereoMatcherType.STEREO_MATCHER_BM

sv = StereoVision(
    device_info, matcher_type, left_yaml, right_yaml
)
if (not sv.getCalibration().isValid()):
    raise Exception("Failed to load calibration")

print("StereoVision instance created")
if use_test_image:
    sv.setTestImagePaths(left_image_file, right_image_file)

sv.setDownsampleFactor(downsample_factor)
matcher = sv.getMatcher()
if matcher_type == StereoMatcherType.STEREO_MATCHER_I3DRSGM:
    matcher.setWindowSize(3)
    # matcher.setMinDisparity(0)
    matcher.setNumDisparities(49)
    matcher.setSpeckleMaxSize(1000)
    matcher.setSpeckleMaxDiff(0.5)
    # matcher.enableInterpolation(True)
if matcher_type == StereoMatcherType.STEREO_MATCHER_BM:
    matcher.setWindowSize(3)
    matcher.setMinDisparity(0)
    matcher.setNumDisparities(10)

print("Connecting to camera...")
ret = sv.connect()
print("Camera connected: {}".format(ret))
if (ret):
    sv.startCapture()
    print("Running non-threaded camera capture...")
    for i in range(0, capture_count):
        read_result = sv.read()
        if (read_result.valid):
            print("Stereo result received")
            print("Framerate: {}".format(sv.getCamera().getFrameRate()))
            if display_downsample != 1.0:
                img_left = scaleImage(
                    read_result.left, display_downsample)
                img_right = scaleImage(
                    read_result.right, display_downsample)
                img_disp = scaleImage(
                    normaliseDisparity(
                        read_result.disparity), display_downsample)
            else:
                img_left = read_result.left
                img_right = read_result.right
                img_disp = normaliseDisparity(read_result.disparity)
            cv2.imshow("left", img_left)
            cv2.imshow("right", img_right)
            cv2.imshow("disparity", img_disp)
            cv2.waitKey(1)
        else:
            sv.disconnect()
            raise Exception("Failed to read stereo result")

    print("Running split threaded camera capture...")
    cam = sv.getCamera()
    matcher = sv.getMatcher()
    for i in range(0, capture_count):
        print("Starting read thread...")
        cam.startReadThread()
        print("Waiting for result...")
        while(cam.isReadThreadRunning()):
            pass
        print("Processing read result...")
        cam_result = cam.getReadThreadResult()
        if (cam_result.valid):
            print("Read result received")
            image_pair = sv.getCalibration().rectify(
                cam_result.left,
                cam_result.right)
            print("Starting compute thread...")
            matcher.startComputeThread(
                image_pair.left, image_pair.right)
            print("Framerate: {}".format(cam.getFrameRate()))
            if display_downsample != 1.0:
                img_left = scaleImage(image_pair.left, display_downsample)
                img_right = scaleImage(image_pair.right, display_downsample)
            else:
                img_left = image_pair.left
                img_right = image_pair.right
            cv2.imshow("left", img_left)
            cv2.imshow("right", img_right)
            cv2.waitKey(1)
            print("Waiting for compute result...")
            while(matcher.isComputeThreadRunning()):
                # continue camera capture while waiting for compute result
                print("Starting read thread...")
                cam.startReadThread()
                print("Waiting for read result...")
                while(cam.isReadThreadRunning()):
                    pass
                print("Processing read result...")
                cam_result = cam.getReadThreadResult()
                if (cam_result.valid):
                    print("Rectifing read result...")
                    image_pair = sv.getCalibration().rectify(
                        cam_result.left,
                        cam_result.right)
                    print("Displaying read result...")
                    if display_downsample != 1.0:
                        img_left = scaleImage(
                            image_pair.left, display_downsample)
                        img_right = scaleImage(
                            image_pair.right, display_downsample)
                    else:
                        img_left = image_pair.left
                        img_right = image_pair.right
                    cv2.imshow("left", img_left)
                    cv2.imshow("right", img_right)
                    cv2.waitKey(1)
            matcher_result = matcher.getComputeThreadResult()
            if (matcher_result.valid):
                print("Compute result received")
                if display_downsample != 1.0:
                    img_disp = scaleImage(
                        normaliseDisparity(
                            matcher_result.disparity), display_downsample)
                else:
                    img_disp = normaliseDisparity(matcher_result.disparity)
                cv2.imshow("disparity", img_disp)
                cv2.waitKey(1)
        else:
            sv.disconnect()
            raise Exception("Failed to read stereo result")

    print("Running threaded camera capture...")
    for i in range(0, capture_count):
        sv.startReadThread()
        print("Waiting for result...")
        while(sv.isReadThreadRunning()):
            pass
        result = sv.getReadThreadResult()
        if (result.valid):
            print("Stereo result received")
            print("Framerate: {}".format(sv.getCamera().getFrameRate()))
            if display_downsample != 1.0:
                img_left = scaleImage(result.left, display_downsample)
                img_right = scaleImage(result.right, display_downsample)
                img_disp = scaleImage(
                    normaliseDisparity(result.disparity), display_downsample)
            else:
                img_left = result.left
                img_right = result.right
                img_disp = normaliseDisparity(result.disparity)
            cv2.imshow("left", img_left)
            cv2.imshow("right", img_right)
            cv2.imshow("disparity", img_disp)
            cv2.waitKey(1)
        else:
            sv.disconnect()
            raise Exception("Failed to read stereo result")
    sv.disconnect()
    print("Camera disconnected")
