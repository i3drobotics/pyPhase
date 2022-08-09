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
    //TODOC Description of the class and functions in StereoI3DRSGM class
    py::class_<I3DR::Phase::StereoI3DRSGM>(m, "StereoI3DRSGM", R"(TODOC)")
        .def(py::init<>(), R"(TODOC)")
        .def(py::init<I3DR::Phase::StereoParams>(), R"(TODOC)")
        .def("compute", &I3DR::Phase::StereoI3DRSGM::compute, R"(TODOC)")
        .def("startComputeThread", &I3DR::Phase::StereoI3DRSGM::startComputeThread, R"(TODOC)")
        .def("setComputeThreadCallback", &I3DR::Phase::StereoI3DRSGM::setComputeThreadCallback, R"(TODOC)")
        .def("isComputeThreadRunning", &I3DR::Phase::StereoI3DRSGM::isComputeThreadRunning, R"(TODOC)")
        .def("getComputeThreadResult", &I3DR::Phase::StereoI3DRSGM::getComputeThreadResult, R"(TODOC)")
        .def("setWindowSize", &I3DR::Phase::StereoI3DRSGM::setWindowSize, R"(TODOC)")
        .def("setMinDisparity", &I3DR::Phase::StereoI3DRSGM::setMinDisparity, R"(TODOC)")
        .def("setNumDisparities", &I3DR::Phase::StereoI3DRSGM::setNumDisparities, R"(TODOC)")
        .def("setSpeckleMaxSize", &I3DR::Phase::StereoI3DRSGM::setSpeckleMaxSize, R"(TODOC)")
        .def("setSpeckleMaxDiff", &I3DR::Phase::StereoI3DRSGM::setSpeckleMaxDiff, R"(TODOC)")
        .def("enableSubpixel", &I3DR::Phase::StereoI3DRSGM::enableSubpixel, R"(TODOC)")
        .def("enableInterpolation", &I3DR::Phase::StereoI3DRSGM::enableInterpolation, R"(TODOC)")
        .def_static("isLicenseValid", &I3DR::Phase::StereoI3DRSGM::isLicenseValid, R"(TODOC)");
}