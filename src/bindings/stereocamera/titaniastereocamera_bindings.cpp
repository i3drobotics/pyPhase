/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file titaniastereocamera_bindings.cpp
 * @brief Titania Stereo Camera class python bindings
 * @details Python bindings generated using pybind11
 */


#include"pybind11/pybind11.h"
#include "ndarray_converter.h"

#include <phase/stereocamera/titaniastereocamera.h>

namespace py = pybind11;

void init_titaniastereocamera(py::module_ &m) {
    NDArrayConverter::init_numpy();

    py::class_<I3DR::Phase::TitaniaStereoCamera>(m, "TitaniaStereoCamera")
        .def(py::init<I3DR::Phase::CameraDeviceInfo>())
        .def("connect", &I3DR::Phase::TitaniaStereoCamera::connect)
        .def("isConnected", &I3DR::Phase::TitaniaStereoCamera::isConnected)
        .def("startCapture", &I3DR::Phase::TitaniaStereoCamera::startCapture)
        .def("stopCapture", &I3DR::Phase::TitaniaStereoCamera::stopCapture)
        .def("isCapturing", &I3DR::Phase::TitaniaStereoCamera::isCapturing)
        .def("getFrameRate", &I3DR::Phase::TitaniaStereoCamera::getFrameRate)
        .def("setExposure", &I3DR::Phase::TitaniaStereoCamera::setExposure)
        .def("enableHardwareTrigger", &I3DR::Phase::TitaniaStereoCamera::enableHardwareTrigger)
        .def("setFrameRate", &I3DR::Phase::TitaniaStereoCamera::setFrameRate)
        .def("setLeftAOI", &I3DR::Phase::TitaniaStereoCamera::setLeftAOI)
        .def("setRightAOI", &I3DR::Phase::TitaniaStereoCamera::setRightAOI)
        .def("read", &I3DR::Phase::TitaniaStereoCamera::read, py::arg("timeout") = 1000)
        .def("setTestImagePaths", &I3DR::Phase::TitaniaStereoCamera::setTestImagePaths)
        .def("startReadThread", &I3DR::Phase::TitaniaStereoCamera::startReadThread, py::arg("timeout") = 1000)
        .def("isReadThreadRunning", &I3DR::Phase::TitaniaStereoCamera::isReadThreadRunning)
        .def("getReadThreadResult", &I3DR::Phase::TitaniaStereoCamera::getReadThreadResult)
        .def("setReadThreadCallback", &I3DR::Phase::TitaniaStereoCamera::setReadThreadCallback)
        .def("startContinousReadThread", &I3DR::Phase::TitaniaStereoCamera::startContinousReadThread, py::arg("timeout") = 1000)
        .def("stopContinousReadThread", &I3DR::Phase::TitaniaStereoCamera::stopContinousReadThread)
        .def("isContinousReadThreadRunning", &I3DR::Phase::TitaniaStereoCamera::isContinousReadThreadRunning)
        .def("getWidth", &I3DR::Phase::TitaniaStereoCamera::getWidth)
        .def("getHeight", &I3DR::Phase::TitaniaStereoCamera::getHeight)
        .def("getDownsampleFactor", &I3DR::Phase::TitaniaStereoCamera::getDownsampleFactor)
        .def("enableDataCapture", &I3DR::Phase::TitaniaStereoCamera::enableDataCapture)
        .def("setDataCapturePath", &I3DR::Phase::TitaniaStereoCamera::setDataCapturePath)
        .def("getCaptureCount", &I3DR::Phase::TitaniaStereoCamera::getCaptureCount)
        .def("resetCaptureCount", &I3DR::Phase::TitaniaStereoCamera::resetCaptureCount)
        .def("setLeftFlipX", &I3DR::Phase::TitaniaStereoCamera::setLeftFlipX)
        .def("setLeftFlipY", &I3DR::Phase::TitaniaStereoCamera::setLeftFlipY)
        .def("setRightFlipX", &I3DR::Phase::TitaniaStereoCamera::setRightFlipX)
        .def("setRightFlipY", &I3DR::Phase::TitaniaStereoCamera::setRightFlipY)
        .def("setDownsampleFactor", &I3DR::Phase::TitaniaStereoCamera::setDownsampleFactor)
        .def("disconnect", &I3DR::Phase::TitaniaStereoCamera::disconnect);
}