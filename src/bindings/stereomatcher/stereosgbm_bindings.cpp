/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file stereosgbm_bindings.cpp
 * @brief Stereo Semi-Global Block Matcher class python bindings
 * @details Python bindings generated using pybind11
 */

#include "pybind11/pybind11.h"
#include "pybind11/functional.h"
#include "ndarray_converter.h"

#include <phase/stereomatcher/stereosgbm.h>

namespace py = pybind11;

void init_stereosgbm(py::module_ &m) {
    NDArrayConverter::init_numpy();

    py::class_<I3DR::Phase::StereoSGBM>(m, "StereoSGBM")
        .def(py::init<>())
        .def(py::init<I3DR::Phase::StereoParams>())
        .def("compute", &I3DR::Phase::StereoSGBM::compute)
        .def("startComputeThread", &I3DR::Phase::StereoSGBM::startComputeThread)
        .def("setComputeThreadCallback", &I3DR::Phase::StereoSGBM::setComputeThreadCallback)
        .def("isComputeThreadRunning", &I3DR::Phase::StereoSGBM::isComputeThreadRunning)
        .def("getComputeThreadResult", &I3DR::Phase::StereoSGBM::getComputeThreadResult)
        .def("setWindowSize", &I3DR::Phase::StereoSGBM::setWindowSize)
        .def("setMinDisparity", &I3DR::Phase::StereoSGBM::setMinDisparity)
        .def("setNumDisparities", &I3DR::Phase::StereoSGBM::setNumDisparities);
}