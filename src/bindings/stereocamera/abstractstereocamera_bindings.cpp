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
    // All functions and variables of AbstractStereoCamera
    py::class_<I3DR::Phase::CameraReadResult>(m, "CameraReadResult", R"(
        Structure of CameraReadResult
        )")
        .def(py::init<bool,cv::Mat,cv::Mat>())
        .def_readwrite("valid", &I3DR::Phase::CameraReadResult::valid)
        .def_readwrite("left", &I3DR::Phase::CameraReadResult::left)
        .def_readwrite("right", &I3DR::Phase::CameraReadResult::right);
        
    py::class_<I3DR::Phase::AbstractStereoCamera>(m, "AbstractStereoCamera", R"(
            Variables contain camera data

            )")
        .def("connect", &I3DR::Phase::AbstractStereoCamera::connect, R"(
            Connect camera from reading CameraDeviceInfo
            
            )")
        .def("isConnected", &I3DR::Phase::AbstractStereoCamera::isConnected, R"(
            Check if camera is connected

            )")
        .def("startCapture", &I3DR::Phase::AbstractStereoCamera::startCapture, R"(
            To start camera communication
    
            )")
        .def("stopCapture", &I3DR::Phase::AbstractStereoCamera::stopCapture, R"(
            To stop camera communication

            )")
        .def("isCapturing", &I3DR::Phase::AbstractStereoCamera::isCapturing, R"(
            Check if camera is capturing

            )")
        .def("getFrameRate", &I3DR::Phase::AbstractStereoCamera::getFrameRate, R"(
            Get the value of frame rate

            )")
        .def("setExposure", &I3DR::Phase::AbstractStereoCamera::setExposure, R"(
            To overwrite the exposure value

            Parameters
            ----------

            value : int
                Input desired value of exposure
            )")
        .def("enableHardwareTrigger", &I3DR::Phase::AbstractStereoCamera::enableHardwareTrigger, R"(
            To enable camera trigger

            Parameters
            ----------

            enable : bool
                Set "True" to enable trigger
            )")
        .def("setFrameRate", &I3DR::Phase::AbstractStereoCamera::setFrameRate, R"(
            To overwrite the frame rate
            
            Parameters
            ----------
            value : float
                Input desired value of frame rate
            )")
        .def("setLeftAOI", &I3DR::Phase::AbstractStereoCamera::setLeftAOI, R"(
            To set a new area of interest for LEFT image
            
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
            To set a new area of interest for RIGHT image
            
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
            Read image from createStereoCamera

            Parameters
            ----------
            timeout : int
                timeout in millisecond, default timeout is 1000(1s)

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
                timeout in millisecond, default timeout is 1000(1s)

            Returns
            -------
            bool
                True if thread is reading
            )")
        .def("isReadThreadRunning", &I3DR::Phase::AbstractStereoCamera::isReadThreadRunning, R"(
            Check if camera thread is reading

            Returns
            -------
            bool
                True if thread is reading
            )")
        .def("getReadThreadResult", &I3DR::Phase::AbstractStereoCamera::getReadThreadResult, R"(
            Get the result of thread read
        
            )")
        .def("setReadThreadCallback", &I3DR::Phase::AbstractStereoCamera::setReadThreadCallback, R"(
            Set read thread callback from function read
        
            )")
        .def("startContinousReadThread", &I3DR::Phase::AbstractStereoCamera::startContinousReadThread, py::arg("timeout") = 1000, R"(
            Start read thread continuously
            
            Parameters
            ----------
            timeout : int
                timeout in millisecond, default timeout is 1000(1s)

            Returns
            -------
            bool
                True if thread is reading
            )")
        .def("stopContinousReadThread", &I3DR::Phase::AbstractStereoCamera::stopContinousReadThread, R"(
            Stop read thread continuously after startContinousReadThread

            )")
        .def("isContinousReadThreadRunning", &I3DR::Phase::AbstractStereoCamera::isContinousReadThreadRunning, R"(
            Check if thread is continuously reading
            
            Returns
            -------
            bool
                True if thread is reading
            )")
        .def("getWidth", &I3DR::Phase::AbstractStereoCamera::getWidth, R"(
            Get the width of image
            
            Returns
            -------
            value : int
                Width of image
            )")
        .def("getHeight", &I3DR::Phase::AbstractStereoCamera::getHeight, R"(
            Get the height of image
            
            Returns
            -------
            value : int
                Height of image
            )")
        .def("getDownsampleFactor", &I3DR::Phase::AbstractStereoCamera::getDownsampleFactor, R"(Get the value of Downsample Factor
            
            Returns
            -------
            value : float
                Downsampled factor
            )")
        .def("enableDataCapture", &I3DR::Phase::AbstractStereoCamera::enableDataCapture, R"(
            Enable data capture

            Parameters
            ----------
            enable : bool
                Set "True" to enable data capture
            )")
        .def("setDataCapturePath", &I3DR::Phase::AbstractStereoCamera::setDataCapturePath, R"(
            Set path of saved directory for capture data

            path : str
                directory of desired capture data storage
            )")
        .def("getCaptureCount", &I3DR::Phase::AbstractStereoCamera::getCaptureCount, R"(
            Get the capture count

            Returns
            -------
            value : int
                Value of capture count
            )")
        .def("resetCaptureCount", &I3DR::Phase::AbstractStereoCamera::resetCaptureCount, R"(
            Reset the capture count

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
            To overwrite the downsample factor

            Parameters
            ----------
            float : value
                Set desired downsample factor
            )")
        .def("disconnect", &I3DR::Phase::AbstractStereoCamera::disconnect, R"(
            Disconnect camera from reading CameraDeviceInfo

            )");

    //TODO add callback funtion for read results (https://pybind11.readthedocs.io/en/stable/advanced/cast/functional.html)

}