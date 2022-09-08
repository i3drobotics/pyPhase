#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2022-09-06
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file demo_generate_pointcloud.py
 @brief Example application using pyPhase to generate point cloud
"""
import os
import cv2
import phase.pyphase as phase


# Define information about the virtual camera
left_serial = "0815-0000"
right_serial = "0815-0001"
device_type = phase.stereocamera.CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON
interface_type = phase.stereocamera.CameraInterfaceType.INTERFACE_TYPE_VIRTUAL

# Define parameters for process
downsample_factor = 1.0
display_downsample = 0.25

# Create stereo camera device information from parameters
device_info = phase.stereocamera.CameraDeviceInfo(
    left_serial, right_serial, "virtual-camera",
    device_type,
    interface_type
)

# Create stereo camera
cam = phase.stereocamera.createStereoCamera(device_info)

# Define calibration files and save pointcloud path
script_path = os.path.dirname(os.path.realpath(__file__))
test_folder = os.path.join(script_path, "..", ".phase_test")
data_folder = os.path.join(script_path, "..", "data")
left_yaml = os.path.join(data_folder, "left.yaml")
right_yaml = os.path.join(data_folder, "right.yaml")
out_ply = os.path.join(test_folder, "out.ply")

# Define calibration files
script_path = os.path.dirname(os.path.realpath(__file__))
data_folder = os.path.join(script_path, "..", "data")
left_yaml = os.path.join(data_folder, "left.yaml")
right_yaml = os.path.join(data_folder, "right.yaml")

# Check for I3DRSGM license
license_valid = phase.stereomatcher.StereoI3DRSGM().isLicenseValid()
if license_valid:
    print("I3DRSGM license accepted")
    stereo_params = phase.stereomatcher.StereoParams(
        phase.stereomatcher.StereoMatcherType.STEREO_MATCHER_I3DRSGM,
        9, 0, 49, False
    )
else:
    print("Missing or invalid I3DRSGM license. Will use StereoBM")
    stereo_params = phase.stereomatcher.StereoParams(
        phase.stereomatcher.StereoMatcherType.STEREO_MATCHER_BM,
        11, 0, 25, False
    )

# Load calibration
calibration = phase.calib.StereoCameraCalibration.calibrationFromYAML(
    left_yaml, right_yaml)

# Create stereo matcher
matcher = phase.stereomatcher.createStereoMatcher(stereo_params)

# Connect camera and start data capture
print("Connecting to camera...")
ret = cam.connect()
if (ret):
    cam.startCapture()
    print("Running camera capture...")
    read_result = cam.read()
    if (read_result.valid):
        print("Stereo result received")
        rect = calibration.rectify(read_result.left, read_result.right)
        match_result = matcher.compute(rect.left, rect.right)
        # Convert disparity to 3D xyz pointcloud
        xyz = phase.disparity2xyz(
            match_result.disparity, calibration.getQ())

        # Display stereo and disparity images
        img_left = phase.scaleImage(
            rect.left, display_downsample)
        img_right = phase.scaleImage(
            rect.right, display_downsample)
        img_disp = phase.scaleImage(
            phase.normaliseDisparity(
                match_result.disparity), display_downsample)
        cv2.imshow("left", img_left)
        cv2.imshow("right", img_right)
        cv2.imshow("disparity", img_disp)
        c = cv2.waitKey(1)

        # Save the pointcloud
        save_success = phase.savePLY(out_ply, xyz, rect.left)
        if save_success:
            print("Pointcloud saved to " + out_ply)
        
    else:
        cam.disconnect()
        raise Exception("Failed to read stereo result")
