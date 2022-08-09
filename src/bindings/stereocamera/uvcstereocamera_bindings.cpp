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
    //TODOC Description of the class and the functions in UVCStereoCamera class
    py::class_<I3DR::Phase::UVCStereoCamera>(m, "UVCStereoCamera", R"(TODOC)")
        .def(py::init<I3DR::Phase::CameraDeviceInfo>(), R"(TODOC)")
        .def("connect", &I3DR::Phase::UVCStereoCamera::connect, R"(TODOC)")
        .def("isConnected", &I3DR::Phase::UVCStereoCamera::isConnected, R"(TODOC)")
        .def("startCapture", &I3DR::Phase::UVCStereoCamera::startCapture, R"(TODOC)")
        .def("stopCapture", &I3DR::Phase::UVCStereoCamera::stopCapture, R"(TODOC)")
        .def("isCapturing", &I3DR::Phase::UVCStereoCamera::isCapturing, R"(TODOC)")
        .def("getFrameRate", &I3DR::Phase::UVCStereoCamera::getFrameRate, R"(TODOC)")
        .def("setExposure", &I3DR::Phase::UVCStereoCamera::setExposure, R"(TODOC)")
        .def("enableHardwareTrigger", &I3DR::Phase::UVCStereoCamera::enableHardwareTrigger, R"(TODOC)")
        .def("setFrameRate", &I3DR::Phase::UVCStereoCamera::setFrameRate, R"(TODOC)")
        .def("setLeftAOI", &I3DR::Phase::UVCStereoCamera::setLeftAOI, R"(TODOC)")
        .def("setRightAOI", &I3DR::Phase::UVCStereoCamera::setRightAOI, R"(TODOC)")
        .def("read", &I3DR::Phase::UVCStereoCamera::read, py::arg("timeout") = 1000, R"(TODOC)")
        .def("setTestImagePaths", &I3DR::Phase::UVCStereoCamera::setTestImagePaths, R"(TODOC)")
        .def("startReadThread", &I3DR::Phase::UVCStereoCamera::startReadThread, py::arg("timeout") = 1000, R"(TODOC)")
        .def("isReadThreadRunning", &I3DR::Phase::UVCStereoCamera::isReadThreadRunning, R"(TODOC)")
        .def("getReadThreadResult", &I3DR::Phase::UVCStereoCamera::getReadThreadResult, R"(TODOC)")
        .def("setReadThreadCallback", &I3DR::Phase::UVCStereoCamera::setReadThreadCallback, R"(TODOC)")
        .def("startContinousReadThread", &I3DR::Phase::UVCStereoCamera::startContinousReadThread, py::arg("timeout") = 1000, R"(TODOC)")
        .def("stopContinousReadThread", &I3DR::Phase::UVCStereoCamera::stopContinousReadThread, R"(TODOC)")
        .def("isContinousReadThreadRunning", &I3DR::Phase::UVCStereoCamera::isContinousReadThreadRunning, R"(TODOC)")
        .def("getWidth", &I3DR::Phase::UVCStereoCamera::getWidth, R"(TODOC)")
        .def("getHeight", &I3DR::Phase::UVCStereoCamera::getHeight, R"(TODOC)")
        .def("getDownsampleFactor", &I3DR::Phase::UVCStereoCamera::getDownsampleFactor, R"(TODOC)")
        .def("enableDataCapture", &I3DR::Phase::UVCStereoCamera::enableDataCapture, R"(TODOC)")
        .def("setDataCapturePath", &I3DR::Phase::UVCStereoCamera::setDataCapturePath, R"(TODOC)")
        .def("getCaptureCount", &I3DR::Phase::UVCStereoCamera::getCaptureCount, R"(TODOC)")
        .def("resetCaptureCount", &I3DR::Phase::UVCStereoCamera::resetCaptureCount, R"(TODOC)")
        .def("setLeftFlipX", &I3DR::Phase::UVCStereoCamera::setLeftFlipX, R"(TODOC)")
        .def("setLeftFlipY", &I3DR::Phase::UVCStereoCamera::setLeftFlipY, R"(TODOC)")
        .def("setRightFlipX", &I3DR::Phase::UVCStereoCamera::setRightFlipX, R"(TODOC)")
        .def("setRightFlipY", &I3DR::Phase::UVCStereoCamera::setRightFlipY, R"(TODOC)")
        .def("setDownsampleFactor", &I3DR::Phase::UVCStereoCamera::setDownsampleFactor, R"(TODOC)")
        .def("disconnect", &I3DR::Phase::UVCStereoCamera::disconnect, R"(TODOC)");
}
