********
Examples
********

Read and process stereo camera data
###################################

.. code-block:: python
   
    import cv2
    from phase.core import StereoVision
    from phase.core.types import CameraDeviceType, CameraInterfaceType
    from phase.core.types import CameraDeviceInfo, StereoMatcherType
    from phase.core.stereomatcher import StereoI3DRSGM
    from phase.core import scaleImage, normaliseDisparity

    i3drsgm = StereoI3DRSGM()
    license_valid = i3drsgm.isLicenseValid()
    if license_valid:
        print("I3DRSGM license accepted")
    else:
        print("Missing or invalid I3DRSGM license")

    # Define camera info
    camera_name = "titania"
    left_serial = "40091829"
    right_serial = "40098273"
    device_type = CameraDeviceType.DEVICE_TYPE_TITANIA
    interface_type = CameraInterfaceType.INTERFACE_TYPE_USB

    # Define calibration files
    left_yaml = "left.yaml"
    right_yaml = "right.yaml"

    downsample_factor = 1.0
    display_downsample = 0.25
    capture_count = 5

    device_info = CameraDeviceInfo(
        left_serial, right_serial, camera_name,
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

    sv.setDownsampleFactor(downsample_factor)
    matcher = sv.getMatcher()
    matcher.setWindowSize(3)
    if matcher_type == StereoMatcherType.STEREO_MATCHER_I3DRSGM:
        # matcher.setMinDisparity(0)
        matcher.setNumDisparities(49)
        matcher.setSpeckleMaxSize(1000)
        matcher.setSpeckleMaxDiff(0.5)
        # matcher.enableInterpolation(True)

    print("Connecting to camera...")
    ret = sv.connect()
    print("Camera connected: {}".format(ret))
    if (ret):
        print("Running non-threaded camera capture...")
        for i in range(0, capture_count):
            read_result = sv.read()
            if (read_result.valid):
                print("Stereo result received")
                print("Framerate: {}".format(sv.getCamera().getFrameRate()))
                if display_downsample != 1.0:
                    img_left = scaleImage(
                        read_result.left_image, display_downsample)
                    img_right = scaleImage(
                        read_result.right_image, display_downsample)
                    img_disp = scaleImage(
                        normaliseDisparity(
                            read_result.disparity), display_downsample)
                else:
                    img_left = read_result.left_image
                    img_right = read_result.right_image
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
                    cam_result.left_image,
                    cam_result.right_image)
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
                            cam_result.left_image,
                            cam_result.right_image)
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
                    img_left = scaleImage(result.left_image, display_downsample)
                    img_right = scaleImage(result.right_image, display_downsample)
                    img_disp = scaleImage(
                        normaliseDisparity(result.disparity), display_downsample)
                else:
                    img_left = result.left_image
                    img_right = result.right_image
                    img_disp = normaliseDisparity(matcher_result.disparity)
                cv2.imshow("left", img_left)
                cv2.imshow("right", img_right)
                cv2.imshow("disparity", img_disp)
                cv2.waitKey(1)
            else:
                sv.disconnect()
                raise Exception("Failed to read stereo result")
        sv.disconnect()
        print("Camera disconnected")

Read and process stereo data from file
######################################

.. code-block:: python
   
    import cv2
    import numpy as np
    from phase.core.types import CameraDeviceType, CameraInterfaceType
    from phase.core.types import StereoMatcherType, MatrixUInt8
    from phase.core.stereomatcher import StereoI3DRSGM, StereoParams
    from phase.core.calib import StereoCameraCalibration
    from phase.core import processStereo, disparity2depth

    license_valid = StereoI3DRSGM().isLicenseValid()
    if license_valid:
        print("I3DRSGM license accepted")
    else:
        print("Missing or invalid I3DRSGM license")

    # Define calibration files
    left_yaml = "left.yaml"
    right_yaml = "right.yaml"

    # Define stereo image pair
    left_image_file = "left.png"
    right_image_file = "right.png"

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

    # Read stereo image pair
    np_left_image = cv2.imread(left_image_file, cv2.IMREAD_UNCHANGED)
    np_right_image = cv2.imread(right_image_file, cv2.IMREAD_UNCHANGED)

    # Convert numpy to Mat images
    left_image = MatrixUInt8(np_left_image)
    right_image = MatrixUInt8(np_right_image)

    # Load calibration
    calibration = StereoCameraCalibration.calibrationFromYAML(
        left_yaml, right_yaml)

    # Process stereo
    disparity = processStereo(
        stereo_params, left_image, right_image, calibration
    )
    if disparity.isEmpty():
        raise Exception("Failed to process stereo")

    # Convert disparity to depth
    np_disparity = np.array(disparity)
    np_depth = disparity2depth(np_disparity, calibration.getQ())
    if np_depth.size == 0:
        raise Exception("Failed to convert disparity to depth")

Convert between Mat and numpy
#############################

.. code-block:: python

    import cv2
    import numpy as np
    from phase.core.types import MatrixUInt8, StereoMatcherType
    from phase.core import processStereo

    np_image = cv2.imread("image.png", cv2.IMREAD_UNCHANGED)
    mat_left_image = MatrixUInt8(np_image)
    np_image2 = np.array(mat_left_image)

Save / Load RGBD Video
######################

.. code-block:: python
   
    import os
    import cv2
    import numpy as np
    from phase.core.types import MatrixUInt8, StereoMatcherType
    from phase.core.calib import StereoCameraCalibration
    from phase.core import processStereo, disparity2depth
    from phase.core import RGBDVideoWriter, RGBDVideoStream
    from phase.core.stereomatcher import StereoParams

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