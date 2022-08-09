/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file titaniastereocamera_bindings.cpp
 * @brief Titania Stereo Camera class python bindings
 * @details Python bindings generated using pybind11
 */


#include "pybind11/pybind11.h"
#include <pybind11/functional.h>
#include "ndarray_converter.h"

#include <phase/stereocamera/titaniastereocamera.h>

namespace py = pybind11;

void init_titaniastereocamera(py::module_ &m) {
    NDArrayConverter::init_numpy();
    //TODOC Description of the class and functions in TitaniaStereoCamera class
    py::class_<I3DR::Phase::TitaniaStereoCamera>(m, "TitaniaStereoCamera", R"(TODOC)")
        .def(py::init<I3DR::Phase::CameraDeviceInfo>(), R"(TODOC)")
        .def("connect", &I3DR::Phase::TitaniaStereoCamera::connect, R"(TODOC)")
        .def("isConnected", &I3DR::Phase::TitaniaStereoCamera::isConnected, R"(TODOC)")
        .def("startCapture", &I3DR::Phase::TitaniaStereoCamera::startCapture, R"(TODOC)")
        .def("stopCapture", &I3DR::Phase::TitaniaStereoCamera::stopCapture, R"(TODOC)")
        .def("isCapturing", &I3DR::Phase::TitaniaStereoCamera::isCapturing, R"(TODOC)")
        .def("getFrameRate", &I3DR::Phase::TitaniaStereoCamera::getFrameRate, R"(TODOC)")
        .def("setExposure", &I3DR::Phase::TitaniaStereoCamera::setExposure, R"(TODOC)")
        .def("enableHardwareTrigger", &I3DR::Phase::TitaniaStereoCamera::enableHardwareTrigger, R"(TODOC)")
        .def("setFrameRate", &I3DR::Phase::TitaniaStereoCamera::setFrameRate, R"(TODOC)")
        .def("setLeftAOI", &I3DR::Phase::TitaniaStereoCamera::setLeftAOI, R"(TODOC)")
        .def("setRightAOI", &I3DR::Phase::TitaniaStereoCamera::setRightAOI, R"(TODOC)")
        .def("read", &I3DR::Phase::TitaniaStereoCamera::read, py::arg("timeout") = 1000, R"(TODOC)")
        .def("setTestImagePaths", &I3DR::Phase::TitaniaStereoCamera::setTestImagePaths, R"(TODOC)")
        .def("startReadThread", &I3DR::Phase::TitaniaStereoCamera::startReadThread, py::arg("timeout") = 1000, R"(TODOC)")
        .def("isReadThreadRunning", &I3DR::Phase::TitaniaStereoCamera::isReadThreadRunning, R"(TODOC)")
        .def("getReadThreadResult", &I3DR::Phase::TitaniaStereoCamera::getReadThreadResult, R"(TODOC)")
        .def("setReadThreadCallback", &I3DR::Phase::TitaniaStereoCamera::setReadThreadCallback, R"(TODOC)")
        .def("startContinousReadThread", &I3DR::Phase::TitaniaStereoCamera::startContinousReadThread, py::arg("timeout") = 1000, R"(TODOC)")
        .def("stopContinousReadThread", &I3DR::Phase::TitaniaStereoCamera::stopContinousReadThread, R"(TODOC)")
        .def("isContinousReadThreadRunning", &I3DR::Phase::TitaniaStereoCamera::isContinousReadThreadRunning, R"(TODOC)")
        .def("getWidth", &I3DR::Phase::TitaniaStereoCamera::getWidth, R"(TODOC)")
        .def("getHeight", &I3DR::Phase::TitaniaStereoCamera::getHeight, R"(TODOC)")
        .def("getDownsampleFactor", &I3DR::Phase::TitaniaStereoCamera::getDownsampleFactor, R"(TODOC)")
        .def("enableDataCapture", &I3DR::Phase::TitaniaStereoCamera::enableDataCapture, R"(TODOC)")
        .def("setDataCapturePath", &I3DR::Phase::TitaniaStereoCamera::setDataCapturePath, R"(TODOC)")
        .def("getCaptureCount", &I3DR::Phase::TitaniaStereoCamera::getCaptureCount, R"(TODOC)")
        .def("resetCaptureCount", &I3DR::Phase::TitaniaStereoCamera::resetCaptureCount, R"(TODOC)")
        .def("setLeftFlipX", &I3DR::Phase::TitaniaStereoCamera::setLeftFlipX, R"(TODOC)")
        .def("setLeftFlipY", &I3DR::Phase::TitaniaStereoCamera::setLeftFlipY, R"(TODOC)")
        .def("setRightFlipX", &I3DR::Phase::TitaniaStereoCamera::setRightFlipX, R"(TODOC)")
        .def("setRightFlipY", &I3DR::Phase::TitaniaStereoCamera::setRightFlipY, R"(TODOC)")
        .def("setDownsampleFactor", &I3DR::Phase::TitaniaStereoCamera::setDownsampleFactor, R"(TODOC)")
        .def("disconnect", &I3DR::Phase::TitaniaStereoCamera::disconnect, R"(TODOC)");
}