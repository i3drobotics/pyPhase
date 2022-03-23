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
        .def("startCapture", &I3DR::Phase::TitaniaStereoCamera::startCapture)
        .def("stopCapture", &I3DR::Phase::TitaniaStereoCamera::stopCapture)
        .def("isCapturing", &I3DR::Phase::TitaniaStereoCamera::isCapturing)
        .def("isConnected", &I3DR::Phase::TitaniaStereoCamera::isConnected)
        .def("connect", &I3DR::Phase::TitaniaStereoCamera::connect)
        .def("getWidth", &I3DR::Phase::TitaniaStereoCamera::getWidth)
        .def("getHeight", &I3DR::Phase::TitaniaStereoCamera::getHeight)
        .def("getFrameRate", &I3DR::Phase::TitaniaStereoCamera::getFrameRate)
        .def("setExposure", &I3DR::Phase::TitaniaStereoCamera::setExposure)
        .def("setTestImagePaths", &I3DR::Phase::TitaniaStereoCamera::setTestImagePaths)
        .def("setDownsampleFactor", &I3DR::Phase::TitaniaStereoCamera::setDownsampleFactor)
        .def("enableHardwareTrigger", &I3DR::Phase::TitaniaStereoCamera::enableHardwareTrigger)
        .def("setLeftAOI", &I3DR::Phase::TitaniaStereoCamera::setLeftAOI)
        .def("setRightAOI", &I3DR::Phase::TitaniaStereoCamera::setRightAOI)
        .def("setFrameRate", &I3DR::Phase::TitaniaStereoCamera::setFrameRate)
        .def("read", &I3DR::Phase::TitaniaStereoCamera::read, py::arg("timeout") = 1000)
        .def("startReadThread", &I3DR::Phase::TitaniaStereoCamera::startReadThread, py::arg("timeout") = 1000)
        .def("isReadThreadRunning", &I3DR::Phase::TitaniaStereoCamera::isReadThreadRunning)
        .def("getReadThreadResult", &I3DR::Phase::TitaniaStereoCamera::getReadThreadResult)
        .def("disconnect", &I3DR::Phase::TitaniaStereoCamera::disconnect);
}