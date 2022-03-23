/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file phobosstereocamera_bindings.cpp
 * @brief Phobos Stereo Camera class python bindings
 * @details Python bindings generated using pybind11
 */

#include"pybind11/pybind11.h"
#include "ndarray_converter.h"

#include <phase/stereocamera/phobosstereocamera.h>

namespace py = pybind11;

void init_phobosstereocamera(py::module_ &m) {
    NDArrayConverter::init_numpy();

    py::class_<I3DR::Phase::PhobosStereoCamera>(m, "PhobosStereoCamera")
        .def(py::init<I3DR::Phase::CameraDeviceInfo>())
        .def("startCapture", &I3DR::Phase::PhobosStereoCamera::startCapture)
        .def("stopCapture", &I3DR::Phase::PhobosStereoCamera::stopCapture)
        .def("isCapturing", &I3DR::Phase::PhobosStereoCamera::isCapturing)
        .def("isConnected", &I3DR::Phase::PhobosStereoCamera::isConnected)
        .def("connect", &I3DR::Phase::PhobosStereoCamera::connect)
        .def("getWidth", &I3DR::Phase::PhobosStereoCamera::getWidth)
        .def("getHeight", &I3DR::Phase::PhobosStereoCamera::getHeight)
        .def("getFrameRate", &I3DR::Phase::PhobosStereoCamera::getFrameRate)
        .def("setExposure", &I3DR::Phase::PhobosStereoCamera::setExposure)
        .def("setTestImagePaths", &I3DR::Phase::PhobosStereoCamera::setTestImagePaths)
        .def("setDownsampleFactor", &I3DR::Phase::PhobosStereoCamera::setDownsampleFactor)
        .def("enableHardwareTrigger", &I3DR::Phase::PhobosStereoCamera::enableHardwareTrigger)
        .def("setLeftAOI", &I3DR::Phase::PhobosStereoCamera::setLeftAOI)
        .def("setRightAOI", &I3DR::Phase::PhobosStereoCamera::setRightAOI)
        .def("setFrameRate", &I3DR::Phase::PhobosStereoCamera::setFrameRate)
        .def("read", &I3DR::Phase::PhobosStereoCamera::read, py::arg("timeout") = 1000)
        .def("startReadThread", &I3DR::Phase::PhobosStereoCamera::startReadThread, py::arg("timeout") = 1000)
        .def("isReadThreadRunning", &I3DR::Phase::PhobosStereoCamera::isReadThreadRunning)
        .def("getReadThreadResult", &I3DR::Phase::PhobosStereoCamera::getReadThreadResult)
        .def("disconnect", &I3DR::Phase::PhobosStereoCamera::disconnect);
        //TODO add callback funtion for read results (https://pybind11.readthedocs.io/en/stable/advanced/cast/functional.html)
}