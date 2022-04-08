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

    py::class_<I3DR::Phase::StereoParams>(m, "StereoParams")
        .def(py::init<I3DR::Phase::StereoMatcherType,int,int,int,bool>())
        .def_readwrite("matcherType", &I3DR::Phase::StereoParams::matcherType)
        .def_readwrite("windowSize", &I3DR::Phase::StereoParams::windowSize)
        .def_readwrite("minDisparity", &I3DR::Phase::StereoParams::minDisparity)
        .def_readwrite("numDisparities", &I3DR::Phase::StereoParams::numDisparities)
        .def_readwrite("interpolation", &I3DR::Phase::StereoParams::interpolation);

    py::class_<I3DR::Phase::AbstractStereoMatcher>(m, "AbstractStereoMatcher")
        .def("compute", &I3DR::Phase::AbstractStereoMatcher::compute)
        .def("startComputeThread", &I3DR::Phase::AbstractStereoMatcher::startComputeThread)
        .def("isComputeThreadRunning", &I3DR::Phase::AbstractStereoMatcher::isComputeThreadRunning)
        .def("getComputeThreadResult", &I3DR::Phase::AbstractStereoMatcher::getComputeThreadResult)
        .def("setComputeThreadCallback", &I3DR::Phase::AbstractStereoMatcher::setComputeThreadCallback);

}