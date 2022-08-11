/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file phobosstereocamera_bindings.cpp
 * @brief Phobos Stereo Camera class python bindings
 * @details Python bindings generated using pybind11
 */

#include "pybind11/pybind11.h"
#include <pybind11/functional.h>
#include "ndarray_converter.h"

#include <phase/stereocamera/phobosstereocamera.h>

namespace py = pybind11;

void init_phobosstereocamera(py::module_ &m) {
    NDArrayConverter::init_numpy();
    // All functions and variables of PhobosStereoCamera
    py::class_<I3DR::Phase::PhobosStereoCamera>(m, "PhobosStereoCamera", R"(
            Variables contain Phobos camera data

            )")
        .def(py::init<I3DR::Phase::CameraDeviceInfo>(), R"(
            Variable stored unique camera information

            Parameters
            ----------

            left_serial     : str
                Camera left serial ID
            right_serial    : str
                Camera right serial ID
            unique_serial   : str
                Camera unique serial ID
            device_type     : enum
                enum of device type, according to the type of camera
            interface_type  : enum
                enum of interface type, according to the type of camera connection
            )")
        .def("connect", &I3DR::Phase::PhobosStereoCamera::connect, R"(
            Connect camera from reading CameraDeviceInfo

            )")
        .def("isConnected", &I3DR::Phase::PhobosStereoCamera::isConnected, R"(
            Check if camera is connected

            )")
        .def("startCapture", &I3DR::Phase::PhobosStereoCamera::startCapture, R"(
            To start camera communication

            )")
        .def("stopCapture", &I3DR::Phase::PhobosStereoCamera::stopCapture, R"(
            To stop camera communication
            
            )")
        .def("isCapturing", &I3DR::Phase::PhobosStereoCamera::isCapturing, R"(
            Check if camera is capturing
            
            )")
        .def("getFrameRate", &I3DR::Phase::PhobosStereoCamera::getFrameRate, R"(
            Get the value of frame rate

            )")
        .def("setExposure", &I3DR::Phase::PhobosStereoCamera::setExposure, R"(
            To overwrite the exposure value

            Parameters
            ----------

            value : int
                Input desired value of exposure
            )")
        .def("enableHardwareTrigger", &I3DR::Phase::PhobosStereoCamera::enableHardwareTrigger, R"(
            To enable camera trigger

            Parameters
            ----------

            enable : bool
                Set "True" to enable trigger
            )")
        .def("setFrameRate", &I3DR::Phase::PhobosStereoCamera::setFrameRate, R"(
            To overwrite the frame rate
            
            Parameters
            ----------
            value : float
                Input desired value of frame rate
            )")
        .def("setLeftAOI", &I3DR::Phase::PhobosStereoCamera::setLeftAOI, R"(
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
        .def("setRightAOI", &I3DR::Phase::PhobosStereoCamera::setRightAOI, R"(
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
        .def("read", &I3DR::Phase::PhobosStereoCamera::read, py::arg("timeout") = 1000, R"(
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
        .def("setTestImagePaths", &I3DR::Phase::PhobosStereoCamera::setTestImagePaths, R"(
            Set the path for test images, input both left and right image path

            Parameters
            ----------
            left_test_image_path    : str
            right_test_image_path   : str
            )")
        .def("startReadThread", &I3DR::Phase::PhobosStereoCamera::startReadThread, py::arg("timeout") = 1000, R"(
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
        .def("isReadThreadRunning", &I3DR::Phase::PhobosStereoCamera::isReadThreadRunning, R"(
            Check if camera thread is reading

            Returns
            -------
            bool
                True if thread is reading
            )")
        .def("getReadThreadResult", &I3DR::Phase::PhobosStereoCamera::getReadThreadResult, R"(
            Get the result of thread read
        
            )")
        .def("setReadThreadCallback", &I3DR::Phase::PhobosStereoCamera::setReadThreadCallback, R"(
            Set read thread callback from function read

            )")
        .def("startContinousReadThread", &I3DR::Phase::PhobosStereoCamera::startContinousReadThread, py::arg("timeout") = 1000, R"(
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
        .def("stopContinousReadThread", &I3DR::Phase::PhobosStereoCamera::stopContinousReadThread, R"(
            Stop read thread continuously after startContinousReadThread

            )")
        .def("isContinousReadThreadRunning", &I3DR::Phase::PhobosStereoCamera::isContinousReadThreadRunning, R"(
            Check if thread is continuously reading
            
            Returns
            -------
            bool
                True if thread is reading
            )")
        .def("getWidth", &I3DR::Phase::PhobosStereoCamera::getWidth, R"(
            Get the width of Phobos image
            
            Returns
            -------
            value : int
                Width of Phobos image
            )")
        .def("getHeight", &I3DR::Phase::PhobosStereoCamera::getHeight, R"(
            Get the height of Phobos image
            
            Returns
            -------
            value : int
                Height of Phobos image
            )")
        .def("getDownsampleFactor", &I3DR::Phase::PhobosStereoCamera::getDownsampleFactor, R"(
            Get the value of Downsample Factor
            
            Returns
            -------
            value : float
                Downsampled factor
            )")
        .def("enableDataCapture", &I3DR::Phase::PhobosStereoCamera::enableDataCapture, R"(
            Enable data capture

            Parameters
            ----------
            enable : bool
                Set "True" to enable data capture
            )")
        .def("setDataCapturePath", &I3DR::Phase::PhobosStereoCamera::setDataCapturePath, R"(
            Set path of saved directory for capture data

            path : str
                directory of desired capture data storage
            )")
        .def("getCaptureCount", &I3DR::Phase::PhobosStereoCamera::getCaptureCount, R"(
            Get the capture count

            Returns
            -------
            value : int
                Value of capture count
            )")
        .def("resetCaptureCount", &I3DR::Phase::PhobosStereoCamera::resetCaptureCount, R"(
            Reset the capture count

            )")
        .def("setLeftFlipX", &I3DR::Phase::PhobosStereoCamera::setLeftFlipX, R"(
            Flip left image in x axis

            Parameters
            ----------
            enable : bool
                Set "True" to flip image
            )")
        .def("setLeftFlipY", &I3DR::Phase::PhobosStereoCamera::setLeftFlipY, R"(
            Flip left image in y axis

            Parameters
            ----------
            enable : bool
                Set "True" to flip image
            )")
        .def("setRightFlipX", &I3DR::Phase::PhobosStereoCamera::setRightFlipX, R"(
            Flip right image in x axis

            Parameters
            ----------
            enable : bool
                Set "True" to flip image
            )")
        .def("setRightFlipY", &I3DR::Phase::PhobosStereoCamera::setRightFlipY, R"(
            Flip right image in y axis

            Parameters
            ----------
            enable : bool
                Set "True" to flip image
            )")
        .def("setDownsampleFactor", &I3DR::Phase::PhobosStereoCamera::setDownsampleFactor, R"(
            To overwrite the downsample factor

            Parameters
            ----------
            float : value
                Set desired downsample factor
            )")
        .def("disconnect", &I3DR::Phase::PhobosStereoCamera::disconnect, R"(
            Disconnect camera from reading CameraDeviceInfo

            )");

}