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

#include <phase/calib/stereocalibration.h>

namespace py = pybind11;

void init_stereocalibration(py::module_ &m) {
    NDArrayConverter::init_numpy();
    // Load in stereo camera calibration file
    py::class_<I3DR::Phase::StereoCameraCalibration>(m, "StereoCameraCalibration", R"(
            Variables of stereo camera calibration file
            )")
        .def(py::init<I3DR::Phase::CameraCalibration, I3DR::Phase::CameraCalibration>(), R"(
            Load left and right calibration file

            Parameters
            ----------
            left_calibration : phase.pyphase.calib.CameraCalibration
                Left calibration file
            right_calibration : phase.pyphase.calib.CameraCalibration
                Right calibration file
            )")
        .def_static("calibrationFromYAML", &I3DR::Phase::StereoCameraCalibration::calibrationFromYAML, R"(
            Load calibration files in yaml format

            Parameters
            ----------
            left_calibration_filepath : str
                Left side calibration file path directory
            right_calibration_filepath : str
                Right side calibration file path directory
            )")
        .def_static("calibrationFromIdeal", &I3DR::Phase::StereoCameraCalibration::calibrationFromIdeal, R"(
            Load calibration files with ideal variables

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
            baseline : float
                Baseline value of calibration file
            )")
        .def_readwrite("left_calibration", &I3DR::Phase::StereoCameraCalibration::left_calibration, R"(
            Store variables of Left calibration

            )")
        .def_readwrite("right_calibration", &I3DR::Phase::StereoCameraCalibration::right_calibration, R"(
            Store variables of Left calibration

            )")
        .def("isValid", &I3DR::Phase::StereoCameraCalibration::isValid, R"(
            Check if the calibration file is valid

            Returns
            -------
            bool
                True if calibration file is valid
            )")
        .def("isValidSize", &I3DR::Phase::StereoCameraCalibration::isValidSize, R"(
            Check if the calibration file in valid size

            Returns
            -------
            bool
                True if calibration file is valid in size
            )")
        .def("rectify", static_cast<I3DR::Phase::StereoImagePair(I3DR::Phase::StereoCameraCalibration::*)(cv::Mat, cv::Mat)>(&I3DR::Phase::StereoCameraCalibration::rectify), R"(
            Rectify stereo image pair from calibration file

            Parameters
            ----------
            left_image : numpy.ndarray
                Stereo camera left image
            right_image : numpy.ndarray
                Stereo camera right image
            left_rect_image : numpy.ndarray
                numpy.ndarray to store left rectified image
            right_rect_image : numpy.ndarray
                numpy.ndarray to store right rectified image
            )")
        .def("remapPoint", &I3DR::Phase::StereoCameraCalibration::remapPoint, R"(
            Remap point from calibration

            Parameters
            ----------
            point : phase.pyphase.types.Point2i
            camera_selection : enum

            Returns
            -------
            remapped_point : phase.pyphase.types.Point2i
            )")
        .def("getQ", &I3DR::Phase::StereoCameraCalibration::getQ, R"(
            Get the Q matrix in numpy.ndarray

            Returns
            -------
            Q : numpy.ndarray
                Q matrix of calibration file
            )")
        .def("getBaseline", &I3DR::Phase::StereoCameraCalibration::getBaseline, R"(
            Get the baseline value of calibration file

            Returns
            -------
            value : float
                Baseline value of calibration file
            )")
        .def("getDownsampleFactor", &I3DR::Phase::StereoCameraCalibration::getDownsampleFactor, R"(
            Get downsample factor

            Returns
            -------
            value : float
                Downsample value of calibration files
            )")
        .def("setDownsampleFactor", &I3DR::Phase::StereoCameraCalibration::setDownsampleFactor, R"(
            Set downsample factor

            Parameters
            ----------
            value : float
                Desired value of downsample factor
            )")
        .def("getHFOV", &I3DR::Phase::StereoCameraCalibration::getHFOV, R"(
            Get horitonzal Field Of View of camera from Q matrix

            Returns
            -------
            fov_x : float
                Horitonzal Field Of View of camera from Q matrix
            )")
        .def("saveToYAML", &I3DR::Phase::StereoCameraCalibration::saveToYAML, R"(
            Flip image horizontally or vertically based on flip code.

            Parameters
            ----------
            left_calibration_filepath : str
                Desired path directory to save calibration file
            right_calibration_filepath : str
                Desired path directory to save calibration file
            cal_file_type : enum
                Type of calibration file, e.g. ROS_YAML/OPENCV_YAML
            
            Returns
            -------
            bool
                True if calibration yaml files are saved
            )");
}