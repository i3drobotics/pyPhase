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
    //TODOC Description of the class and functions in StereoHOBM class
    py::class_<I3DR::Phase::StereoHOBM>(m, "StereoHOBM", R"(TODOC)")
        .def(py::init<>(), R"(TODOC)")
        .def(py::init<I3DR::Phase::StereoParams>(), R"(TODOC)")
        .def("compute", &I3DR::Phase::StereoHOBM::compute, R"(TODOC)")
        .def("startComputeThread", &I3DR::Phase::StereoHOBM::startComputeThread, R"(TODOC)")
        .def("setComputeThreadCallback", &I3DR::Phase::StereoHOBM::setComputeThreadCallback, R"(TODOC)")
        .def("isComputeThreadRunning", &I3DR::Phase::StereoHOBM::isComputeThreadRunning, R"(TODOC)")
        .def("getComputeThreadResult", &I3DR::Phase::StereoHOBM::getComputeThreadResult, R"(TODOC)")
        .def("setWindowSize", &I3DR::Phase::StereoHOBM::setWindowSize, R"(TODOC)")
        .def("setMinDisparity", &I3DR::Phase::StereoHOBM::setMinDisparity, R"(TODOC)")
        .def("setNumDisparities", &I3DR::Phase::StereoHOBM::setNumDisparities, R"(TODOC)");
}