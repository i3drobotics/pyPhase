import cv2
import os
from phase.pyphase.stereocamera import CameraDeviceInfo, TitaniaStereoCamera
from phase.pyphase.stereocamera import CameraDeviceType, CameraInterfaceType
from phase.pyphase.calib import StereoCameraCalibration
from phase.pyphase.stereomatcher import StereoMatcherType
from phase.pyphase.stereomatcher import StereoI3DRSGM, StereoParams
from phase.pyphase.stereomatcher import createStereoMatcher
from phase.pyphase import scaleImage, normaliseDisparity
from phase.pyphase import disparity2xyz, savePLY


# Define camera info
# Replace camera_name, left_serial & right serial
# with unique camera serials
camera_name = "746974616e24322"#"746974616e24317"
left_serial = "40136578"#"40098272"
right_serial = "40098277"#"40098282"
device_type = CameraDeviceType.DEVICE_TYPE_TITANIA
interface_type = CameraInterfaceType.INTERFACE_TYPE_USB

script_path = os.path.dirname(os.path.realpath(__file__))

# Define calibration file
# Calibrate through Vision Stereo toolkit
test_folder = os.path.join(script_path, "..", ".phase_test")
data_folder = os.path.join(script_path, "..", "data")
left_yaml = os.path.join(data_folder, "titania_left.yaml")
right_yaml = os.path.join(data_folder, "titania_right.yaml")
out_ply = os.path.join(test_folder, "titania_out.ply")

# Parameters for read and display 20 frames
downsample_factor = 1.0
display_downsample = 0.25
capture_count = 20
exposure_value = 10000

# Check for license
i3drsgm = StereoI3DRSGM()
license_valid = i3drsgm.isLicenseValid()
if license_valid:
    print("I3DRSGM license accepted")
else:
    print("Missing or invalid I3DRSGM license")

    # Check for I3DRSGM license
if license_valid:
    stereo_params = StereoParams(
        StereoMatcherType.STEREO_MATCHER_I3DRSGM,
        9, 0, 49, False
    )
else:
    stereo_params = StereoParams(
        StereoMatcherType.STEREO_MATCHER_BM,
        11, 0, 25, False
    )
# Load calibration
calibration = StereoCameraCalibration.calibrationFromYAML(
    left_yaml, right_yaml)

# Create stereo matcher
matcher = createStereoMatcher(stereo_params)

# Define titania info from connection
device_info = CameraDeviceInfo(
    left_serial, right_serial, camera_name,
    device_type,
    interface_type)
tinaniaCam = TitaniaStereoCamera(device_info)

# Connect Titania
ret = tinaniaCam.connect()
if (ret):
    # If Titania is connected, start capture
    tinaniaCam.startCapture()
    # Set new exposure value
    tinaniaCam.setExposure(exposure_value)
    while True:
        if (not tinaniaCam.isConnected()):
            break
        read_result = tinaniaCam.read()

        if read_result.valid:
            # Rectify stereo image pair
            rect_image_pair = calibration.rectify(read_result.left, read_result.right)
            rect_img_left = rect_image_pair.left
            rect_img_right = rect_image_pair.right

            match_result = matcher.compute(rect_img_left, rect_img_right)

            if not match_result.valid:
                print("Failed to process stereo")
                continue

            # Find the disparity from matcher
            disparity = match_result.disparity

            # Convert disparity into 3D pointcloud
            xyz = disparity2xyz(
                disparity, calibration.getQ())

            # Display left, right and disparity image with downsample option
            if display_downsample != 1.0:
                img_left = scaleImage(
                        rect_img_left, display_downsample)
                img_right = scaleImage(
                        rect_img_right, display_downsample)
                img_disp = scaleImage(
                        normaliseDisparity(
                            disparity), display_downsample)

            else:
                img_left = rect_img_left
                img_right = rect_img_right
                img_disp = normaliseDisparity(disparity)
              
            cv2.imshow("Left", img_left)
            cv2.imshow("Right", img_right)
            cv2.imshow("Disparity", img_disp)
            c = cv2.waitKey(1)

            # If p key is pressed, save the pointcloud of current frame
            if c == ord('p'):
                save_success = savePLY(out_ply, xyz, rect_img_left)
                if save_success:
                    print("Pointcloud saved to " + out_ply)
                else:
                    print("Unable to save pointcloud")
            
            #if q key is pressed, quit Titania capture
            if c == ord('q'):
                break
        else:
            tinaniaCam.disconnect()
            raise Exception("Failed to read stereo result")
            
cv2.destroyAllWindows()