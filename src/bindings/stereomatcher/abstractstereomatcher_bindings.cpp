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
    // Stereo matcher parameters class
    py::class_<I3DR::Phase::StereoParams>(m, "StereoParams", R"(
        Class of stereo matcher parameters
        )")
        .def(py::init<I3DR::Phase::StereoMatcherType,int,int,int,bool>(), R"(
            Stereo parameters contain matcherType, windowSize, minDisparity, numDisparities, interpolation
        )")
        .def_readwrite("matcherType", &I3DR::Phase::StereoParams::matcherType)
        .def_readwrite("windowSize", &I3DR::Phase::StereoParams::windowSize)
        .def_readwrite("minDisparity", &I3DR::Phase::StereoParams::minDisparity)
        .def_readwrite("numDisparities", &I3DR::Phase::StereoParams::numDisparities)
        .def_readwrite("interpolation", &I3DR::Phase::StereoParams::interpolation);
    // Stereo matcher class
    py::class_<I3DR::Phase::AbstractStereoMatcher>(m, "AbstractStereoMatcher", R"(
        Class to set the parameters for stereo matcher
        )")
        .def("compute", &I3DR::Phase::AbstractStereoMatcher::compute, R"(
            Compute stereo matching

            Parameters
            ----------
            left_image : numpy.ndarray
                Left image of stereo pair
            right_image : numpy.ndarray
                Right image of stereo pair
            )")
        .def("startComputeThread", &I3DR::Phase::AbstractStereoMatcher::startComputeThread, R"(
            Start compute thread

            Parameters
            ----------
            left_image : numpy.ndarray
                Left image of stereo pair
            right_image : numpy.ndarray
                Right image of stereo pair
            )")
        .def("isComputeThreadRunning", &I3DR::Phase::AbstractStereoMatcher::isComputeThreadRunning, R"(
            Check if compute thread is running

            Returns
            -------
            bool
                True is compute thread is running
            )")
        .def("getComputeThreadResult", &I3DR::Phase::AbstractStereoMatcher::getComputeThreadResult, R"(
            Get compute thread result 
      
            )")
        .def("setComputeThreadCallback", &I3DR::Phase::AbstractStereoMatcher::setComputeThreadCallback, R"(
            Set to compute thread callback

            Parameters
            ----------
            computeThread_callback : std::function<void __cdecl(void)>
            )");

}