********
Examples
********

Read stereo images from camera
###################################

.. code-block:: python
   
    import cv2
    from phase.pyphase.types import CameraDeviceType, CameraInterfaceType
    from phase.pyphase.types import CameraDeviceInfo
    from phase.pyphase.stereocamera import createStereoCamera
    from phase.pyphase import scaleImage


    left_serial = "0815-0000"
    right_serial = "0815-0001"
    device_type = CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON  # DEVICE_TYPE_TITANIA / DEVICE_TYPE_PHOBOS
    interface_type = CameraInterfaceType.INTERFACE_TYPE_VIRTUAL  # INTERFACE_TYPE_USB / INTERFACE_TYPE_GIGE

    downsample_factor = 1.0
    display_downsample = 0.25
    capture_count = 20

    device_info = CameraDeviceInfo(
        left_serial, right_serial, "virtual-camera",
        device_type,
        interface_type
    )

    cam = createStereoCamera(device_info)

    print("Connecting to camera...")
    ret = cam.connect()
    if (ret):
        cam.startCapture()
        print("Running non-threaded camera capture...")
        for i in range(0, capture_count):
            read_result = cam.read()
            if (read_result.valid):
                print("Stereo result received")
                print("Framerate: {}".format(cam.getFrameRate()))
                if display_downsample != 1.0:
                    img_left = scaleImage(
                        read_result.left, display_downsample)
                    img_right = scaleImage(
                        read_result.right, display_downsample)
                else:
                    img_left = read_result.left
                    img_right = read_result.right
                cv2.imshow("left", img_left)
                cv2.imshow("right", img_right)
                cv2.waitKey(1)
            else:
                cam.disconnect()
                raise Exception("Failed to read stereo result")


Stereo match images from camera
######################################

.. code-block:: python
   
    import os
    import cv2
    from phase.pyphase.types import CameraDeviceType, CameraInterfaceType
    from phase.pyphase.types import CameraDeviceInfo, StereoMatcherType
    from phase.pyphase.stereocamera import createStereoCamera
    from phase.pyphase.calib import StereoCameraCalibration
    from phase.pyphase.stereomatcher import StereoParams, createStereoMatcher
    from phase.pyphase.stereomatcher import StereoI3DRSGM
    from phase.pyphase import scaleImage, normaliseDisparity, disparity2depth


    left_serial = "0815-0000"
    right_serial = "0815-0001"
    device_type = CameraDeviceType.DEVICE_TYPE_GENERIC_PYLON  # DEVICE_TYPE_TITANIA / DEVICE_TYPE_PHOBOS
    interface_type = CameraInterfaceType.INTERFACE_TYPE_VIRTUAL  # INTERFACE_TYPE_USB / INTERFACE_TYPE_GIGE

    downsample_factor = 1.0
    display_downsample = 0.25
    capture_count = 20

    device_info = CameraDeviceInfo(
        left_serial, right_serial, "virtual-camera",
        device_type,
        interface_type
    )

    script_path = os.path.dirname(os.path.realpath(__file__))
    data_folder = os.path.join(script_path, "..", "data")
    left_yaml = os.path.join(data_folder, "left.yaml")
    right_yaml = os.path.join(data_folder, "right.yaml")

    license_valid = StereoI3DRSGM().isLicenseValid()
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

    cam = createStereoCamera(device_info)
    calibration = StereoCameraCalibration.calibrationFromYAML(
        left_yaml, right_yaml)
    matcher = createStereoMatcher(stereo_params)

    print("Connecting to camera...")
    ret = cam.connect()
    if (ret):
        cam.startCapture()
        print("Running non-threaded camera capture...")
        for i in range(0, capture_count):
            read_result = cam.read()
            if (read_result.valid):
                print("Stereo result received")
                rect = calibration.rectify(read_result.left, read_result.right)
                print("Framerate: {}".format(cam.getFrameRate()))
                match_result = matcher.compute(rect.left, rect.right)
                depth = disparity2depth(match_result.disparity, calibration.getQ())
                if depth.size == 0:
                    print("Failed to convert disparity to depth")
                if display_downsample != 1.0:
                    img_left = scaleImage(
                        rect.left, display_downsample)
                    img_right = scaleImage(
                        rect.right, display_downsample)
                    img_disp = scaleImage(
                        normaliseDisparity(
                            match_result.disparity), display_downsample)
                else:
                    img_left = rect.left
                    img_right = rect.right
                    img_disp = normaliseDisparity(match_result.disparity)
                cv2.imshow("left", img_left)
                cv2.imshow("right", img_right)
                cv2.imshow("disparity", img_disp)
                cv2.waitKey(1)
            else:
                cam.disconnect()
                raise Exception("Failed to read stereo result")

Save / Load RGBD Video
######################

.. code-block:: python
   
    import os
    import cv2
    import numpy as np
    from phase.pyphase.types import MatrixUInt8, StereoMatcherType
    from phase.pyphase.calib import StereoCameraCalibration
    from phase.pyphase import processStereo, disparity2depth
    from phase.pyphase import RGBDVideoWriter, RGBDVideoStream
    from phase.pyphase.stereomatcher import StereoParams

    left_yaml = "left.yaml"
    right_yaml = "right.yaml"
    left_image_file = "left.png"
    right_image_file = "right.png"
    out_rgb_video = "rgb.mp4"
    out_depth_video = "depth.avi"
    num_of_frames = 1

    if not os.path.exists(out_folder):
        os.makedirs(out_folder)

    np_left_image = cv2.imread(left_image_file, cv2.IMREAD_UNCHANGED)
    np_right_image = cv2.imread(right_image_file, cv2.IMREAD_UNCHANGED)

    calibration = StereoCameraCalibration.calibrationFromYAML(
        left_yaml, right_yaml)

    rect_image_pair = calibration.rectify(np_left_image, np_right_image)

    ph_left_image = MatrixUInt8(rect_image_pair.left)
    ph_right_image = MatrixUInt8(rect_image_pair.right)

    stereo_params = StereoParams(
        StereoMatcherType.STEREO_MATCHER_BM,
        11, 0, 25, False
    )
    ph_disparity = processStereo(
        stereo_params,
        ph_left_image, ph_right_image, calibration, False
    )

    if ph_disparity.isEmpty():
        raise Exception("Failed to process stereo")

    np_disparity = np.array(ph_disparity)

    np_depth = disparity2depth(np_disparity, calibration.getQ())

    if np_depth.size == 0:
        raise Exception("Failed to convert disparity to depth")

    rgbdVideoWriter = RGBDVideoWriter(
        out_rgb_video, out_depth_video,
        ph_left_image.getColumns(), ph_left_image.getRows()
    )

    if not rgbdVideoWriter.isOpened():
        raise Exception("Failed to open RGBD video for writing")

    for i in range(0, num_of_frames):
        rgbdVideoWriter.add(rect_image_pair.left, np_depth)

    rgbdVideoWriter.saveThreaded()
    while(rgbdVideoWriter.isSaveThreadRunning()):
        pass

    if not rgbdVideoWriter.getSaveThreadResult():
        raise Exception("Error saving RGBD video")

    rgbdVideoStream = RGBDVideoStream(
        out_rgb_video, out_depth_video
    )

    if not rgbdVideoStream.isOpened():
        raise Exception("Failed to open RGBD video stream")

    rgbdVideoStream.loadThreaded()

    while(rgbdVideoStream.isLoadThreadRunning()):
        pass

    if not rgbdVideoStream.getLoadThreadResult():
        raise Exception("Failed to load RGBD video stream")

    while (not rgbdVideoStream.isFinished()):
        frame = rgbdVideoStream.read()

    rgbdVideoStream.close()