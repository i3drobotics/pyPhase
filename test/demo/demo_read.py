#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2022-09-06
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file demo_read.py
 @brief Example application using pyPhase to read camera data
"""
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
capture_count = 20

# Create stereo camera device information from parameters
device_info = phase.stereocamera.CameraDeviceInfo(
    left_serial, right_serial, "virtual-camera",
    device_type,
    interface_type
)

# Create stereo camera
cam = phase.stereocamera.createStereoCamera(device_info)

# Connect camera and start data capture
print("Connecting to camera...")
ret = cam.connect()
if (ret):
    cam.startCapture()
    print("Running camera capture...")
    for i in range(0, capture_count):
        # Read frame from camera
        read_result = cam.read()
        if (read_result.valid):
            print("Stereo frame received")
            print("Framerate: {}".format(cam.getFrameRate()))

            # Display stereo images
            img_left = phase.scaleImage(
                read_result.left, display_downsample)
            img_right = phase.scaleImage(
                read_result.right, display_downsample)
            cv2.imshow("left", img_left)
            cv2.imshow("right", img_right)
            c = cv2.waitKey(1)
            # Quit data capture if 'q' is pressed
            if c == ord('q'):
                break
        else:
            cam.disconnect()
            raise Exception("Failed to read stereo result")
