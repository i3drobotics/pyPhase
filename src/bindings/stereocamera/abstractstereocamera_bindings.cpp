/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file abstractstereocamera_bindings.cpp
 * @brief Abstract Stereo Camera class python bindings
 * @details Python bindings generated using pybind11
 */

#include"pybind11/pybind11.h"
#include "ndarray_converter.h"

#include <phase/stereocamera/abstractstereocamera.h>

namespace py = pybind11;

void init_abstractstereocamera(py::module_ &m) {
    NDArrayConverter::init_numpy();

    py::class_<I3DR::Phase::AbstractStereoCamera>(m, "AbstractStereoCamera")
        .def("connect", &I3DR::Phase::AbstractStereoCamera::connect)
        .def("isConnected", &I3DR::Phase::AbstractStereoCamera::isConnected)
        .def("startCapture", &I3DR::Phase::AbstractStereoCamera::startCapture)
        .def("stopCapture", &I3DR::Phase::AbstractStereoCamera::stopCapture)
        .def("isCapturing", &I3DR::Phase::AbstractStereoCamera::isCapturing)
        .def("getFrameRate", &I3DR::Phase::AbstractStereoCamera::getFrameRate)
        .def("setExposure", &I3DR::Phase::AbstractStereoCamera::setExposure)
        .def("enableHardwareTrigger", &I3DR::Phase::AbstractStereoCamera::enableHardwareTrigger)
        .def("setFrameRate", &I3DR::Phase::AbstractStereoCamera::setFrameRate)
        .def("setLeftAOI", &I3DR::Phase::AbstractStereoCamera::setLeftAOI)
        .def("setRightAOI", &I3DR::Phase::AbstractStereoCamera::setRightAOI)
        .def("read", &I3DR::Phase::AbstractStereoCamera::read, py::arg("timeout") = 1000)
        .def("setTestImagePaths", &I3DR::Phase::AbstractStereoCamera::setTestImagePaths)
        .def("startReadThread", &I3DR::Phase::AbstractStereoCamera::startReadThread, py::arg("timeout") = 1000)
        .def("isReadThreadRunning", &I3DR::Phase::AbstractStereoCamera::isReadThreadRunning)
        .def("getReadThreadResult", &I3DR::Phase::AbstractStereoCamera::getReadThreadResult)
        .def("startContinousReadThread", &I3DR::Phase::AbstractStereoCamera::startContinousReadThread, py::arg("timeout") = 1000)
        .def("stopContinousReadThread", &I3DR::Phase::AbstractStereoCamera::stopContinousReadThread)
        .def("isContinousReadThreadRunning", &I3DR::Phase::AbstractStereoCamera::isContinousReadThreadRunning)
        .def("getWidth", &I3DR::Phase::AbstractStereoCamera::getWidth)
        .def("getHeight", &I3DR::Phase::AbstractStereoCamera::getHeight)
        .def("getDownsampleFactor", &I3DR::Phase::AbstractStereoCamera::getDownsampleFactor)
        .def("enableDataCapture", &I3DR::Phase::AbstractStereoCamera::enableDataCapture)
        .def("setDataCapturePath", &I3DR::Phase::AbstractStereoCamera::setDataCapturePath)
        .def("getCaptureCount", &I3DR::Phase::AbstractStereoCamera::getCaptureCount)
        .def("resetCaptureCount", &I3DR::Phase::AbstractStereoCamera::resetCaptureCount)
        .def("setLeftFlipX", &I3DR::Phase::AbstractStereoCamera::setLeftFlipX)
        .def("setLeftFlipY", &I3DR::Phase::AbstractStereoCamera::setLeftFlipY)
        .def("setRightFlipX", &I3DR::Phase::AbstractStereoCamera::setRightFlipX)
        .def("setRightFlipY", &I3DR::Phase::AbstractStereoCamera::setRightFlipY)
        .def("setDownsampleFactor", &I3DR::Phase::AbstractStereoCamera::setDownsampleFactor)
        .def("disconnect", &I3DR::Phase::AbstractStereoCamera::disconnect);

    //TODO add callback funtion for read results (https://pybind11.readthedocs.io/en/stable/advanced/cast/functional.html)

}