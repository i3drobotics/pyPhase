/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file uvcstereocamera_bindings.cpp
 * @brief UVC Stereo Camera class python bindings
 * @details Python bindings generated using pybind11
 */

#include"pybind11/pybind11.h"
#include "ndarray_converter.h"

#include <phase/stereocamera/uvcstereocamera.h>

namespace py = pybind11;

void init_uvcstereocamera(py::module_ &m) {
    NDArrayConverter::init_numpy();

    py::class_<I3DR::Phase::UVCStereoCamera>(m, "UVCStereoCamera")
        .def(py::init<I3DR::Phase::CameraDeviceInfo>())
        .def("startCapture", &I3DR::Phase::UVCStereoCamera::startCapture)
        .def("stopCapture", &I3DR::Phase::UVCStereoCamera::stopCapture)
        .def("isCapturing", &I3DR::Phase::UVCStereoCamera::isCapturing)
        .def("isConnected", &I3DR::Phase::UVCStereoCamera::isConnected)
        .def("connect", &I3DR::Phase::UVCStereoCamera::connect)
        .def("getWidth", &I3DR::Phase::UVCStereoCamera::getWidth)
        .def("getHeight", &I3DR::Phase::UVCStereoCamera::getHeight)
        .def("getFrameRate", &I3DR::Phase::UVCStereoCamera::getFrameRate)
        .def("setExposure", &I3DR::Phase::UVCStereoCamera::setExposure)
        .def("setTestImagePaths", &I3DR::Phase::UVCStereoCamera::setTestImagePaths)
        .def("setDownsampleFactor", &I3DR::Phase::UVCStereoCamera::setDownsampleFactor)
        .def("enableHardwareTrigger", &I3DR::Phase::UVCStereoCamera::enableHardwareTrigger)
        .def("setLeftAOI", &I3DR::Phase::UVCStereoCamera::setLeftAOI)
        .def("setRightAOI", &I3DR::Phase::UVCStereoCamera::setRightAOI)
        .def("setFrameRate", &I3DR::Phase::UVCStereoCamera::setFrameRate)
        .def("read", &I3DR::Phase::UVCStereoCamera::read, py::arg("timeout") = 1000)
        .def("startReadThread", &I3DR::Phase::UVCStereoCamera::startReadThread, py::arg("timeout") = 1000)
        .def("isReadThreadRunning", &I3DR::Phase::UVCStereoCamera::isReadThreadRunning)
        .def("getReadThreadResult", &I3DR::Phase::UVCStereoCamera::getReadThreadResult)
        .def("disconnect", &I3DR::Phase::UVCStereoCamera::disconnect);
}