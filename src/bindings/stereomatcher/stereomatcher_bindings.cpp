/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file stereomatcher_bindings.cpp
 * @brief Stereo Matcher class python bindings
 * @details Python bindings generated using pybind11
 */

#include "pybind11/pybind11.h"
#include "ndarray_converter.h"

#include <phase/stereomatcher/stereomatcher.h>

namespace py = pybind11;

void init_stereomatcher(py::module_ &m) {
    NDArrayConverter::init_numpy();
    // Create stereo matcher caccording to type or params
    m.def("createStereoMatcher", static_cast<I3DR::Phase::AbstractStereoMatcher* (*)(I3DR::Phase::StereoMatcherType)>(&I3DR::Phase::createStereoMatcher), py::return_value_policy::reference, R"(
        Create stereo matching from stereo matcher type

        )");
    m.def("createStereoMatcher", static_cast<I3DR::Phase::AbstractStereoMatcher* (*)(I3DR::Phase::StereoParams)>(&I3DR::Phase::createStereoMatcher), py::return_value_policy::reference, R"(
        Create stereo matching from stereo matcher parameters

        )");
}