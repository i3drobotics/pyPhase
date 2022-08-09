/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file abstractstereocamera_bindings.cpp
 * @brief Abstract Stereo Camera class python bindings
 * @details Python bindings generated using pybind11
 */

#include "pybind11/pybind11.h"
#include <pybind11/functional.h>
#include "ndarray_converter.h"

#include <phase/stereocamera/abstractstereocamera.h>

namespace py = pybind11;

void init_abstractstereocamera(py::module_ &m) {
    NDArrayConverter::init_numpy();
    //TODOC Description of the class and functions in AbstractStereoCamera class
    py::class_<I3DR::Phase::AbstractStereoCamera>(m, "AbstractStereoCamera", R"(TODOC)")
        .def("connect", &I3DR::Phase::AbstractStereoCamera::connect, R"(TODOC)")
        .def("isConnected", &I3DR::Phase::AbstractStereoCamera::isConnected, R"(TODOC)")
        .def("startCapture", &I3DR::Phase::AbstractStereoCamera::startCapture, R"(TODOC)")
        .def("stopCapture", &I3DR::Phase::AbstractStereoCamera::stopCapture, R"(TODOC)")
        .def("isCapturing", &I3DR::Phase::AbstractStereoCamera::isCapturing, R"(TODOC)")
        .def("getFrameRate", &I3DR::Phase::AbstractStereoCamera::getFrameRate, R"(TODOC)")
        .def("setExposure", &I3DR::Phase::AbstractStereoCamera::setExposure, R"(TODOC)")
        .def("enableHardwareTrigger", &I3DR::Phase::AbstractStereoCamera::enableHardwareTrigger, R"(TODOC)")
        .def("setFrameRate", &I3DR::Phase::AbstractStereoCamera::setFrameRate, R"(TODOC)")
        .def("setLeftAOI", &I3DR::Phase::AbstractStereoCamera::setLeftAOI, R"(TODOC)")
        .def("setRightAOI", &I3DR::Phase::AbstractStereoCamera::setRightAOI, R"(TODOC)")
        .def("read", &I3DR::Phase::AbstractStereoCamera::read, py::arg("timeout") = 1000, R"(TODOC)")
        .def("setTestImagePaths", &I3DR::Phase::AbstractStereoCamera::setTestImagePaths, R"(TODOC)")
        .def("startReadThread", &I3DR::Phase::AbstractStereoCamera::startReadThread, py::arg("timeout") = 1000, R"(TODOC)")
        .def("isReadThreadRunning", &I3DR::Phase::AbstractStereoCamera::isReadThreadRunning, R"(TODOC)")
        .def("getReadThreadResult", &I3DR::Phase::AbstractStereoCamera::getReadThreadResult, R"(TODOC)")
        .def("setReadThreadCallback", &I3DR::Phase::AbstractStereoCamera::setReadThreadCallback, R"(TODOC)")
        .def("startContinousReadThread", &I3DR::Phase::AbstractStereoCamera::startContinousReadThread, py::arg("timeout") = 1000, R"(TODOC)")
        .def("stopContinousReadThread", &I3DR::Phase::AbstractStereoCamera::stopContinousReadThread, R"(TODOC)")
        .def("isContinousReadThreadRunning", &I3DR::Phase::AbstractStereoCamera::isContinousReadThreadRunning, R"(TODOC)")
        .def("getWidth", &I3DR::Phase::AbstractStereoCamera::getWidth, R"(TODOC)")
        .def("getHeight", &I3DR::Phase::AbstractStereoCamera::getHeight, R"(TODOC)")
        .def("getDownsampleFactor", &I3DR::Phase::AbstractStereoCamera::getDownsampleFactor, R"(TODOC)")
        .def("enableDataCapture", &I3DR::Phase::AbstractStereoCamera::enableDataCapture, R"(TODOC)")
        .def("setDataCapturePath", &I3DR::Phase::AbstractStereoCamera::setDataCapturePath, R"(TODOC)")
        .def("getCaptureCount", &I3DR::Phase::AbstractStereoCamera::getCaptureCount, R"(TODOC)")
        .def("resetCaptureCount", &I3DR::Phase::AbstractStereoCamera::resetCaptureCount, R"(TODOC)")
        .def("setLeftFlipX", &I3DR::Phase::AbstractStereoCamera::setLeftFlipX, R"(TODOC)")
        .def("setLeftFlipY", &I3DR::Phase::AbstractStereoCamera::setLeftFlipY, R"(TODOC)")
        .def("setRightFlipX", &I3DR::Phase::AbstractStereoCamera::setRightFlipX, R"(TODOC)")
        .def("setRightFlipY", &I3DR::Phase::AbstractStereoCamera::setRightFlipY, R"(TODOC)")
        .def("setDownsampleFactor", &I3DR::Phase::AbstractStereoCamera::setDownsampleFactor, R"(TODOC)")
        .def("disconnect", &I3DR::Phase::AbstractStereoCamera::disconnect, R"(TODOC)");

    //TODO add callback funtion for read results (https://pybind11.readthedocs.io/en/stable/advanced/cast/functional.html)

}