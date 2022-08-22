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

    py::class_<I3DR::Phase::StereoMatcherComputeResult>(m, "StereoMatcherComputeResult", R"(
        Struture to store the result from a stereo match. Used in the stereo matcher classes.
        )")
        .def(py::init<bool,cv::Mat>())
        .def_readwrite("valid", &I3DR::Phase::StereoMatcherComputeResult::valid)
        .def_readwrite("disparity", &I3DR::Phase::StereoMatcherComputeResult::disparity);

    py::enum_<I3DR::Phase::StereoMatcherType>(m, "StereoMatcherType", R"(
        Enum to indicate stereo matcher type. Used in stereo matcher class to select which matcher to use.

        )")
        .value("STEREO_MATCHER_BM", I3DR::Phase::StereoMatcherType::STEREO_MATCHER_BM)
        .value("STEREO_MATCHER_SGBM", I3DR::Phase::StereoMatcherType::STEREO_MATCHER_SGBM)
        .value("STEREO_MATCHER_I3DRSGM", I3DR::Phase::StereoMatcherType::STEREO_MATCHER_I3DRSGM)
        .export_values();

    // Stereo matcher parameters class
    py::class_<I3DR::Phase::StereoParams>(m, "StereoParams", R"(
        Struture to store stereo parameters
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
        Abstract base class for building stereo matcher
        classes. Includes functions/structures common across
        all stereo matchers. A stereo matcher takes a two images
        (left and right) and calculates to pixel disparity of features.
        The produces a disparity value for each pixel which can be
        used to generate depth.
        )")
        .def("compute", &I3DR::Phase::AbstractStereoMatcher::compute, R"(
            Compute stereo matching
            Generates disparity from left and right images

            Parameters
            ----------
            left_image : numpy.ndarray
                Left image of stereo pair
            right_image : numpy.ndarray
                Right image of stereo pair
            )")
        .def("startComputeThread", &I3DR::Phase::AbstractStereoMatcher::startComputeThread, R"(
            Start compute thread
            Generates disparity from left and right images
            Use getComputeThreadResult() to get results of compute

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
            Get results from threaded compute process
            Should be used with startComputeThread()

            Returns
            -------
            StereoMatcherComputeResult
                result from compute
      
            )")
        .def("setComputeThreadCallback", &I3DR::Phase::AbstractStereoMatcher::setComputeThreadCallback, R"(
            Set callback function to run when compute thread completes
            Should be used with startComputeThread()
            Useful as an external trigger that compute is complete
            and results can be retrieved.

            Parameters
            ----------
            f : callback
            )");

}