/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file uvcstereocamera_bindings.cpp
 * @brief UVC Stereo Camera class python bindings
 * @details Python bindings generated using pybind11
 */

#include "pybind11/pybind11.h"
#include <pybind11/functional.h>
#include "ndarray_converter.h"

#include <phase/stereocamera/uvcstereocamera.h>

namespace py = pybind11;

void init_uvcstereocamera(py::module_ &m) {
    NDArrayConverter::init_numpy();
    // All functions and variables of UVCStereoCamera
    py::class_<I3DR::Phase::UVCStereoCamera>(m, "UVCStereoCamera", R"(
            UVC Stereo Camera class
            Capture data from a stereo camera using UVC cameras
            where left and right is transported via green and red channels.

            )")
        .def(py::init<I3DR::Phase::CameraDeviceInfo>(), R"(
            Initalise Stereo Camera with the given device_info.

            Parameters
            ----------

            device_info     : CameraDeviceInfo
                Camera device information to use when initalising camera
            )")
        .def("connect", &I3DR::Phase::UVCStereoCamera::connect, R"(
            Connect to camera
    
            )")
        .def("isConnected", &I3DR::Phase::UVCStereoCamera::isConnected, R"(
            Check if camera is connected
    
            )")
        .def("startCapture", &I3DR::Phase::UVCStereoCamera::startCapture, R"(
            Start stereo camera capture
            Must be started before read() is called
    
            )")
        .def("stopCapture", &I3DR::Phase::UVCStereoCamera::stopCapture, R"(
            Stop stereo camera capture
            Will no longer be able to read() after this is called

            )")
        .def("isCapturing", &I3DR::Phase::UVCStereoCamera::isCapturing, R"(
            Check if camera is capturing
    
            )")
        .def("getFrameRate", &I3DR::Phase::UVCStereoCamera::getFrameRate, R"(
            Get the value of frame rate
    
            )")
        .def("setExposure", &I3DR::Phase::UVCStereoCamera::setExposure, R"(
            Set exposure value of camera

            Parameters
            ----------

            value : int
                Value of exposure (us)
            )")
        .def("enableHardwareTrigger", &I3DR::Phase::UVCStereoCamera::enableHardwareTrigger, R"(
            Enable camera hardware trigger

            Parameters
            ----------

            enable : bool
                Set "True" to enable hardware trigger
            )")
        .def("setFrameRate", &I3DR::Phase::UVCStereoCamera::setFrameRate, R"(
            Set frame rate of camera
            
            Parameters
            ----------
            value : float
                Value of frame rate
            )")
        .def("setLeftAOI", &I3DR::Phase::UVCStereoCamera::setLeftAOI, R"(
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
            )")
        .def("setRightAOI", &I3DR::Phase::UVCStereoCamera::setRightAOI, R"(
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
            )")
        .def("read", &I3DR::Phase::UVCStereoCamera::read, py::arg("timeout") = 1000, R"(
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
        .def("setTestImagePaths", &I3DR::Phase::UVCStereoCamera::setTestImagePaths, R"(
            Set the path for test images, input both left and right image path

            Parameters
            ----------
            left_test_image_path    : str
            right_test_image_path   : str
            )")
        .def("startReadThread", &I3DR::Phase::UVCStereoCamera::startReadThread, py::arg("timeout") = 1000, R"(
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
        .def("isReadThreadRunning", &I3DR::Phase::UVCStereoCamera::isReadThreadRunning, R"(
            Check if camera read thread is running

            Returns
            -------
            bool
                True if read thread is running
            )")
        .def("getReadThreadResult", &I3DR::Phase::UVCStereoCamera::getReadThreadResult, R"(
            Get results from threaded read process
            Should be used with startReadThread()

            Returns
            -------
            CameraReadResult
                Result from read
    
            )")
        .def("setReadThreadCallback", &I3DR::Phase::UVCStereoCamera::setReadThreadCallback, R"(
            Set callback function to run when read thread completes
            Should be used with startReadThread()
            Useful as an external trigger that read is complete
            and results can be retrieved.

            Parameters
            ----------
            f : callback

            )")
        .def("startContinousReadThread", &I3DR::Phase::UVCStereoCamera::startContinousReadThread, py::arg("timeout") = 1000, R"(
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
        .def("stopContinousReadThread", &I3DR::Phase::UVCStereoCamera::stopContinousReadThread, R"(
            Stop continous read thread
    
            )")
        .def("isContinousReadThreadRunning", &I3DR::Phase::UVCStereoCamera::isContinousReadThreadRunning, R"(
            Check if continous read thread is running
            Should be used with startContinousReadThread()
            
            Returns
            -------
            bool
                Continous read thread running status
            )")
        .def("getWidth", &I3DR::Phase::UVCStereoCamera::getWidth, R"(
            Get camera image width
            
            Returns
            -------
            value : int
                Camera image width
            )")
        .def("getHeight", &I3DR::Phase::UVCStereoCamera::getHeight, R"(
            Get camera image height
            
            Returns
            -------
            value : int
                Camera image height
            )")
        .def("getDownsampleFactor", &I3DR::Phase::UVCStereoCamera::getDownsampleFactor, R"(
            Get current downsample factor
            
            Returns
            -------
            value : float
                Downsample factor
            )")
        .def("enableDataCapture", &I3DR::Phase::UVCStereoCamera::enableDataCapture, R"(
            Enable/disable saving captured images to file
            Use with setDataCapturePath() to set path to save images

            Parameters
            ----------
            enable : bool
                Enable/disable saving images to file
            )")
        .def("setDataCapturePath", &I3DR::Phase::UVCStereoCamera::setDataCapturePath, R"(
            Set data capture path to save images
            Use with enableDataCapture() to toggle saving images to file

            path : str
                Directory of desired capture data storage
            )")
        .def("getCaptureCount", &I3DR::Phase::UVCStereoCamera::getCaptureCount, R"(
            Get number of frames captured since
            initalisation of the camera or last count reset
            Use with resetFrameCount() to reset frame count

            Returns
            -------
            value : int
                Number of frames captured
            )")
        .def("resetCaptureCount", &I3DR::Phase::UVCStereoCamera::resetCaptureCount, R"(
            Reset captured frame count to zero
            Use with getCaptureCount() to get number of frames captured

            )")
        .def("setLeftFlipX", &I3DR::Phase::UVCStereoCamera::setLeftFlipX, R"(
            Flip left image in x axis

            Parameters
            ----------
            enable : bool
                Set "True" to flip image
            )")
        .def("setLeftFlipY", &I3DR::Phase::UVCStereoCamera::setLeftFlipY, R"(
            Flip left image in y axis

            Parameters
            ----------
            enable : bool
                Set "True" to flip image
            )")
        .def("setRightFlipX", &I3DR::Phase::UVCStereoCamera::setRightFlipX, R"(
            Flip right image in x axis

            Parameters
            ----------
            enable : bool
                Set "True" to flip image
            )")
        .def("setRightFlipY", &I3DR::Phase::UVCStereoCamera::setRightFlipY, R"(
            Flip right image in y axis

            Parameters
            ----------
            enable : bool
                Set "True" to flip image
            )")
        .def("setDownsampleFactor", &I3DR::Phase::UVCStereoCamera::setDownsampleFactor, R"(
            Set downsample factor

            Parameters
            ----------
            float : value
                Downsample factor value
            )")
        .def("disconnect", &I3DR::Phase::UVCStereoCamera::disconnect, R"(
            Disconnect camera

            )");
}
