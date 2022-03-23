/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file stereobm_bindings.cpp
 * @brief Stereo Block Matcher class python bindings
 * @details Python bindings generated using pybind11
 */

#include"pybind11/pybind11.h"
#include "pybind11/functional.h"
#include "ndarray_converter.h"

#include <phase/stereomatcher/stereobm.h>

namespace py = pybind11;

void init_stereobm(py::module_ &m) {
    NDArrayConverter::init_numpy();

    py::class_<I3DR::Phase::StereoBM>(m, "StereoBM")
        .def(py::init<>())
        .def(py::init<I3DR::Phase::StereoParams>())
        .def("compute", &I3DR::Phase::StereoBM::compute)
        .def("startComputeThread", &I3DR::Phase::StereoBM::startComputeThread)
        .def("setComputeThreadCallback", &I3DR::Phase::StereoBM::setComputeThreadCallback)
        .def("isComputeThreadRunning", &I3DR::Phase::StereoBM::isComputeThreadRunning)
        .def("getComputeThreadResult", &I3DR::Phase::StereoBM::getComputeThreadResult)
        .def("setWindowSize", &I3DR::Phase::StereoBM::setWindowSize)
        .def("setMinDisparity", &I3DR::Phase::StereoBM::setMinDisparity)
        .def("setNumDisparities", &I3DR::Phase::StereoBM::setNumDisparities);
}