/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file abstractstereomatcher_bindings.cpp
 * @brief Abstract Stereo Matcher class python bindings
 * @details Python bindings generated using pybind11
 */

#include "pybind11/pybind11.h"
#include "ndarray_converter.h"

#include <phase/stereomatcher/abstractstereomatcher.h>

namespace py = pybind11;

void init_abstractstereomatcher(py::module_ &m) {
    NDArrayConverter::init_numpy();
    //TODOC Description of the class and functions in StereoParams class
    py::class_<I3DR::Phase::StereoParams>(m, "StereoParams", R"(TODOC)")
        .def(py::init<I3DR::Phase::StereoMatcherType,int,int,int,bool>(), R"(TODOC)")
        .def_readwrite("matcherType", &I3DR::Phase::StereoParams::matcherType, R"(TODOC)")
        .def_readwrite("windowSize", &I3DR::Phase::StereoParams::windowSize, R"(TODOC)")
        .def_readwrite("minDisparity", &I3DR::Phase::StereoParams::minDisparity, R"(TODOC)")
        .def_readwrite("numDisparities", &I3DR::Phase::StereoParams::numDisparities, R"(TODOC)")
        .def_readwrite("interpolation", &I3DR::Phase::StereoParams::interpolation, R"(TODOC)");
    //TODOC Description of the class and functions in AbstractStereoMatcher class
    py::class_<I3DR::Phase::AbstractStereoMatcher>(m, "AbstractStereoMatcher", R"(TODOC)")
        .def("compute", &I3DR::Phase::AbstractStereoMatcher::compute, R"(TODOC)")
        .def("startComputeThread", &I3DR::Phase::AbstractStereoMatcher::startComputeThread, R"(TODOC)")
        .def("isComputeThreadRunning", &I3DR::Phase::AbstractStereoMatcher::isComputeThreadRunning, R"(TODOC)")
        .def("getComputeThreadResult", &I3DR::Phase::AbstractStereoMatcher::getComputeThreadResult, R"(TODOC)")
        .def("setComputeThreadCallback", &I3DR::Phase::AbstractStereoMatcher::setComputeThreadCallback, R"(TODOC)");

}