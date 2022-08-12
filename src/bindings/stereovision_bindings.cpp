/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file stereovision_bindings.cpp
 * @brief Stereo Vision class python bindings
 * @details Python bindings generated using pybind11
 */

#include "pybind11/pybind11.h"
#include "ndarray_converter.h"

#include <phase/stereovision.h>

namespace py = pybind11;

void init_stereovision(py::module_ &m) {
    NDArrayConverter::init_numpy();

    py::class_<I3DR::Phase::StereoVision>(m, "StereoVision", py::module_local(), R"(
        Stereo Vision class
        

        Capture images from stereo camera and process with stereo matcher
        to generate depth. Brings together Stereo Camera and Stereo Matcher classes into
        single class for easy use.

        )")
        
        .def(py::init<I3DR::Phase::CameraDeviceInfo,I3DR::Phase::StereoMatcherType,const char*,const char*>(), R"(
            Load stereo matcher

            Parameters
            ----------
            left_yaml : str
            right_yaml : str
            )")
        .def("connect", &I3DR::Phase::StereoVision::connect, R"(
            Connect camera from reading CameraDeviceInfo

            )")
        .def("isConnected", &I3DR::Phase::StereoVision::isConnected, R"(
            Check if camera is connected

            )")
        .def("startCapture", &I3DR::Phase::StereoVision::startCapture, R"(
            To start camera communication

            )")
        .def("stopCapture", &I3DR::Phase::StereoVision::stopCapture, R"(
            To stop camera communication

            )")
        .def("isCapturing", &I3DR::Phase::StereoVision::isCapturing, R"(
            Check if camera is capturing

            )")
        .def("isValidCalibration", &I3DR::Phase::StereoVision::isValidCalibration, R"(
            Check if the calibration file pair is valid 

            Returns
            -------
            bool
                True is calibration is valid
            )")
        .def("getWidth", &I3DR::Phase::StereoVision::getWidth, R"(
            Get the width of image
            
            Returns
            -------
            value : int
                Width of image
            )")
        .def("getHeight", &I3DR::Phase::StereoVision::getHeight, R"(
            Get the height of image
            
            Returns
            -------
            value : int
                Height of image
            )")
        .def("getDownsampleFactor", &I3DR::Phase::StereoVision::getDownsampleFactor, R"(
            Get the value of Downsample Factor
            
            Returns
            -------
            value : float
                Downsampled factor
            )")
        .def("setTestImagePaths", &I3DR::Phase::StereoVision::setTestImagePaths, R"(
            Set the path for test images, input both left and right image path

            Parameters
            ----------
            left_test_image_path    : str
            right_test_image_path   : str
            )")
        .def("getCamera", &I3DR::Phase::StereoVision::getCamera, py::return_value_policy::reference, R"(
            Load camera

            )")
        .def("getMatcher", &I3DR::Phase::StereoVision::getMatcher, py::return_value_policy::reference, R"(
            Load stereo matcher

            )")
        .def("getCalibration", &I3DR::Phase::StereoVision::getCalibration, py::return_value_policy::reference, R"(
            Load stereo calibration
    
            )")
        .def("getHFOV", &I3DR::Phase::StereoVision::getHFOV, R"(
            Get horitonzal Field Of View of camera from Q matrix

            Returns
            -------
            fov_x : float
                Horitonzal Field Of View of camera from Q matrix
            )")
        .def("setDownsampleFactor", &I3DR::Phase::StereoVision::setDownsampleFactor, R"(
            Set downsample factor

            Parameters
            ----------
            value : float
                Desired value of downsample factor
            )")
        .def("read", &I3DR::Phase::StereoVision::read, py::arg("timeout") = 1000, py::arg("rectify") = true, R"(
            Read image from camera
            
            Parameters
            ----------
            timeout : int
                timeout in millisecond, default timeout is 1000(1s)
            Returns
            -------
            left : numpy.ndarray, right : numpy.ndarray
                Return stereo images left, right
            )")
        .def("startReadThread", &I3DR::Phase::StereoVision::startReadThread, py::arg("timeout") = 1000, py::arg("rectify") = true, R"(
            Read camera thread
            
            Parameters
            ----------
            timeout : int
                timeout in millisecond, default timeout is 1000(1s)

            Returns
            -------
            bool
                True if thread is reading
            )")
        .def("isReadThreadRunning", &I3DR::Phase::StereoVision::isReadThreadRunning, R"(
            Check if camera thread is reading

            Returns
            -------
            bool
                True if thread is reading
            )")
        .def("getReadThreadResult", &I3DR::Phase::StereoVision::getReadThreadResult, R"(
            Get the result of thread read

            )")
        .def("disconnect", &I3DR::Phase::StereoVision::disconnect, R"(
            Disconnect camera from reading CameraDeviceInfo

            )");
        //TODO add callback funtion for read results (https://pybind11.readthedocs.io/en/stable/advanced/cast/functional.html)
}