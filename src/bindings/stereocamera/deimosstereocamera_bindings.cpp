/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file deimosstereocamera_bindings.cpp
 * @brief Deimos Stereo Camera class python bindings
 * @details Python bindings generated using pybind11
 */


#include"pybind11/pybind11.h"
#include "ndarray_converter.h"

#include <phase/stereocamera/deimosstereocamera.h>

namespace py = pybind11;

void init_deimosstereocamera(py::module_ &m) {
    NDArrayConverter::init_numpy();

    py::class_<I3DR::Phase::DeimosStereoCamera>(m, "DeimosStereoCamera")
        .def(py::init<I3DR::Phase::CameraDeviceInfo>())
        .def("startCapture", &I3DR::Phase::DeimosStereoCamera::startCapture)
        .def("stopCapture", &I3DR::Phase::DeimosStereoCamera::stopCapture)
        .def("isCapturing", &I3DR::Phase::DeimosStereoCamera::isCapturing)
        .def("isConnected", &I3DR::Phase::DeimosStereoCamera::isConnected)
        .def("connect", &I3DR::Phase::DeimosStereoCamera::connect)
        .def("getWidth", &I3DR::Phase::DeimosStereoCamera::getWidth)
        .def("getHeight", &I3DR::Phase::DeimosStereoCamera::getHeight)
        .def("getFrameRate", &I3DR::Phase::DeimosStereoCamera::getFrameRate)
        .def("setExposure", &I3DR::Phase::DeimosStereoCamera::setExposure)
        .def("enableHardwareTrigger", &I3DR::Phase::DeimosStereoCamera::enableHardwareTrigger)
        .def("setLeftAOI", &I3DR::Phase::DeimosStereoCamera::setLeftAOI)
        .def("setRightAOI", &I3DR::Phase::DeimosStereoCamera::setRightAOI)
        .def("setFrameRate", &I3DR::Phase::DeimosStereoCamera::setFrameRate)
        .def("setTestImagePaths", &I3DR::Phase::DeimosStereoCamera::setTestImagePaths)
        .def("setDownsampleFactor", &I3DR::Phase::DeimosStereoCamera::setDownsampleFactor)
        .def("read", &I3DR::Phase::DeimosStereoCamera::read, py::arg("timeout") = 1000)
        .def("startReadThread", &I3DR::Phase::DeimosStereoCamera::startReadThread, py::arg("timeout") = 1000)
        .def("isReadThreadRunning", &I3DR::Phase::DeimosStereoCamera::isReadThreadRunning)
        .def("getReadThreadResult", &I3DR::Phase::DeimosStereoCamera::getReadThreadResult)
        .def("disconnect", &I3DR::Phase::DeimosStereoCamera::disconnect);
}