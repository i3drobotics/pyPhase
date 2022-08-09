/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file deimosstereocamera_bindings.cpp
 * @brief Deimos Stereo Camera class python bindings
 * @details Python bindings generated using pybind11
 */


#include "pybind11/pybind11.h"
#include <pybind11/functional.h>
#include "ndarray_converter.h"

#include <phase/stereocamera/deimosstereocamera.h>

namespace py = pybind11;

void init_deimosstereocamera(py::module_ &m) {
    NDArrayConverter::init_numpy();
    //TODOC Description of the class and functions in DeimosStereoCamera class
    py::class_<I3DR::Phase::DeimosStereoCamera>(m, "DeimosStereoCamera", R"(TODOC)")
        .def(py::init<I3DR::Phase::CameraDeviceInfo>(), R"(TODOC)")
        .def("connect", &I3DR::Phase::DeimosStereoCamera::connect, R"(TODOC)")
        .def("isConnected", &I3DR::Phase::DeimosStereoCamera::isConnected, R"(TODOC)")
        .def("startCapture", &I3DR::Phase::DeimosStereoCamera::startCapture, R"(TODOC)")
        .def("stopCapture", &I3DR::Phase::DeimosStereoCamera::stopCapture, R"(TODOC)")
        .def("isCapturing", &I3DR::Phase::DeimosStereoCamera::isCapturing, R"(TODOC)")
        .def("getFrameRate", &I3DR::Phase::DeimosStereoCamera::getFrameRate, R"(TODOC)")
        .def("setExposure", &I3DR::Phase::DeimosStereoCamera::setExposure, R"(TODOC)")
        .def("enableHardwareTrigger", &I3DR::Phase::DeimosStereoCamera::enableHardwareTrigger, R"(TODOC)")
        .def("setFrameRate", &I3DR::Phase::DeimosStereoCamera::setFrameRate, R"(TODOC)")
        .def("setLeftAOI", &I3DR::Phase::DeimosStereoCamera::setLeftAOI, R"(TODOC)")
        .def("setRightAOI", &I3DR::Phase::DeimosStereoCamera::setRightAOI, R"(TODOC)")
        .def("read", &I3DR::Phase::DeimosStereoCamera::read, py::arg("timeout") = 1000, R"(TODOC)")
        .def("setTestImagePaths", &I3DR::Phase::DeimosStereoCamera::setTestImagePaths, R"(TODOC)")
        .def("startReadThread", &I3DR::Phase::DeimosStereoCamera::startReadThread, py::arg("timeout") = 1000, R"(TODOC)")
        .def("isReadThreadRunning", &I3DR::Phase::DeimosStereoCamera::isReadThreadRunning, R"(TODOC)")
        .def("getReadThreadResult", &I3DR::Phase::DeimosStereoCamera::getReadThreadResult, R"(TODOC)")
        .def("setReadThreadCallback", &I3DR::Phase::DeimosStereoCamera::setReadThreadCallback, R"(TODOC)")
        .def("startContinousReadThread", &I3DR::Phase::DeimosStereoCamera::startContinousReadThread, py::arg("timeout") = 1000, R"(TODOC)")
        .def("stopContinousReadThread", &I3DR::Phase::DeimosStereoCamera::stopContinousReadThread, R"(TODOC)")
        .def("isContinousReadThreadRunning", &I3DR::Phase::DeimosStereoCamera::isContinousReadThreadRunning, R"(TODOC)")
        .def("getWidth", &I3DR::Phase::DeimosStereoCamera::getWidth, R"(TODOC)")
        .def("getHeight", &I3DR::Phase::DeimosStereoCamera::getHeight, R"(TODOC)")
        .def("getDownsampleFactor", &I3DR::Phase::DeimosStereoCamera::getDownsampleFactor, R"(TODOC)")
        .def("enableDataCapture", &I3DR::Phase::DeimosStereoCamera::enableDataCapture, R"(TODOC)")
        .def("setDataCapturePath", &I3DR::Phase::DeimosStereoCamera::setDataCapturePath, R"(TODOC)")
        .def("getCaptureCount", &I3DR::Phase::DeimosStereoCamera::getCaptureCount, R"(TODOC)")
        .def("resetCaptureCount", &I3DR::Phase::DeimosStereoCamera::resetCaptureCount, R"(TODOC)")
        .def("setLeftFlipX", &I3DR::Phase::DeimosStereoCamera::setLeftFlipX, R"(TODOC)")
        .def("setLeftFlipY", &I3DR::Phase::DeimosStereoCamera::setLeftFlipY, R"(TODOC)")
        .def("setRightFlipX", &I3DR::Phase::DeimosStereoCamera::setRightFlipX, R"(TODOC)")
        .def("setRightFlipY", &I3DR::Phase::DeimosStereoCamera::setRightFlipY, R"(TODOC)")
        .def("setDownsampleFactor", &I3DR::Phase::DeimosStereoCamera::setDownsampleFactor, R"(TODOC)")
        .def("disconnect", &I3DR::Phase::DeimosStereoCamera::disconnect, R"(TODOC)");
}