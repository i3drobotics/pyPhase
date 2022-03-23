/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file stereovision_bindings.cpp
 * @brief Stereo Vision class python bindings
 * @details Python bindings generated using pybind11
 */

#include"pybind11/pybind11.h"
#include "ndarray_converter.h"

#include <phase/stereovision.h>

namespace py = pybind11;

void init_stereovision(py::module_ &m) {
    NDArrayConverter::init_numpy();

    py::class_<I3DR::Phase::StereoVision>(m, "StereoVision", py::module_local(), R"(
        Stereo Vision class
        

        Capture images from stereo camera and process with stereo matcher
        to generate depth. Brings together Stereo Camera and Stereo Matcher classes into
        single class for easy use.

        )")
        .def(py::init<I3DR::Phase::CameraDeviceInfo,I3DR::Phase::StereoMatcherType,const char*,const char*>())
        .def("connect", &I3DR::Phase::StereoVision::connect)
        .def("isConnected", &I3DR::Phase::StereoVision::isConnected)
        .def("startCapture", &I3DR::Phase::StereoVision::startCapture)
        .def("stopCapture", &I3DR::Phase::StereoVision::stopCapture)
        .def("isCapturing", &I3DR::Phase::StereoVision::isCapturing)
        .def("isValidCalibration", &I3DR::Phase::StereoVision::isValidCalibration)
        .def("getWidth", &I3DR::Phase::StereoVision::getWidth)
        .def("getHeight", &I3DR::Phase::StereoVision::getHeight)
        .def("getDownsampleFactor", &I3DR::Phase::StereoVision::getDownsampleFactor)
        .def("setTestImagePaths", &I3DR::Phase::StereoVision::setTestImagePaths)
        .def("getCamera", &I3DR::Phase::StereoVision::getCamera, py::return_value_policy::reference)
        .def("getMatcher", &I3DR::Phase::StereoVision::getMatcher, py::return_value_policy::reference)
        .def("getCalibration", &I3DR::Phase::StereoVision::getCalibration, py::return_value_policy::reference)
        .def("getHFOV", &I3DR::Phase::StereoVision::getHFOV)
        .def("setDownsampleFactor", &I3DR::Phase::StereoVision::setDownsampleFactor)
        .def("read", &I3DR::Phase::StereoVision::read, py::arg("timeout") = 1000, py::arg("rectify") = true)
        .def("startReadThread", &I3DR::Phase::StereoVision::startReadThread, py::arg("timeout") = 1000, py::arg("rectify") = true)
        .def("isReadThreadRunning", &I3DR::Phase::StereoVision::isReadThreadRunning)
        .def("getReadThreadResult", &I3DR::Phase::StereoVision::getReadThreadResult)
        .def("disconnect", &I3DR::Phase::StereoVision::disconnect);
        //TODO add callback funtion for read results (https://pybind11.readthedocs.io/en/stable/advanced/cast/functional.html)
}