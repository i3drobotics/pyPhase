********
Examples
********

Read stereo camera data
#######################

.. code-block:: python
   
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


Compute disparity from stereo camera
####################################

.. code-block:: python
   
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
        for i in range(0, capture_count):
            read_result = cam.read()
            if (read_result.valid):
                print("Stereo result received")
                # Rectify stereo image pair
                rect = calibration.rectify(read_result.left, read_result.right)
                # Compute stereo match
                match_result = matcher.compute(rect.left, rect.right)

                # Check compute is valid
                if not match_result.valid:
                    print("Failed to compute match")
                    continue

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
            else:
                cam.disconnect()
                raise Exception("Failed to read stereo result")


Read data from Titania camera and generate 3D
#############################################

.. code-block:: python
   
    import cv2
    import os
    import phase.pyphase as phase


    # Define information about the Titania camera
    # Each camera has unique camera_name, left_serial, and right_serial
    camera_name = "746974616e24317"
    left_serial = "40098272"
    right_serial = "40098282"
    device_type = phase.stereocamera.CameraDeviceType.DEVICE_TYPE_TITANIA
    interface_type = phase.stereocamera.CameraInterfaceType.INTERFACE_TYPE_USB

    script_path = os.path.dirname(os.path.realpath(__file__))

    # Define calibration files
    test_folder = os.path.join(script_path, "..", ".phase_test")
    data_folder = os.path.join(script_path, "..", "data")
    left_yaml = os.path.join(data_folder, "titania_left.yaml")
    right_yaml = os.path.join(data_folder, "titania_right.yaml")
    out_ply = os.path.join(test_folder, "titania_out.ply")

    # Define parameters for read process
    downsample_factor = 1.0
    display_downsample = 0.25
    exposure_value = 10000

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

    # Create stereo camera device information from parameters
    device_info = phase.stereocamera.CameraDeviceInfo(
        left_serial, right_serial, camera_name,
        device_type,
        interface_type)
    # Create stereo camera
    tinaniaCam = phase.stereocamera.TitaniaStereoCamera(device_info)

    # Connect camera and start data capture
    print("Connecting to camera...")
    ret = tinaniaCam.connect()
    if (ret):
        tinaniaCam.startCapture()
        # Set camera exposure value
        tinaniaCam.setExposure(exposure_value)
        print("Running camera capture...")
        while not tinaniaCam.isConnected():
            read_result = tinaniaCam.read()
            if read_result.valid:
                # Rectify stereo image pair
                rect_image_pair = calibration.rectify(read_result.left, read_result.right)
                rect_img_left = rect_image_pair.left
                rect_img_right = rect_image_pair.right

                match_result = matcher.compute(rect_img_left, rect_img_right)

                # Check compute is valid
                if not match_result.valid:
                    print("Failed to compute match")
                    continue

                # Find the disparity from matcher
                disparity = match_result.disparity

                # Convert disparity into 3D pointcloud
                xyz = phase.disparity2xyz(
                    disparity, calibration.getQ())

                # Display stereo and disparity images
                img_left = phase.scaleImage(
                        rect_img_left, display_downsample)
                img_right = phase.scaleImage(
                        rect_img_right, display_downsample)
                img_disp = phase.scaleImage(
                        phase.normaliseDisparity(
                            disparity), display_downsample)
                cv2.imshow("Left", img_left)
                cv2.imshow("Right", img_right)
                cv2.imshow("Disparity", img_disp)
                c = cv2.waitKey(1)

                # Save the pointcloud of current frame if 'p' is pressed
                if c == ord('p'):
                    save_success = phase.savePLY(out_ply, xyz, rect_img_left)
                    if save_success:
                        print("Pointcloud saved to " + out_ply)
                    else:
                        print("Failed to save pointcloud")
                
                # Quit data capture if 'q' is pressed
                if c == ord('q'):
                    break
            else:
                tinaniaCam.disconnect()
                raise Exception("Failed to read stereo result")
                
    cv2.destroyAllWindows()


Generate point cloud from stereo camera
#######################################

.. code-block:: python

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


Generate calibration from images
################################

.. code-block:: python

    import os
    import phase.pyphase as phase


    # Define data paths
    script_path = os.path.dirname(os.path.realpath(__file__))
    test_folder = os.path.join(script_path, "..", ".phase_test")
    data_folder = os.path.join(
        script_path, "..", "data", "checker_sample")
    left_cal_folder = data_folder
    right_cal_folder = data_folder
    output_folder = os.path.join(test_folder, "cal")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Define calibration files
    left_yaml = os.path.join(output_folder, "left.yaml")
    right_yaml = os.path.join(output_folder, "right.yaml")
    left_img_wildcard = "*_l.png"
    right_img_wildcard = "*_r.png"
    image_type = phase.calib.CalibrationBoardType.CHECKERBOARD

    # Load calibration from images
    cal = phase.calib.StereoCameraCalibration.calibrationFromImages(
        left_cal_folder, right_cal_folder,
        left_img_wildcard, right_img_wildcard,
        image_type, 10, 6, 0.039)

    if not cal.isValid():
        print("Calibration is invalid")

    # Save calibration to YAML
    save_success = cal.saveToYAML(
        left_yaml, right_yaml,
        phase.calib.CalibrationFileType.ROS_YAML)
    if not save_success:
        print("Failed to save calibration to YAML")


Read stereo camera data in thread
#################################

.. code-block:: python

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


Compute disparity from stereo camera in thread
##############################################

.. code-block:: python

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
