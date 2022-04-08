/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file uvcstereocamera_bindings.cpp
 * @brief UVC Stereo Camera class python bindings
 * @details Python bindings generated using pybind11
 */

#include"pybind11/pybind11.h"
#include "ndarray_converter.h"

#include <phase/stereocamera/uvcstereocamera.h>

namespace py = pybind11;

void init_uvcstereocamera(py::module_ &m) {
    NDArrayConverter::init_numpy();

    py::class_<I3DR::Phase::UVCStereoCamera>(m, "UVCStereoCamera")
        .def(py::init<I3DR::Phase::CameraDeviceInfo>())
        .def("connect", &I3DR::Phase::UVCStereoCamera::connect)
        .def("isConnected", &I3DR::Phase::UVCStereoCamera::isConnected)
        .def("startCapture", &I3DR::Phase::UVCStereoCamera::startCapture)
        .def("stopCapture", &I3DR::Phase::UVCStereoCamera::stopCapture)
        .def("isCapturing", &I3DR::Phase::UVCStereoCamera::isCapturing)
        .def("getFrameRate", &I3DR::Phase::UVCStereoCamera::getFrameRate)
        .def("setExposure", &I3DR::Phase::UVCStereoCamera::setExposure)
        .def("enableHardwareTrigger", &I3DR::Phase::UVCStereoCamera::enableHardwareTrigger)
        .def("setFrameRate", &I3DR::Phase::UVCStereoCamera::setFrameRate)
        .def("setLeftAOI", &I3DR::Phase::UVCStereoCamera::setLeftAOI)
        .def("setRightAOI", &I3DR::Phase::UVCStereoCamera::setRightAOI)
        .def("read", &I3DR::Phase::UVCStereoCamera::read, py::arg("timeout") = 1000)
        .def("setTestImagePaths", &I3DR::Phase::UVCStereoCamera::setTestImagePaths)
        .def("startReadThread", &I3DR::Phase::UVCStereoCamera::startReadThread, py::arg("timeout") = 1000)
        .def("isReadThreadRunning", &I3DR::Phase::UVCStereoCamera::isReadThreadRunning)
        .def("getReadThreadResult", &I3DR::Phase::UVCStereoCamera::getReadThreadResult)
        .def("startContinousReadThread", &I3DR::Phase::UVCStereoCamera::startContinousReadThread, py::arg("timeout") = 1000)
        .def("stopContinousReadThread", &I3DR::Phase::UVCStereoCamera::stopContinousReadThread)
        .def("isContinousReadThreadRunning", &I3DR::Phase::UVCStereoCamera::isContinousReadThreadRunning)
        .def("getWidth", &I3DR::Phase::UVCStereoCamera::getWidth)
        .def("getHeight", &I3DR::Phase::UVCStereoCamera::getHeight)
        .def("getDownsampleFactor", &I3DR::Phase::UVCStereoCamera::getDownsampleFactor)
        .def("enableDataCapture", &I3DR::Phase::UVCStereoCamera::enableDataCapture)
        .def("setDataCapturePath", &I3DR::Phase::UVCStereoCamera::setDataCapturePath)
        .def("getCaptureCount", &I3DR::Phase::UVCStereoCamera::getCaptureCount)
        .def("resetCaptureCount", &I3DR::Phase::UVCStereoCamera::resetCaptureCount)
        .def("setLeftFlipX", &I3DR::Phase::UVCStereoCamera::setLeftFlipX)
        .def("setLeftFlipY", &I3DR::Phase::UVCStereoCamera::setLeftFlipY)
        .def("setRightFlipX", &I3DR::Phase::UVCStereoCamera::setRightFlipX)
        .def("setRightFlipY", &I3DR::Phase::UVCStereoCamera::setRightFlipY)
        .def("setDownsampleFactor", &I3DR::Phase::UVCStereoCamera::setDownsampleFactor)
        .def("disconnect", &I3DR::Phase::UVCStereoCamera::disconnect);
}
