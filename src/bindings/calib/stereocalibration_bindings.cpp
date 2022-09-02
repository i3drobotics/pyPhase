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

    py::enum_<I3DR::Phase::CalibrationSelection>(m, "CalibrationSelection", R"(
        Enum to indicate calibration from left or right camera/image

        )")
        .value("LEFT", I3DR::Phase::CalibrationSelection::LEFT)
        .value("RIGHT", I3DR::Phase::CalibrationSelection::RIGHT)
        .export_values();

    // Load in stereo camera calibration file
    py::class_<I3DR::Phase::StereoCameraCalibration>(m, "StereoCameraCalibration", R"(
            Store and manipulate stereo camera calibration data.

            )")
        .def(py::init<I3DR::Phase::CameraCalibration, I3DR::Phase::CameraCalibration>(), R"(
            Initalise stereo camera calibration using left and right calibration.

            Parameters
            ----------
            left_calibration : phase.pyphase.calib.CameraCalibration
                Left calibration file
            right_calibration : phase.pyphase.calib.CameraCalibration
                Right calibration file
            )")
        .def_static("calibrationFromYAML", &I3DR::Phase::StereoCameraCalibration::calibrationFromYAML, R"(
            Load calibration from yaml files

            Parameters
            ----------
            left_calibration_filepath : str
                Left side calibration file path directory
            right_calibration_filepath : str
                Right side calibration file path directory
            )")
        .def_static("calibrationFromIdeal", &I3DR::Phase::StereoCameraCalibration::calibrationFromIdeal, R"(
            Create ideal stereo calibration from camera information

            Parameters
            ----------
            width : int
                Image width of cameras
            height : int
                Image height of cameras
            pixel_pitch : float
                Pixel pitch of cameras
            focal_length : float
                Focal length of cameras
            baseline : float
                Baseline of stereo camera
            )")
        .def_static("calibrationFromImages", &I3DR::Phase::StereoCameraCalibration::calibrationFromImages, R"(
            Create ideal stereo calibration from camera information

            Parameters
            ----------
            left_cal_folder : str
                Path to folder with left calibration images
            right_cal_folder : str
                Path to folder with right calibration images
            left_img_wildcard : str
                Wildcard to use for identifying left images
            right_img_wildcard : str
                Wildcard to use for identifying right images
            board_type : enum
                Calibration board type used in calibration images
            pattern_size_x : int
                Number of rows in calibration board pattern
            pattern_size_y : int
                Number of columns in calibration board pattern
            square_size : float
                Width of single square in calibration board pattern (in meters)
            
            Returns
                Stereo camera calibration
            )")
        .def_readwrite("left_calibration", &I3DR::Phase::StereoCameraCalibration::left_calibration, R"(
            Stores left camera calibration

            )")
        .def_readwrite("right_calibration", &I3DR::Phase::StereoCameraCalibration::right_calibration, R"(
            Stores right camera calibration

            )")
        .def("isValid", &I3DR::Phase::StereoCameraCalibration::isValid, R"(
            Check if loaded calibration is valid

            Returns
            -------
            bool
                True if calibration file is valid
            )")
        .def("isValidSize", &I3DR::Phase::StereoCameraCalibration::isValidSize, R"(
            Check if loaded calibration image width and height match specified values

            Parameters
            ----------
            width : int
                Image width to check against
            height : int
                Image height to check against

            
            Returns
            -------
            bool
                True if calibration file is valid in size
            )")
        .def("rectify", static_cast<I3DR::Phase::StereoImagePair(I3DR::Phase::StereoCameraCalibration::*)(cv::Mat, cv::Mat)>(&I3DR::Phase::StereoCameraCalibration::rectify), R"(
            Rectify stereo images based on calibration

            Parameters
            ----------
            left_image : numpy.ndarray
                Left image to rectify
            right_image : numpy.ndarray
                Right image to rectify
            left_rect_image : numpy.ndarray
                Rectified left stereo image
            right_rect_image : numpy.ndarray
                Rectified right stereo image
            )")
        .def("getQ", &I3DR::Phase::StereoCameraCalibration::getQ, R"(
            Get the Q matrix

            Returns
            -------
            Q : numpy.ndarray
                Q matrix
            )")
        .def("getBaseline", &I3DR::Phase::StereoCameraCalibration::getBaseline, R"(
            Get the baseline from calibration

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
            Get horitonzal Field Of View of camera from calibration

            Returns
            -------
            fov_x : float
                Horitonzal Field Of View of camera
            )")
        .def("saveToYAML", &I3DR::Phase::StereoCameraCalibration::saveToYAML, R"(
            Save stereo camera calibration to YAML files

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