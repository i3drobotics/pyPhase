/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file stereoi3drsgm_bindings.cpp
 * @brief I3DR's Semi-Global Stereo Matcher class python bindings
 * @details Python bindings generated using pybind11
 */

#include "pybind11/pybind11.h"
#include "pybind11/functional.h"
#include "ndarray_converter.h"

#include <phase/stereomatcher/stereoi3drsgm.h>

namespace py = pybind11;

void init_stereoi3drsgm(py::module_ &m) {
    NDArrayConverter::init_numpy();

    py::class_<I3DR::Phase::StereoI3DRSGM>(m, "StereoI3DRSGM")
        .def(py::init<>())
        .def(py::init<I3DR::Phase::StereoParams>())
        .def("compute", &I3DR::Phase::StereoI3DRSGM::compute)
        .def("startComputeThread", &I3DR::Phase::StereoI3DRSGM::startComputeThread)
        .def("setComputeThreadCallback", &I3DR::Phase::StereoI3DRSGM::setComputeThreadCallback)
        .def("isComputeThreadRunning", &I3DR::Phase::StereoI3DRSGM::isComputeThreadRunning)
        .def("getComputeThreadResult", &I3DR::Phase::StereoI3DRSGM::getComputeThreadResult)
        .def("setWindowSize", &I3DR::Phase::StereoI3DRSGM::setWindowSize)
        .def("setMinDisparity", &I3DR::Phase::StereoI3DRSGM::setMinDisparity)
        .def("setNumDisparities", &I3DR::Phase::StereoI3DRSGM::setNumDisparities)
        .def("setSpeckleMaxSize", &I3DR::Phase::StereoI3DRSGM::setSpeckleMaxSize)
        .def("setSpeckleMaxDiff", &I3DR::Phase::StereoI3DRSGM::setSpeckleMaxDiff)
        .def("enableSubpixel", &I3DR::Phase::StereoI3DRSGM::enableSubpixel)
        .def("enableInterpolation", &I3DR::Phase::StereoI3DRSGM::enableInterpolation)
        .def_static("isLicenseValid", &I3DR::Phase::StereoI3DRSGM::isLicenseValid);
}