/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file stereocalibration_bindings.cpp
 * @brief Stereo Calibration class python bindings
 * @details Python bindings generated using pybind11
 */

#include "pybind11/pybind11.h"
#include "ndarray_converter.h"

#include <phase/calib/cameracalibration.h>

namespace py = pybind11;

void init_cameracalibration(py::module_ &m) {
    NDArrayConverter::init_numpy();
    // Determine the type of stereo calibration file
    py::enum_<I3DR::Phase::CalibrationFileType>(m, "CalibrationFileType", R"(
            Enum to indicate calibration file type. OpenCV uses different YAML standard from ROS.
            )")
        .value("ROS_YAML", I3DR::Phase::CalibrationFileType::ROS_YAML, R"(
            ROS YAML calibration file type (YAML v1.2 used by ROS)

            )")
        .value("OPENCV_YAML", I3DR::Phase::CalibrationFileType::OPENCV_YAML, R"(
            OpenCV YAML calibration file type (YAML v1.0 used by OpenCV)
            
            )")
        .value("INVALID_YAML", I3DR::Phase::CalibrationFileType::INVALID_YAML, R"(
               Invalid calibration file type
            )")
        .export_values();
    py::enum_<I3DR::Phase::CalibrationBoardType>(m, "CalibrationBoardType", R"(
            Enum to indicate calibration board type.
            )")
        .value("CHECKERBOARD", I3DR::Phase::CalibrationBoardType::CHECKERBOARD, R"(
            Checkerboard calibration board type

            )")
        .value("INVALID_BOARD", I3DR::Phase::CalibrationBoardType::INVALID_BOARD, R"(
            Invalid calibration board type

            )")
        .export_values();
    // Load in stereo camera calibration file
    py::class_<I3DR::Phase::CameraCalibration>(m, "CameraCalibration", R"(
            Store and manipulate mono camera calibration data.
            )")
        .def(py::init<const char*>(), R"(
            Initalise camera calibration from calibration file.

            Parameters
            ----------
            calibration_filepath : str
                Stereo calibration file path location
            )")
        .def(py::init<int, int, cv::Mat, cv::Mat, cv::Mat, cv::Mat>(), R"(
            Initalise camera calibration using the values provided.
            
            Parameters
            ----------
            width : int
                image width of camera
            height : int
                image height of camera
            camera_matrix : numpy.ndarray
                camera matrix of camera
            distortion_coefficients : numpy.ndarray
                distortion coefficients of camera
            rectification_matrix : numpy.ndarray
                rectification matrix of camera
            projection_matrix : numpy.ndarray
                projection matrix of camera
            )")
        .def_static("calibrationFromIdeal", &I3DR::Phase::CameraCalibration::calibrationFromIdeal, R"(
            Create ideal calibration from camera information
            
            Parameters
            ----------
            width : int
                image width of camera
            height : int
                image height of camera
            pixel_pitch : float
                pixel pitch of camera
            focal_length : float
                focal length of camera
            translation_x : float
                translation of principle point in X
            translation_y : float
                translation of principle point in Y
            )")
        .def("rectify", &I3DR::Phase::CameraCalibration::rectify, R"(
            Rectify image based on calibration

            Parameters
            ----------
            left_image : numpy.ndarray
                image to rectify
            right_image : numpy.ndarray
                image to store rectified image
            )")
        .def("isValid", &I3DR::Phase::CameraCalibration::isValid, R"(
            Check if loaded calibration is valid 

            Returns
            -------
            bool
                True if calibration is valid
        )")
        .def("setDownsampleFactor", &I3DR::Phase::CameraCalibration::setDownsampleFactor, R"(
            Set the downsample factor

            Parameters
            ----------
            value : float
            )")
        .def("getDownsampleFactor", &I3DR::Phase::CameraCalibration::getDownsampleFactor, R"(
            Get the downsample factor

            Returns
            -------
            value : float
                Value of downsample factor
            )")
        .def("getImageHeight", &I3DR::Phase::CameraCalibration::getImageHeight, R"(
            Get the image height from calibration

            Returns
            -------
            height : int
                Value of image height from calibration
            )")
        .def("getImageWidth", &I3DR::Phase::CameraCalibration::getImageWidth, R"(
            Get the image width from calibration

            Returns
            -------
            width : int
                Value of image width from calibration
            )")
        .def("getCameraMatrix", &I3DR::Phase::CameraCalibration::getCameraMatrix, R"(
            Get the camera matrix of calibration file

            Returns
            -------
            camera_matrix : numpy.ndarray                
                Camera matrix of calibration
            )")
        .def("getDistortionCoefficients", &I3DR::Phase::CameraCalibration::getDistortionCoefficients, R"(
            Get the distortion coefficients of calibration

            Returns
            -------
            distortion_coefficients : numpy.ndarray  
                Distortion coefficients of calibration
            )")
        .def("getRectificationMatrix", &I3DR::Phase::CameraCalibration::getRectificationMatrix, R"(
            Get the rectification matrix of calibration file

            Returns
            -------
            rectification_matrix : numpy.ndarray  
                Rectification matrix of calibration
            )")
        .def("getProjectionMatrix", &I3DR::Phase::CameraCalibration::getProjectionMatrix, R"(
            Get the projection matrix of calibration

            Returns
            -------
            projection_matrix : numpy.ndarray  
                Projection matrix of calibration
            )")
        .def("getCameraFX", &I3DR::Phase::CameraCalibration::getCameraFX, R"(
            Get camera focal length in X in calibration (in pixels)

            Returns
            -------
            cameraFX : float
                focal length in X
            )")
        .def("getCameraFY", &I3DR::Phase::CameraCalibration::getCameraFY, R"(
            Get camera focal length in Y in calibration (in pixels)

            Returns
            -------
            cameraFY : float
                focal length in Y
            )")
        .def("getCameraCX", &I3DR::Phase::CameraCalibration::getCameraCX, R"(
            Get camera principle point in X in calibration (in pixels)

            Returns
            -------
            cameraCX : float
                principle point in X
            )")
        .def("getCameraCY", &I3DR::Phase::CameraCalibration::getCameraCY, R"(
            Get camera principle point in Y in calibration (in pixels)

            Returns
            -------
            cameraCY : float
                principle point in Y
            )")
        .def("getProjectionFX", &I3DR::Phase::CameraCalibration::getProjectionFX, R"(
            Get camera focal length in X in calibration projection (in pixels)

            Returns
            -------
            projectionFX : float
                focal length in X
            )")
        .def("getProjectionFY", &I3DR::Phase::CameraCalibration::getProjectionFY, R"(
            Get camera focal length in Y in calibration projection (in pixels)

            Returns
            -------
            projectionFY : float
                focal length in Y
            )")
        .def("getProjectionCX", &I3DR::Phase::CameraCalibration::getProjectionCX, R"(
            Get camera principle point in X in calibration projection (in pixels)

            Returns
            -------
            projectionCX : float
                principle point in X
            )")
        .def("getProjectionCY", &I3DR::Phase::CameraCalibration::getProjectionCY, R"(
            Get camera principle point in Y in calibration projection (in pixels)

            Returns
            -------
            projectionCY : float
                principle point in Y
            )")
        .def("getProjectionTX", &I3DR::Phase::CameraCalibration::getProjectionTX, R"(
            Get camera baseline in calibration projection (in pixels)

            Returns
            -------
            projectionTX : float
                baseline
            )");
}