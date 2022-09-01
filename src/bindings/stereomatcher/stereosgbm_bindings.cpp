/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file stereosgbm_bindings.cpp
 * @brief Stereo Semi-Global Block Matcher class python bindings
 * @details Python bindings generated using pybind11
 */

#include "pybind11/pybind11.h"
#include "pybind11/functional.h"
#include "ndarray_converter.h"

#include <phase/stereomatcher/stereosgbm.h>

namespace py = pybind11;

void init_stereosgbm(py::module_ &m) {
    NDArrayConverter::init_numpy();
    py::class_<I3DR::Phase::StereoSGBM>(m, "StereoSGBM", R"(
        OpenCV's semi-global block matcher for generting disparity from stereo images
        )")
        .def(py::init<>(), R"(
            Initalise Stereo matcher and set default matching parameters
        )")
        .def(py::init<I3DR::Phase::StereoParams>(), R"(
            Initalise Stereo matcher and use provided StereoParams to set matching parameters
            
            )")
        .def("compute", &I3DR::Phase::StereoSGBM::compute, R"(
            Compute stereo matching
            Generates disparity from left and right images

            Parameters
            ----------
            left_image : numpy.ndarray
                Left image of stereo pair
            right_image : numpy.ndarray
                Right image of stereo pair
            )")
        .def("startComputeThread", &I3DR::Phase::StereoSGBM::startComputeThread, R"(
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
        .def("setComputeThreadCallback", &I3DR::Phase::StereoSGBM::setComputeThreadCallback, R"(
            Set callback function to run when compute thread completes
            Should be used with startComputeThread()
            Useful as an external trigger that compute is complete
            and results can be retrieved.

            Parameters
            ----------
            f : callback
            )")
        .def("isComputeThreadRunning", &I3DR::Phase::StereoSGBM::isComputeThreadRunning, R"(
            Check if compute thread is running

            Returns
            -------
            bool
                True is compute thread is running
            )")
        .def("getComputeThreadResult", &I3DR::Phase::StereoSGBM::getComputeThreadResult, R"(
            Get results from threaded compute process
            Should be used with startComputeThread()

            Returns
            -------
            StereoMatcherComputeResult
                result from compute

            )")
        .def("setWindowSize", &I3DR::Phase::StereoSGBM::setWindowSize, R"(
            Set window size value

            Parameters
            ----------
            value : int
                Desired value of window size value
            )")
        .def("getWindowSize", &I3DR::Phase::StereoSGBM::getWindowSize, R"(
            Get window size value

            Returns
            ----------
            value : int
                Value of window size
            )")
        .def("setMinDisparity", &I3DR::Phase::StereoSGBM::setMinDisparity, R"(
            Set minimum disparity value

            Parameters
            ----------
            value : int
                Desired value of minimum disparity value
            )")
        .def("getMinDisparity", &I3DR::Phase::StereoSGBM::getMinDisparity, R"(
            Get minimum disparity value

            Returns
            ----------
            value : int
                Value of minimum disparity
            )")
        .def("setNumDisparities", &I3DR::Phase::StereoSGBM::setNumDisparities, R"(
            Set number of disparities

            Parameters
            ----------
            value : int
                Desired value of number of disparities
            )")
        .def("getNumDisparities", &I3DR::Phase::StereoSGBM::getNumDisparities, R"(
            Get number of disparities

            Returns
            ----------
            value : int
                Value of number of disparities
            )");
}