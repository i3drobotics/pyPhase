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
            Check the format of calibration files
            )")
        .value("ROS_YAML", I3DR::Phase::CalibrationFileType::ROS_YAML, R"(
            Format of ROS stereo calibration yaml

            )")
        .value("OPENCV_YAML", I3DR::Phase::CalibrationFileType::OPENCV_YAML, R"(
            Format of OpenCV stereo calibration yaml
            
            )")
        .value("INVALID", I3DR::Phase::CalibrationFileType::INVALID, R"(
               Invalid stereo calibration format 
            )")
        .export_values();
    // Load in stereo camera calibration file
    py::class_<I3DR::Phase::CameraCalibration>(m, "CameraCalibration", R"(
            Variables of stereo camera calibration file
            )")
        .def(py::init<const char*>(), R"(
            Get stereo camera calibration file location

            Parameters
            ----------
            calibration_filepath : str
                Stereo calibration file path location
            )")
        .def(py::init<int, int, cv::Mat, cv::Mat, cv::Mat, cv::Mat>(), R"(
            Load calibration file detail
            
            Parameters
            ----------
            width : int
                Image width of calibration file
            height : int
                Image height of calibration file
            camera_matrix : numpy.ndarray
                Camera Matrix of calibration file
            distortion_coefficients : numpy.ndarray
                Distortion coefficients of calibration file
            rectification_matrix : numpy.ndarray
                Rectification matrix of calibration file
            projection_matrix : numpy.ndarray
                Projection Matrix of calibration file
            )")
        .def_static("calibrationFromIdeal", &I3DR::Phase::CameraCalibration::calibrationFromIdeal, R"(
            Load calibration files from ideal, i.e. without distortion
            
            Parameters
            ----------
            width : int
                Image width of calibration file
            height : int
                Image height of calibration file
            pixel_pitch : float
                Pixel pitch of calibration file
            focal_length : float
                Focal length of calibration file
            translation_x : float
                Translation in x axis of calibration file
            translation_y : float
                Translation in y axis of calibration file
            )")
        //.def("rectify", &I3DR::Phase::CameraCalibration::rectify)
        .def("isValid", &I3DR::Phase::CameraCalibration::isValid, R"(
            Check if the calibration file pair is valid 

            Returns
            -------
            bool
                True is calibration is valid
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
                Value of image height from calibration file
            )")
        .def("getImageWidth", &I3DR::Phase::CameraCalibration::getImageWidth, R"(
            Get the image width from calibration

            Returns
            -------
            width : int
                Value of image width from calibration file
            )")
        .def("getCameraMatrix", &I3DR::Phase::CameraCalibration::getCameraMatrix, R"(
            Get the camera matrix of calibration file

            Returns
            -------
            camera_matrix : numpy.ndarray                
                Camera matrix of calibration file
            )")
        .def("getDistortionCoefficients", &I3DR::Phase::CameraCalibration::getDistortionCoefficients, R"(
            Get the distortion coefficients of calibration file

            Returns
            -------
            distortion_coefficients : numpy.ndarray  
                Distortion coefficients of calibration file
            )")
        .def("getRectificationMatrix", &I3DR::Phase::CameraCalibration::getRectificationMatrix, R"(
            Get the rectification matrix of calibration file

            Returns
            -------
            rectification_matrix : numpy.ndarray  
                Rectification matrix of calibration file
            )")
        .def("getProjectionMatrix", &I3DR::Phase::CameraCalibration::getProjectionMatrix, R"(
            Get the projection matrix of calibration file

            Returns
            -------
            projection_matrix : numpy.ndarray  
                Projection matrix of calibration file
            )")
        .def("getCameraFX", &I3DR::Phase::CameraCalibration::getCameraFX, R"(
            Get the cameraFX of calibration file

            Returns
            -------
            cameraFX : float
                CameraFX of calibration file
            )")
        .def("getCameraFY", &I3DR::Phase::CameraCalibration::getCameraFY, R"(
            Get the cameraFY of calibration file

            Returns
            -------
            cameraFY : float
                CameraFY of calibration file
            )")
        .def("getCameraCX", &I3DR::Phase::CameraCalibration::getCameraCX, R"(
            Get the cameraCX of calibration file

            Returns
            -------
            cameraCX : float
                CameraCX of calibration file
            )")
        .def("getCameraCY", &I3DR::Phase::CameraCalibration::getCameraCY, R"(
            Get the cameraCY of calibration file

            Returns
            -------
            cameraCY : float
                CameraCY of calibration file
            )")
        .def("getProjectionFX", &I3DR::Phase::CameraCalibration::getProjectionFX, R"(
            Get the productionFX of calibration file

            Returns
            -------
            projectionFX : float
                ProductionFX of calibration file
            )")
        .def("getProjectionFY", &I3DR::Phase::CameraCalibration::getProjectionFY, R"(
            Get the productionFY of calibration file

            Returns
            -------
            projectionFY : float
                ProductionFY of calibration file
            )")
        .def("getProjectionCX", &I3DR::Phase::CameraCalibration::getProjectionCX, R"(
            Get the productionCX of calibration file

            Returns
            -------
            projectionCX : float
                ProductionCX of calibration file
            )")
        .def("getProjectionCY", &I3DR::Phase::CameraCalibration::getProjectionCY, R"(
            Get the productionCY of calibration file

            Returns
            -------
            projectionCY : float
                ProductionCY of calibration file
            )")
        .def("getProjectionTX", &I3DR::Phase::CameraCalibration::getProjectionTX, R"(
            Get the productionTX of calibration file

            Returns
            -------
            projectionTX : float
                ProductionTX of calibration file
            )");
}