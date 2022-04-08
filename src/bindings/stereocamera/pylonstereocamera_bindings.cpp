/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file pylonstereocamera_bindings.cpp
 * @brief Pylon Stereo Camera class python bindings
 * @details Python bindings generated using pybind11
 */

#include"pybind11/pybind11.h"
#include "ndarray_converter.h"

#include <phase/stereocamera/pylonstereocamera.h>

namespace py = pybind11;

void init_pylonstereocamera(py::module_ &m) {
    NDArrayConverter::init_numpy();

    py::class_<I3DR::Phase::PylonStereoCamera>(m, "PylonStereoCamera")
        .def(py::init<I3DR::Phase::CameraDeviceInfo>())
        .def("connect", &I3DR::Phase::PylonStereoCamera::connect)
        .def("isConnected", &I3DR::Phase::PylonStereoCamera::isConnected)
        .def("startCapture", &I3DR::Phase::PylonStereoCamera::startCapture)
        .def("stopCapture", &I3DR::Phase::PylonStereoCamera::stopCapture)
        .def("isCapturing", &I3DR::Phase::PylonStereoCamera::isCapturing)
        .def("getFrameRate", &I3DR::Phase::PylonStereoCamera::getFrameRate)
        .def("setExposure", &I3DR::Phase::PylonStereoCamera::setExposure)
        .def("enableHardwareTrigger", &I3DR::Phase::PylonStereoCamera::enableHardwareTrigger)
        .def("setFrameRate", &I3DR::Phase::PylonStereoCamera::setFrameRate)
        .def("setLeftAOI", &I3DR::Phase::PylonStereoCamera::setLeftAOI)
        .def("setRightAOI", &I3DR::Phase::PylonStereoCamera::setRightAOI)
        .def("read", &I3DR::Phase::PylonStereoCamera::read, py::arg("timeout") = 1000)
        .def("setTestImagePaths", &I3DR::Phase::PylonStereoCamera::setTestImagePaths)
        .def("startReadThread", &I3DR::Phase::PylonStereoCamera::startReadThread, py::arg("timeout") = 1000)
        .def("isReadThreadRunning", &I3DR::Phase::PylonStereoCamera::isReadThreadRunning)
        .def("getReadThreadResult", &I3DR::Phase::PylonStereoCamera::getReadThreadResult)
        .def("setReadThreadCallback", &I3DR::Phase::PylonStereoCamera::setReadThreadCallback)
        .def("startContinousReadThread", &I3DR::Phase::PylonStereoCamera::startContinousReadThread, py::arg("timeout") = 1000)
        .def("stopContinousReadThread", &I3DR::Phase::PylonStereoCamera::stopContinousReadThread)
        .def("isContinousReadThreadRunning", &I3DR::Phase::PylonStereoCamera::isContinousReadThreadRunning)
        .def("getWidth", &I3DR::Phase::PylonStereoCamera::getWidth)
        .def("getHeight", &I3DR::Phase::PylonStereoCamera::getHeight)
        .def("getDownsampleFactor", &I3DR::Phase::PylonStereoCamera::getDownsampleFactor)
        .def("enableDataCapture", &I3DR::Phase::PylonStereoCamera::enableDataCapture)
        .def("setDataCapturePath", &I3DR::Phase::PylonStereoCamera::setDataCapturePath)
        .def("getCaptureCount", &I3DR::Phase::PylonStereoCamera::getCaptureCount)
        .def("resetCaptureCount", &I3DR::Phase::PylonStereoCamera::resetCaptureCount)
        .def("setLeftFlipX", &I3DR::Phase::PylonStereoCamera::setLeftFlipX)
        .def("setLeftFlipY", &I3DR::Phase::PylonStereoCamera::setLeftFlipY)
        .def("setRightFlipX", &I3DR::Phase::PylonStereoCamera::setRightFlipX)
        .def("setRightFlipY", &I3DR::Phase::PylonStereoCamera::setRightFlipY)
        .def("setDownsampleFactor", &I3DR::Phase::PylonStereoCamera::setDownsampleFactor)
        .def("disconnect", &I3DR::Phase::PylonStereoCamera::disconnect);
}