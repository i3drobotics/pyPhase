#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2022-09-06
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file demo_match_thread.py
 @brief Example application using pyPhase to compute disparity from stereo camera in thread
"""
import os
import datetime
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
capture_count = 20

# Create stereo camera device information from parameters
device_info = phase.stereocamera.CameraDeviceInfo(
    left_serial, right_serial, "virtual-camera",
    device_type,
    interface_type
)

# Create stereo camera
cam = phase.stereocamera.createStereoCamera(device_info)

# Define calibration files
script_path = os.path.dirname(os.path.realpath(__file__))
data_folder = os.path.join(script_path, "..", "data")
left_yaml = os.path.join(data_folder, "left.yaml")
right_yaml = os.path.join(data_folder, "right.yaml")

# Check for I3DRSGM license
i3drsgm = phase.stereomatcher.StereoI3DRSGM()
license_valid = i3drsgm.isLicenseValid()
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
    for i in range(0, capture_count):
        if (read_result.valid):
            print("Stereo result received")
            # Rectify stereo image pair
            rect = calibration.rectify(read_result.left, read_result.right)
            print("Running threaded stereo matcher...")
            # Start compute threaded stereo matcher
            matcher.startComputeThread(rect.left, rect.right)
            start = datetime.datetime.now()
            capture_count = cam.getCaptureCount()
            frame_rate = cam.getFrameRate()
            print("Count {}".format(capture_count))
            print("Internal framerate {}".format(frame_rate))
            while matcher.isComputeThreadRunning():
                # check stereo matching is not taking too long, else stop thread
                end = datetime.datetime.now()
                duration = (end - start).total_seconds()      
                
                if duration > timeout:
                    break
                if capture_count > capture_count:
                    break
            
            # Get the result of threaded stereo matcher
            match_result = matcher.getComputeThreadResult()

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
            if c == ord('q'):
                break

    # Once finished, stop to read thread
    cam.disconnect()
