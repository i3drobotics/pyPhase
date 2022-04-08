/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file stereobm_bindings.cpp
 * @brief Stereo Block Matcher class python bindings
 * @details Python bindings generated using pybind11
 */

#include "pybind11/pybind11.h"
#include "pybind11/functional.h"
#include "ndarray_converter.h"

#include <phase/stereomatcher/stereohobm.h>

namespace py = pybind11;

void init_stereohobm(py::module_ &m) {
    NDArrayConverter::init_numpy();

    py::class_<I3DR::Phase::StereoHOBM>(m, "StereoHOBM")
        .def(py::init<>())
        .def(py::init<I3DR::Phase::StereoParams>())
        .def("compute", &I3DR::Phase::StereoHOBM::compute)
        .def("startComputeThread", &I3DR::Phase::StereoHOBM::startComputeThread)
        .def("setComputeThreadCallback", &I3DR::Phase::StereoHOBM::setComputeThreadCallback)
        .def("isComputeThreadRunning", &I3DR::Phase::StereoHOBM::isComputeThreadRunning)
        .def("getComputeThreadResult", &I3DR::Phase::StereoHOBM::getComputeThreadResult)
        .def("setWindowSize", &I3DR::Phase::StereoHOBM::setWindowSize)
        .def("setMinDisparity", &I3DR::Phase::StereoHOBM::setMinDisparity)
        .def("setNumDisparities", &I3DR::Phase::StereoHOBM::setNumDisparities);
}