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
#include <pybind11/functional.h>
#include "ndarray_converter.h"

#include <phase/stereocamera/pylonstereocamera.h>

namespace py = pybind11;

void init_pylonstereocamera(py::module_ &m) {
    NDArrayConverter::init_numpy();
    //TODOC Description of the class and functions in PylonStereoCamera class
    py::class_<I3DR::Phase::PylonStereoCamera>(m, "PylonStereoCamera", R"(TODOC)")
        .def(py::init<I3DR::Phase::CameraDeviceInfo>(), R"(TODOC)")
        .def("connect", &I3DR::Phase::PylonStereoCamera::connect, R"(TODOC)")
        .def("isConnected", &I3DR::Phase::PylonStereoCamera::isConnected, R"(TODOC)")
        .def("startCapture", &I3DR::Phase::PylonStereoCamera::startCapture, R"(TODOC)")
        .def("stopCapture", &I3DR::Phase::PylonStereoCamera::stopCapture, R"(TODOC)")
        .def("isCapturing", &I3DR::Phase::PylonStereoCamera::isCapturing, R"(TODOC)")
        .def("getFrameRate", &I3DR::Phase::PylonStereoCamera::getFrameRate, R"(TODOC)")
        .def("setExposure", &I3DR::Phase::PylonStereoCamera::setExposure, R"(TODOC)")
        .def("enableHardwareTrigger", &I3DR::Phase::PylonStereoCamera::enableHardwareTrigger, R"(TODOC)")
        .def("setFrameRate", &I3DR::Phase::PylonStereoCamera::setFrameRate, R"(TODOC)")
        .def("setLeftAOI", &I3DR::Phase::PylonStereoCamera::setLeftAOI, R"(TODOC)")
        .def("setRightAOI", &I3DR::Phase::PylonStereoCamera::setRightAOI, R"(TODOC)")
        .def("read", &I3DR::Phase::PylonStereoCamera::read, py::arg("timeout") = 1000, R"(TODOC)")
        .def("setTestImagePaths", &I3DR::Phase::PylonStereoCamera::setTestImagePaths, R"(TODOC)")
        .def("startReadThread", &I3DR::Phase::PylonStereoCamera::startReadThread, py::arg("timeout") = 1000, R"(TODOC)")
        .def("isReadThreadRunning", &I3DR::Phase::PylonStereoCamera::isReadThreadRunning, R"(TODOC)")
        .def("getReadThreadResult", &I3DR::Phase::PylonStereoCamera::getReadThreadResult, R"(TODOC)")
        .def("setReadThreadCallback", &I3DR::Phase::PylonStereoCamera::setReadThreadCallback, R"(TODOC)")
        .def("startContinousReadThread", &I3DR::Phase::PylonStereoCamera::startContinousReadThread, py::arg("timeout") = 1000, R"(TODOC)")
        .def("stopContinousReadThread", &I3DR::Phase::PylonStereoCamera::stopContinousReadThread, R"(TODOC)")
        .def("isContinousReadThreadRunning", &I3DR::Phase::PylonStereoCamera::isContinousReadThreadRunning, R"(TODOC)")
        .def("getWidth", &I3DR::Phase::PylonStereoCamera::getWidth, R"(TODOC)")
        .def("getHeight", &I3DR::Phase::PylonStereoCamera::getHeight, R"(TODOC)")
        .def("getDownsampleFactor", &I3DR::Phase::PylonStereoCamera::getDownsampleFactor, R"(TODOC)")
        .def("enableDataCapture", &I3DR::Phase::PylonStereoCamera::enableDataCapture, R"(TODOC)")
        .def("setDataCapturePath", &I3DR::Phase::PylonStereoCamera::setDataCapturePath, R"(TODOC)")
        .def("getCaptureCount", &I3DR::Phase::PylonStereoCamera::getCaptureCount, R"(TODOC)")
        .def("resetCaptureCount", &I3DR::Phase::PylonStereoCamera::resetCaptureCount, R"(TODOC)")
        .def("setLeftFlipX", &I3DR::Phase::PylonStereoCamera::setLeftFlipX, R"(TODOC)")
        .def("setLeftFlipY", &I3DR::Phase::PylonStereoCamera::setLeftFlipY, R"(TODOC)")
        .def("setRightFlipX", &I3DR::Phase::PylonStereoCamera::setRightFlipX, R"(TODOC)")
        .def("setRightFlipY", &I3DR::Phase::PylonStereoCamera::setRightFlipY, R"(TODOC)")
        .def("setDownsampleFactor", &I3DR::Phase::PylonStereoCamera::setDownsampleFactor, R"(TODOC)")
        .def("disconnect", &I3DR::Phase::PylonStereoCamera::disconnect, R"(TODOC)");
}