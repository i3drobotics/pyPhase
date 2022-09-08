/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file pylonstereocamera_bindings.cpp
 * @brief Pylon Stereo Camera class python bindings
 * @details Python bindings generated using pybind11
 */

#include "pybind11/pybind11.h"
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include <pybind11/functional.h>
#include "ndarray_converter.h"

#include <phase/stereocamera/pylonstereocamera.h>

namespace py = pybind11;

void init_pylonstereocamera(py::module_ &m) {
    NDArrayConverter::init_numpy();
    // All functions and variables of PylonStereoCamera
    py::class_<I3DR::Phase::PylonStereoCamera>(m, "PylonStereoCamera", R"(
            Capture data from a stereo camera using Basler cameras via the Pylon API

            )")
        .def(py::init<I3DR::Phase::CameraDeviceInfo>(), R"(
            Initalise Stereo Camera with the given device_info.

            Parameters
            ----------

            device_info     : CameraDeviceInfo
                Camera device information to use when initalising camera
            )", py::arg("device_info"))
        .def("connect", &I3DR::Phase::PylonStereoCamera::connect, R"(
            Connect to camera

            )")
        .def("isConnected", &I3DR::Phase::PylonStereoCamera::isConnected, R"(
            Check if camera is connected

            )")
        .def("startCapture", &I3DR::Phase::PylonStereoCamera::startCapture, R"(
            Start stereo camera capture
            Must be started before read() is called
    
            )")
        .def("stopCapture", &I3DR::Phase::PylonStereoCamera::stopCapture, R"(
            Stop stereo camera capture
            Will no longer be able to read() after this is called

            )")
        .def("isCapturing", &I3DR::Phase::PylonStereoCamera::isCapturing, R"(
            Check if camera is capturing
            
            )")
        .def("getFrameRate", &I3DR::Phase::PylonStereoCamera::getFrameRate, R"(
            Get the value of frame rate
    
            )")
        .def("setExposure", &I3DR::Phase::PylonStereoCamera::setExposure, R"(
            Set exposure value of camera

            Parameters
            ----------

            value : int
                Value of exposure (us)
            )", py::arg("value"))
        .def("enableHardwareTrigger", &I3DR::Phase::PylonStereoCamera::enableHardwareTrigger, R"(
            Enable camera hardware trigger

            Parameters
            ----------

            enable : bool
                Set "True" to enable hardware trigger
            )", py::arg("enable"))
        .def("setFrameRate", &I3DR::Phase::PylonStereoCamera::setFrameRate, R"(
            Set frame rate of camera
            
            Parameters
            ----------
            value : float
                Value of frame rate
            )", py::arg("value"))
        .def("setLeftAOI", &I3DR::Phase::PylonStereoCamera::setLeftAOI, R"(
            To set area of interest for left camera
            
            Parameters
            ----------
            x_min : int
                x value of top left corner of targeted AOI
            y_min : int
                y value of top left corner of targeted AOI
            x_max : int
                x value of bottom right corner of targeted AOI
            y_max : int
                y value of bottom right corner of targeted AOI
            )", py::arg("x_min"), py::arg("y_min"), py::arg("x_max"), py::arg("y_max"))
        .def("setRightAOI", &I3DR::Phase::PylonStereoCamera::setRightAOI, R"(
            To set area of interest for right camera
            
            Parameters
            ----------
            x_min : int
                x value of top left corner of targeted AOI
            y_min : int
                y value of top left corner of targeted AOI
            x_max : int
                x value of bottom right corner of targeted AOI
            y_max : int
                y value of bottom right corner of targeted AOI
            )", py::arg("x_min"), py::arg("y_min"), py::arg("x_max"), py::arg("y_max"))
        .def("read", &I3DR::Phase::PylonStereoCamera::read, py::arg("timeout") = 1000, R"(
            Read image frame from camera

            Parameters
            ----------
            timeout : int
                Timeout in millisecond, default timeout is 1000(1s)
            Returns
            -------
            CameraReadResult
                Result from camera read
            )")
        .def("setTestImagePaths", &I3DR::Phase::PylonStereoCamera::setTestImagePaths, R"(
            Set the path for test images, input both left and right image path

            Parameters
            ----------
            left_test_image_path    : str
            right_test_image_path   : str
            )", py::arg("left_test_image_path"), py::arg("right_test_image_path"))
        .def("startReadThread", &I3DR::Phase::PylonStereoCamera::startReadThread, py::arg("timeout") = 1000, R"(
            Read camera thread
            
            Parameters
            ----------
            timeout : int
                Timeout in millisecond, default timeout is 1000(1s)

            Returns
            -------
            bool
                True if thread was started successfully
            )")
        .def("isReadThreadRunning", &I3DR::Phase::PylonStereoCamera::isReadThreadRunning, R"(
            Check if camera read thread is running

            Returns
            -------
            bool
                True if read thread is running
            )")
        .def("getReadThreadResult", &I3DR::Phase::PylonStereoCamera::getReadThreadResult, R"(
            Get results from threaded read process
            Should be used with startReadThread()

            Returns
            -------
            CameraReadResult
                Result from read
    
            )")
        .def("setReadThreadCallback", &I3DR::Phase::PylonStereoCamera::setReadThreadCallback, R"(
            Set callback function to run when read thread completes
            Should be used with startReadThread()
            Useful as an external trigger that read is complete
            and results can be retrieved.

            Parameters
            ----------
            f : callback

            )", py::arg("callback"))
        .def("startContinousReadThread", &I3DR::Phase::PylonStereoCamera::startContinousReadThread, py::arg("timeout") = 1000, R"(
            Start threaded process to read stereo images from cameras
            Thread will run continously until stopped
            This is useful for continuous image acquisition
            
            Parameters
            ----------
            timeout : int
                Timeout in millisecond, default timeout is 1000(1s)

            Returns
            -------
            bool
                Success of starting continous read thread
            )")
        .def("stopContinousReadThread", &I3DR::Phase::PylonStereoCamera::stopContinousReadThread, R"(
            Stop continous read thread

            )")
        .def("isContinousReadThreadRunning", &I3DR::Phase::PylonStereoCamera::isContinousReadThreadRunning, R"(
            Check if continous read thread is running
            Should be used with startContinousReadThread()
            
            Returns
            -------
            bool
                Continous read thread running status
            )")
        .def("getWidth", &I3DR::Phase::PylonStereoCamera::getWidth, R"(
            Get camera image width
            
            Returns
            -------
            value : int
                Camera image width
            )")
        .def("getHeight", &I3DR::Phase::PylonStereoCamera::getHeight, R"(
            Get camera image height
            
            Returns
            -------
            value : int
                Camera image height
            )")
        .def("getDownsampleFactor", &I3DR::Phase::PylonStereoCamera::getDownsampleFactor, R"(
            Get current downsample factor
            
            Returns
            -------
            value : float
                Downsample factor
            )")
        .def("enableDataCapture", &I3DR::Phase::PylonStereoCamera::enableDataCapture, R"(
            Enable/disable saving captured images to file
            Use with setDataCapturePath() to set path to save images

            Parameters
            ----------
            enable : bool
                Enable/disable saving images to file
            )", py::arg("enable"))
        .def("setDataCapturePath", &I3DR::Phase::PylonStereoCamera::setDataCapturePath, R"(
            Set path of saved directory for capture data

            path : str
                Directory of desired capture data storage
            )", py::arg("path"))
        .def("getCaptureCount", &I3DR::Phase::PylonStereoCamera::getCaptureCount, R"(
            Get number of frames captured since
            initalisation of the camera or last count reset
            Use with resetFrameCount() to reset frame count

            Returns
            -------
            value : int
                Number of frames captured
            )")
        .def("resetCaptureCount", &I3DR::Phase::PylonStereoCamera::resetCaptureCount, R"(
            Reset captured frame count to zero
            Use with getCaptureCount() to get number of frames captured

            )")
        .def("setLeftFlipX", &I3DR::Phase::PylonStereoCamera::setLeftFlipX, R"(
            Flip left image in x axis

            Parameters
            ----------
            enable : bool
                Set "True" to flip image
            )", py::arg("enable"))
        .def("setLeftFlipY", &I3DR::Phase::PylonStereoCamera::setLeftFlipY, R"(
            Flip left image in y axis

            Parameters
            ----------
            enable : bool
                Set "True" to flip image
            )", py::arg("enable"))
        .def("setRightFlipX", &I3DR::Phase::PylonStereoCamera::setRightFlipX, R"(
            Flip right image in x axis

            Parameters
            ----------
            enable : bool
                Set "True" to flip image
            )", py::arg("enable"))
        .def("setRightFlipY", &I3DR::Phase::PylonStereoCamera::setRightFlipY, R"(
            Flip right image in y axis

            Parameters
            ----------
            enable : bool
                Set "True" to flip image
            )", py::arg("enable"))
        .def("setDownsampleFactor", &I3DR::Phase::PylonStereoCamera::setDownsampleFactor, R"(
            Set downsample factor

            Parameters
            ----------
            value : float
                Downsample factor value
            )", py::arg("value"))
        .def("disconnect", &I3DR::Phase::PylonStereoCamera::disconnect, R"(
            Disconnect camera
    
            )");
}