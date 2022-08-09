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
    //TODOC Description of the class and functions in StereoCameraCalibration class
    py::class_<I3DR::Phase::StereoCameraCalibration>(m, "StereoCameraCalibration", R"(TODOC)")
        .def(py::init<I3DR::Phase::CameraCalibration, I3DR::Phase::CameraCalibration>(), R"(TODOC)")
        .def_static("calibrationFromYAML", &I3DR::Phase::StereoCameraCalibration::calibrationFromYAML, R"(TODOC)")
        .def_static("calibrationFromIdeal", &I3DR::Phase::StereoCameraCalibration::calibrationFromIdeal, R"(TODOC)")
        .def_readwrite("left_calibration", &I3DR::Phase::StereoCameraCalibration::left_calibration, R"(TODOC)")
        .def_readwrite("right_calibration", &I3DR::Phase::StereoCameraCalibration::right_calibration, R"(TODOC)")
        .def("isValid", &I3DR::Phase::StereoCameraCalibration::isValid, R"(TODOC)")
        .def("isValidSize", &I3DR::Phase::StereoCameraCalibration::isValidSize, R"(TODOC)")
        .def("rectify", static_cast<I3DR::Phase::StereoImagePair(I3DR::Phase::StereoCameraCalibration::*)(cv::Mat, cv::Mat)>(&I3DR::Phase::StereoCameraCalibration::rectify), R"(TODOC)")
        .def("remapPoint", &I3DR::Phase::StereoCameraCalibration::remapPoint, R"(TODOC)")
        .def("getQ", &I3DR::Phase::StereoCameraCalibration::getQ, R"(TODOC)")
        .def("getBaseline", &I3DR::Phase::StereoCameraCalibration::getBaseline, R"(TODOC)")
        .def("getDownsampleFactor", &I3DR::Phase::StereoCameraCalibration::getDownsampleFactor, R"(TODOC)")
        .def("setDownsampleFactor", &I3DR::Phase::StereoCameraCalibration::setDownsampleFactor, R"(TODOC)")
        .def("getHFOV", &I3DR::Phase::StereoCameraCalibration::getHFOV, R"(TODOC)")
        .def("saveToYAML", &I3DR::Phase::StereoCameraCalibration::saveToYAML, R"(TODOC)");
}