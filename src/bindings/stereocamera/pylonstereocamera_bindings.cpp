/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file pylonstereocamera_bindings.cpp
 * @brief Pylon Stereo Camera class python bindings
 * @details Python bindings generated using pybind11
 */

#include"pybind11/pybind11.h"
#include "ndarray_converter.h"

#include <phase/stereocamera/pylonstereocamera.h>

namespace py = pybind11;

void init_pylonstereocamera(py::module_ &m) {
    NDArrayConverter::init_numpy();

    py::class_<I3DR::Phase::PylonStereoCamera>(m, "PylonStereoCamera")
        .def(py::init<I3DR::Phase::CameraDeviceInfo>())
        .def("startCapture", &I3DR::Phase::PylonStereoCamera::startCapture)
        .def("stopCapture", &I3DR::Phase::PylonStereoCamera::stopCapture)
        .def("isCapturing", &I3DR::Phase::PylonStereoCamera::isCapturing)
        .def("isConnected", &I3DR::Phase::PylonStereoCamera::isConnected)
        .def("connect", &I3DR::Phase::PylonStereoCamera::connect)
        .def("getWidth", &I3DR::Phase::PylonStereoCamera::getWidth)
        .def("getHeight", &I3DR::Phase::PylonStereoCamera::getHeight)
        .def("getFrameRate", &I3DR::Phase::PylonStereoCamera::getFrameRate)
        .def("setExposure", &I3DR::Phase::PylonStereoCamera::setExposure)
        .def("setTestImagePaths", &I3DR::Phase::PylonStereoCamera::setTestImagePaths)
        .def("setDownsampleFactor", &I3DR::Phase::PylonStereoCamera::setDownsampleFactor)
        .def("enableHardwareTrigger", &I3DR::Phase::PylonStereoCamera::enableHardwareTrigger)
        .def("setLeftAOI", &I3DR::Phase::PylonStereoCamera::setLeftAOI)
        .def("setRightAOI", &I3DR::Phase::PylonStereoCamera::setRightAOI)
        .def("setFrameRate", &I3DR::Phase::PylonStereoCamera::setFrameRate)
        .def("read", &I3DR::Phase::PylonStereoCamera::read, py::arg("timeout") = 1000)
        .def("startReadThread", &I3DR::Phase::PylonStereoCamera::startReadThread, py::arg("timeout") = 1000)
        .def("isReadThreadRunning", &I3DR::Phase::PylonStereoCamera::isReadThreadRunning)
        .def("getReadThreadResult", &I3DR::Phase::PylonStereoCamera::getReadThreadResult)
        .def_readwrite("left_reverse_x", &I3DR::Phase::PylonStereoCamera::left_reverse_x)
        .def_readwrite("left_reverse_y", &I3DR::Phase::PylonStereoCamera::left_reverse_y)
        .def_readwrite("right_reverse_x", &I3DR::Phase::PylonStereoCamera::right_reverse_x)
        .def_readwrite("right_reverse_y", &I3DR::Phase::PylonStereoCamera::right_reverse_y)
        .def("disconnect", &I3DR::Phase::PylonStereoCamera::disconnect);
}