#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2022-09-06
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file demo_read_thread.py
 @brief Example application using pyPhase to read camera data in thread
"""
import time
import datetime
import cv2
import phase.pyphase as phase


# Define information about the virtual camera
left_serial = "0815-0000"
right_serial = "0815-0001"
device_type = phase.stereocamera.CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON
interface_type = phase.stereocamera.CameraInterfaceType.INTERFACE_TYPE_VIRTUAL

# Define parameters for read process
downsample_factor = 1.0
display_downsample = 0.25
frames = 20
timeout = 30
waitkey_delay = 1

# Create stereo camera device information from parameters
device_info = phase.stereocamera.CameraDeviceInfo(
    left_serial, right_serial, "virtual-camera",
    device_type,
    interface_type
)

# Create stereo camera
cam = phase.stereocamera.createStereoCamera(device_info)

# Callback funtion to run when a frame is read from the camera
def read_callback(read_result: phase.stereocamera.CameraReadResult):
    # Display stereo and disparity images
    if read_result.valid:
        print("Stereo result received")
        disp_image_left = phase.scaleImage(read_result.left, 0.25)
        disp_image_right = phase.scaleImage(read_result.right, 0.25)
        cv2.imshow("left", disp_image_left)
        cv2.imshow("right", disp_image_right)
        cv2.waitKey(waitkey_delay)
    else:
        print("Failed to read stereo result")

# Set the callback function to call on new frame
cam.setReadThreadCallback(read_callback)

# Connect camera and start data capture
print("Connecting to camera...")
ret = cam.connect()
if (ret):
    cam.startCapture()
    print("Running threaded camera capture...")
    cam.startContinousReadThread()
    start = datetime.datetime.now()
    capture_count = cam.getCaptureCount()
    while capture_count < frames:
        capture_count = cam.getCaptureCount()
        frame_rate = cam.getFrameRate()
        print("Count {}".format(capture_count))
        print("Internal framerate {}".format(frame_rate))
        end = datetime.datetime.now()
        duration = (end - start).total_seconds()
        # Stop if thread reading is too long
        if duration > timeout:
            break
        time.sleep(1)
    cam.stopContinousReadThread()
    cam.disconnect()
