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

    py::class_<I3DR::Phase::PhobosStereoCamera>(m, "PhobosStereoCamera")
        .def(py::init<I3DR::Phase::CameraDeviceInfo>())
        .def("connect", &I3DR::Phase::PhobosStereoCamera::connect)
        .def("isConnected", &I3DR::Phase::PhobosStereoCamera::isConnected)
        .def("startCapture", &I3DR::Phase::PhobosStereoCamera::startCapture)
        .def("stopCapture", &I3DR::Phase::PhobosStereoCamera::stopCapture)
        .def("isCapturing", &I3DR::Phase::PhobosStereoCamera::isCapturing)
        .def("getFrameRate", &I3DR::Phase::PhobosStereoCamera::getFrameRate)
        .def("setExposure", &I3DR::Phase::PhobosStereoCamera::setExposure)
        .def("enableHardwareTrigger", &I3DR::Phase::PhobosStereoCamera::enableHardwareTrigger)
        .def("setFrameRate", &I3DR::Phase::PhobosStereoCamera::setFrameRate)
        .def("setLeftAOI", &I3DR::Phase::PhobosStereoCamera::setLeftAOI)
        .def("setRightAOI", &I3DR::Phase::PhobosStereoCamera::setRightAOI)
        .def("read", &I3DR::Phase::PhobosStereoCamera::read, py::arg("timeout") = 1000)
        .def("setTestImagePaths", &I3DR::Phase::PhobosStereoCamera::setTestImagePaths)
        .def("startReadThread", &I3DR::Phase::PhobosStereoCamera::startReadThread, py::arg("timeout") = 1000)
        .def("isReadThreadRunning", &I3DR::Phase::PhobosStereoCamera::isReadThreadRunning)
        .def("getReadThreadResult", &I3DR::Phase::PhobosStereoCamera::getReadThreadResult)
        .def("setReadThreadCallback", &I3DR::Phase::PhobosStereoCamera::setReadThreadCallback)
        .def("startContinousReadThread", &I3DR::Phase::PhobosStereoCamera::startContinousReadThread, py::arg("timeout") = 1000)
        .def("stopContinousReadThread", &I3DR::Phase::PhobosStereoCamera::stopContinousReadThread)
        .def("isContinousReadThreadRunning", &I3DR::Phase::PhobosStereoCamera::isContinousReadThreadRunning)
        .def("getWidth", &I3DR::Phase::PhobosStereoCamera::getWidth)
        .def("getHeight", &I3DR::Phase::PhobosStereoCamera::getHeight)
        .def("getDownsampleFactor", &I3DR::Phase::PhobosStereoCamera::getDownsampleFactor)
        .def("enableDataCapture", &I3DR::Phase::PhobosStereoCamera::enableDataCapture)
        .def("setDataCapturePath", &I3DR::Phase::PhobosStereoCamera::setDataCapturePath)
        .def("getCaptureCount", &I3DR::Phase::PhobosStereoCamera::getCaptureCount)
        .def("resetCaptureCount", &I3DR::Phase::PhobosStereoCamera::resetCaptureCount)
        .def("setLeftFlipX", &I3DR::Phase::PhobosStereoCamera::setLeftFlipX)
        .def("setLeftFlipY", &I3DR::Phase::PhobosStereoCamera::setLeftFlipY)
        .def("setRightFlipX", &I3DR::Phase::PhobosStereoCamera::setRightFlipX)
        .def("setRightFlipY", &I3DR::Phase::PhobosStereoCamera::setRightFlipY)
        .def("setDownsampleFactor", &I3DR::Phase::PhobosStereoCamera::setDownsampleFactor)
        .def("disconnect", &I3DR::Phase::PhobosStereoCamera::disconnect);

}