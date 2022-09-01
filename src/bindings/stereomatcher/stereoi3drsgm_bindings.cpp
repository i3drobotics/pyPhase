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
    py::class_<I3DR::Phase::StereoI3DRSGM>(m, "StereoI3DRSGM", R"(
        I3DRS's stereo semi-global matcher for generting disparity from stereo images.
    
        )")
        .def(py::init<>(), R"(
            Initalise Stereo matcher and set default matching parameters
        )")
        .def(py::init<I3DR::Phase::StereoParams>(), R"(
            Initalise Stereo matcher and use provided StereoParams to set matching parameters
            
            )")
        .def("compute", &I3DR::Phase::StereoI3DRSGM::compute, R"(
            Compute stereo matching
            Generates disparity from left and right images

            Parameters
            ----------
            left_image : numpy.ndarray
                Left image of stereo pair
            right_image : numpy.ndarray
                Right image of stereo pair
            )")
        .def("startComputeThread", &I3DR::Phase::StereoI3DRSGM::startComputeThread, R"(
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
        .def("setComputeThreadCallback", &I3DR::Phase::StereoI3DRSGM::setComputeThreadCallback, R"(
            Set callback function to run when compute thread completes
            Should be used with startComputeThread()
            Useful as an external trigger that compute is complete
            and results can be retrieved.

            Parameters
            ----------
            f : callback
            )")
        .def("isComputeThreadRunning", &I3DR::Phase::StereoI3DRSGM::isComputeThreadRunning, R"(
            Check if compute thread is running

            Returns
            -------
            bool
                True is compute thread is running
            )")
        .def("getComputeThreadResult", &I3DR::Phase::StereoI3DRSGM::getComputeThreadResult, R"(
            Get results from threaded compute process
            Should be used with startComputeThread()

            Returns
            -------
            StereoMatcherComputeResult
                result from compute

            )")
        .def("setWindowSize", &I3DR::Phase::StereoI3DRSGM::setWindowSize, R"(
            Set window size value

            Parameters
            ----------
            value : int
                Desired value of window size value
            )")
        .def("getWindowSize", &I3DR::Phase::StereoI3DRSGM::getWindowSize, R"(
            Get window size value

            Returns
            ----------
            value : int
                Value of window size
            )")
        .def("setMinDisparity", &I3DR::Phase::StereoI3DRSGM::setMinDisparity, R"(
            Set minimum disparity value

            Parameters
            ----------
            value : int
                Desired value of minimum disparity value
            )")
        .def("getMinDisparity", &I3DR::Phase::StereoI3DRSGM::getMinDisparity, R"(
            Get minimum disparity value

            Returns
            ----------
            value : int
                Value of minimum disparity
            )")
        .def("setNumDisparities", &I3DR::Phase::StereoI3DRSGM::setNumDisparities, R"(
            Set number of disparities

            Parameters
            ----------
            value : int
                Desired value of number of disparities
            )")
        .def("getNumDisparities", &I3DR::Phase::StereoI3DRSGM::getNumDisparities, R"(
            Get number of disparities

            Returns
            ----------
            value : int
                Value of number of disparities
            )")
        .def("setSpeckleMaxSize", &I3DR::Phase::StereoI3DRSGM::setSpeckleMaxSize, R"(
            To enable speckle maximum size
            
            Parameters
            ----------
            enable : bool
                Set True to enable speckle maximum size
            )")
        .def("setSpeckleMaxDiff", &I3DR::Phase::StereoI3DRSGM::setSpeckleMaxDiff, R"(
            To enable speckle maximum difference
            
            Parameters
            ----------
            enable : bool
                Set True to enable speckle maximum difference
            )")
        .def("enableSubpixel", &I3DR::Phase::StereoI3DRSGM::enableSubpixel, R"(
            To enable subpixel
            
            Parameters
            ----------
            enable : bool
                Set True to enable subpixel
            )")
        .def("enableInterpolation", &I3DR::Phase::StereoI3DRSGM::enableInterpolation, R"(
            To enable interpolation
            
            Parameters
            ----------
            enable : bool
                Set True to enable interpolation
            )")
        .def_static("isLicenseValid", &I3DR::Phase::StereoI3DRSGM::isLicenseValid, R"(
            Check if the I3DRSGM license is valid
            
            Returns
            -------
            bool
                True if license is valid
            )");
}