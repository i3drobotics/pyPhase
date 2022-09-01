/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file abstractstereocamera_bindings.cpp
 * @brief Abstract Stereo Camera class python bindings
 * @details Python bindings generated using pybind11
 */

#include "pybind11/pybind11.h"
#include <pybind11/functional.h>
#include "ndarray_converter.h"

#include <phase/stereocamera/abstractstereocamera.h>

namespace py = pybind11;

void init_abstractstereocamera(py::module_ &m) {
    NDArrayConverter::init_numpy();

    py::class_<I3DR::Phase::CameraReadResult>(m, "CameraReadResult", R"(
        Struture to store the result from reading a camera frame. Used in the stereo camera classes.
        )")
        .def(py::init<bool,cv::Mat,cv::Mat>())
        .def_readwrite("valid", &I3DR::Phase::CameraReadResult::valid)
        .def_readwrite("left", &I3DR::Phase::CameraReadResult::left)
        .def_readwrite("right", &I3DR::Phase::CameraReadResult::right);

    // All functions and variables of AbstractStereoCamera
    py::class_<I3DR::Phase::AbstractStereoCamera>(m, "AbstractStereoCamera", R"(
            Abstract base class for building stereo camera
            classes. Includes functions/structures common across
            all stereo cameras.

            )")
        .def("connect", &I3DR::Phase::AbstractStereoCamera::connect, R"(
            Connect to camera
            
            )")
        .def("isConnected", &I3DR::Phase::AbstractStereoCamera::isConnected, R"(
            Check if camera is connected

            )")
        .def("startCapture", &I3DR::Phase::AbstractStereoCamera::startCapture, R"(
            Start stereo camera capture
            Must be started before read() is called
    
            )")
        .def("stopCapture", &I3DR::Phase::AbstractStereoCamera::stopCapture, R"(
            Stop stereo camera capture
            Will no longer be able to read() after this is called

            )")
        .def("isCapturing", &I3DR::Phase::AbstractStereoCamera::isCapturing, R"(
            Check if camera is capturing

            )")
        .def("getFrameRate", &I3DR::Phase::AbstractStereoCamera::getFrameRate, R"(
            Get the value of frame rate

            )")
        .def("setExposure", &I3DR::Phase::AbstractStereoCamera::setExposure, R"(
            Set exposure value of camera

            Parameters
            ----------

            value : int
                Value of exposure (us)
            )")
        .def("enableHardwareTrigger", &I3DR::Phase::AbstractStereoCamera::enableHardwareTrigger, R"(
            Enable camera hardware trigger

            Parameters
            ----------

            enable : bool
                Set "True" to enable hardware trigger
            )")
        .def("setFrameRate", &I3DR::Phase::AbstractStereoCamera::setFrameRate, R"(
            Set frame rate of camera
            
            Parameters
            ----------
            value : float
                Value of frame rate
            )")
        .def("setLeftAOI", &I3DR::Phase::AbstractStereoCamera::setLeftAOI, R"(
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
        .def("setRightAOI", &I3DR::Phase::AbstractStereoCamera::setRightAOI, R"(
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
        .def("read", &I3DR::Phase::AbstractStereoCamera::read, py::arg("timeout") = 1000, R"(
            Read image frame from camera

            Parameters
            ----------
            timeout : int
                Timeout in millisecond, default timeout is 1000(1s)

            Returns
            -------
            left : numpy.ndarray, right : numpy.ndarray
                Return stereo images left, right
            )")
        .def("setTestImagePaths", &I3DR::Phase::AbstractStereoCamera::setTestImagePaths, R"(
            Set the path for test images, input both left and right image path

            Parameters
            ----------
            left_test_image_path    : str
            right_test_image_path   : str
            )")
        .def("startReadThread", &I3DR::Phase::AbstractStereoCamera::startReadThread, py::arg("timeout") = 1000, R"(
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
        .def("isReadThreadRunning", &I3DR::Phase::AbstractStereoCamera::isReadThreadRunning, R"(
            Check if camera read thread is running

            Returns
            -------
            bool
                True if read thread is running
            )")
        .def("getReadThreadResult", &I3DR::Phase::AbstractStereoCamera::getReadThreadResult, R"(
            Get results from threaded read process
            Should be used with startReadThread()

            Returns
            -------
            CameraReadResult
                Result from read
        
            )")
        .def("setReadThreadCallback", &I3DR::Phase::AbstractStereoCamera::setReadThreadCallback, R"(
            Set callback function to run when read thread completes
            Should be used with startReadThread()
            Useful as an external trigger that read is complete
            and results can be retrieved.

            Parameters
            ----------
            f : callback
        
            )")
        .def("startContinousReadThread", &I3DR::Phase::AbstractStereoCamera::startContinousReadThread, py::arg("timeout") = 1000, R"(
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
        .def("stopContinousReadThread", &I3DR::Phase::AbstractStereoCamera::stopContinousReadThread, R"(
            Stop continous read thread

            )")
        .def("isContinousReadThreadRunning", &I3DR::Phase::AbstractStereoCamera::isContinousReadThreadRunning, R"(
            Check if continous read thread is running
            Should be used with startContinousReadThread()
            
            Returns
            -------
            bool
                Continous read thread running status
            )")
        .def("getWidth", &I3DR::Phase::AbstractStereoCamera::getWidth, R"(
            Get camera image width
            
            Returns
            -------
            value : int
                Camera image width
            )")
        .def("getHeight", &I3DR::Phase::AbstractStereoCamera::getHeight, R"(
            Get camera image height
            
            Returns
            -------
            value : int
                Camera image height
            )")
        .def("getDownsampleFactor", &I3DR::Phase::AbstractStereoCamera::getDownsampleFactor, R"(Get the value of Downsample Factor
            Get current downsample factor
            
            Returns
            -------
            value : float
                Downsample factor
            )")
        .def("enableDataCapture", &I3DR::Phase::AbstractStereoCamera::enableDataCapture, R"(
            Enable/disable saving captured images to file
            Use with setDataCapturePath() to set path to save images

            Parameters
            ----------
            enable : bool
                Enable/disable saving images to file
            )")
        .def("setDataCapturePath", &I3DR::Phase::AbstractStereoCamera::setDataCapturePath, R"(
            Set data capture path to save images
            Use with enableDataCapture() to toggle saving images to file

            path : str
                Directory of desired storage of captured data
            )")
        .def("getCaptureCount", &I3DR::Phase::AbstractStereoCamera::getCaptureCount, R"(
            Get number of frames captured since
            initalisation of the camera or last count reset
            Use with resetFrameCount() to reset frame count

            Returns
            -------
            value : int
                Number of frames captured
            )")
        .def("resetCaptureCount", &I3DR::Phase::AbstractStereoCamera::resetCaptureCount, R"(
            Reset captured frame count to zero
            Use with getCaptureCount() to get number of frames captured

            )")
        .def("setLeftFlipX", &I3DR::Phase::AbstractStereoCamera::setLeftFlipX, R"(
            Flip left image in x axis

            Parameters
            ----------
            enable : bool
                Set "True" to flip image
            )")
        .def("setLeftFlipY", &I3DR::Phase::AbstractStereoCamera::setLeftFlipY, R"(
            Flip left image in y axis

            Parameters
            ----------
            enable : bool
                Set "True" to flip image
            )")
        .def("setRightFlipX", &I3DR::Phase::AbstractStereoCamera::setRightFlipX, R"(
            Flip right image in x axis

            Parameters
            ----------
            enable : bool
                Set "True" to flip image
            )")
        .def("setRightFlipY", &I3DR::Phase::AbstractStereoCamera::setRightFlipY, R"(
            Flip right image in y axis

            Parameters
            ----------
            enable : bool
                Set "True" to flip image
            )")
        .def("setDownsampleFactor", &I3DR::Phase::AbstractStereoCamera::setDownsampleFactor, R"(
            Set downsample factor

            Parameters
            ----------
            float : value
                Downsample factor value
            )")
        .def("disconnect", &I3DR::Phase::AbstractStereoCamera::disconnect, R"(
            Disconnect camera

            )");

}