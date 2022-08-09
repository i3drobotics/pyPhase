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
    //TODOC Description of the class and functions in PhobosStereoCamera class
    py::class_<I3DR::Phase::PhobosStereoCamera>(m, "PhobosStereoCamera", R"(TODOC)")
        .def(py::init<I3DR::Phase::CameraDeviceInfo>(), R"(TODOC)")
        .def("connect", &I3DR::Phase::PhobosStereoCamera::connect, R"(TODOC)")
        .def("isConnected", &I3DR::Phase::PhobosStereoCamera::isConnected, R"(TODOC)")
        .def("startCapture", &I3DR::Phase::PhobosStereoCamera::startCapture, R"(TODOC)")
        .def("stopCapture", &I3DR::Phase::PhobosStereoCamera::stopCapture, R"(TODOC)")
        .def("isCapturing", &I3DR::Phase::PhobosStereoCamera::isCapturing, R"(TODOC)")
        .def("getFrameRate", &I3DR::Phase::PhobosStereoCamera::getFrameRate, R"(TODOC)")
        .def("setExposure", &I3DR::Phase::PhobosStereoCamera::setExposure, R"(TODOC)")
        .def("enableHardwareTrigger", &I3DR::Phase::PhobosStereoCamera::enableHardwareTrigger, R"(TODOC)")
        .def("setFrameRate", &I3DR::Phase::PhobosStereoCamera::setFrameRate, R"(TODOC)")
        .def("setLeftAOI", &I3DR::Phase::PhobosStereoCamera::setLeftAOI, R"(TODOC)")
        .def("setRightAOI", &I3DR::Phase::PhobosStereoCamera::setRightAOI, R"(TODOC)")
        .def("read", &I3DR::Phase::PhobosStereoCamera::read, py::arg("timeout") = 1000, R"(TODOC)")
        .def("setTestImagePaths", &I3DR::Phase::PhobosStereoCamera::setTestImagePaths, R"(TODOC)")
        .def("startReadThread", &I3DR::Phase::PhobosStereoCamera::startReadThread, py::arg("timeout") = 1000, R"(TODOC)")
        .def("isReadThreadRunning", &I3DR::Phase::PhobosStereoCamera::isReadThreadRunning, R"(TODOC)")
        .def("getReadThreadResult", &I3DR::Phase::PhobosStereoCamera::getReadThreadResult, R"(TODOC)")
        .def("setReadThreadCallback", &I3DR::Phase::PhobosStereoCamera::setReadThreadCallback, R"(TODOC)")
        .def("startContinousReadThread", &I3DR::Phase::PhobosStereoCamera::startContinousReadThread, py::arg("timeout") = 1000, R"(TODOC)")
        .def("stopContinousReadThread", &I3DR::Phase::PhobosStereoCamera::stopContinousReadThread, R"(TODOC)")
        .def("isContinousReadThreadRunning", &I3DR::Phase::PhobosStereoCamera::isContinousReadThreadRunning, R"(TODOC)")
        .def("getWidth", &I3DR::Phase::PhobosStereoCamera::getWidth, R"(TODOC)")
        .def("getHeight", &I3DR::Phase::PhobosStereoCamera::getHeight, R"(TODOC)")
        .def("getDownsampleFactor", &I3DR::Phase::PhobosStereoCamera::getDownsampleFactor, R"(TODOC)")
        .def("enableDataCapture", &I3DR::Phase::PhobosStereoCamera::enableDataCapture, R"(TODOC)")
        .def("setDataCapturePath", &I3DR::Phase::PhobosStereoCamera::setDataCapturePath, R"(TODOC)")
        .def("getCaptureCount", &I3DR::Phase::PhobosStereoCamera::getCaptureCount, R"(TODOC)")
        .def("resetCaptureCount", &I3DR::Phase::PhobosStereoCamera::resetCaptureCount, R"(TODOC)")
        .def("setLeftFlipX", &I3DR::Phase::PhobosStereoCamera::setLeftFlipX, R"(TODOC)")
        .def("setLeftFlipY", &I3DR::Phase::PhobosStereoCamera::setLeftFlipY, R"(TODOC)")
        .def("setRightFlipX", &I3DR::Phase::PhobosStereoCamera::setRightFlipX, R"(TODOC)")
        .def("setRightFlipY", &I3DR::Phase::PhobosStereoCamera::setRightFlipY, R"(TODOC)")
        .def("setDownsampleFactor", &I3DR::Phase::PhobosStereoCamera::setDownsampleFactor, R"(TODOC)")
        .def("disconnect", &I3DR::Phase::PhobosStereoCamera::disconnect, R"(TODOC)");

}