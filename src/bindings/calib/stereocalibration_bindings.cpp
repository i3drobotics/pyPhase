/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file stereocalibration_bindings.cpp
 * @brief Stereo Calibration class python bindings
 * @details Python bindings generated using pybind11
 */

#include"pybind11/pybind11.h"
#include "ndarray_converter.h"

#include <phase/calib/stereocalibration.h>

namespace py = pybind11;

void init_stereocalibration(py::module_ &m) {
    NDArrayConverter::init_numpy();

    py::class_<I3DR::Phase::StereoCameraCalibration>(m, "StereoCameraCalibration")
        .def(py::init<I3DR::Phase::CameraCalibration, I3DR::Phase::CameraCalibration>())
        .def_static("calibrationFromYAML", &I3DR::Phase::StereoCameraCalibration::calibrationFromYAML)
        .def_static("calibrationFromIdeal", &I3DR::Phase::StereoCameraCalibration::calibrationFromIdeal)
        .def("isValid", &I3DR::Phase::StereoCameraCalibration::isValid)
        .def("isValidSize", &I3DR::Phase::StereoCameraCalibration::isValidSize)
        .def("rectify", static_cast<I3DR::Phase::StereoImagePair(I3DR::Phase::StereoCameraCalibration::*)(cv::Mat, cv::Mat)>(&I3DR::Phase::StereoCameraCalibration::rectify))
        .def("remapPoint", &I3DR::Phase::StereoCameraCalibration::remapPoint)
        .def("getQ", &I3DR::Phase::StereoCameraCalibration::getQ)
        .def("getBaseline", &I3DR::Phase::StereoCameraCalibration::getBaseline)
        .def("getDownsampleFactor", &I3DR::Phase::StereoCameraCalibration::getDownsampleFactor)
        .def("setDownsampleFactor", &I3DR::Phase::StereoCameraCalibration::setDownsampleFactor)
        .def("getHFOV", &I3DR::Phase::StereoCameraCalibration::getHFOV)
        .def("saveToYAML", &I3DR::Phase::StereoCameraCalibration::saveToYAML);
}