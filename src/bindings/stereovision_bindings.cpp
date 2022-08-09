/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file stereovision_bindings.cpp
 * @brief Stereo Vision class python bindings
 * @details Python bindings generated using pybind11
 */

#include "pybind11/pybind11.h"
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
        //TODOC Description of functions in StereoVision class
        .def(py::init<I3DR::Phase::CameraDeviceInfo,I3DR::Phase::StereoMatcherType,const char*,const char*>(), R"(TODOC)")
        .def("connect", &I3DR::Phase::StereoVision::connect, R"(TODOC)")
        .def("isConnected", &I3DR::Phase::StereoVision::isConnected, R"(TODOC)")
        .def("startCapture", &I3DR::Phase::StereoVision::startCapture, R"(TODOC)")
        .def("stopCapture", &I3DR::Phase::StereoVision::stopCapture, R"(TODOC)")
        .def("isCapturing", &I3DR::Phase::StereoVision::isCapturing, R"(TODOC)")
        .def("isValidCalibration", &I3DR::Phase::StereoVision::isValidCalibration, R"(TODOC)")
        .def("getWidth", &I3DR::Phase::StereoVision::getWidth, R"(TODOC)")
        .def("getHeight", &I3DR::Phase::StereoVision::getHeight, R"(TODOC)")
        .def("getDownsampleFactor", &I3DR::Phase::StereoVision::getDownsampleFactor, R"(TODOC)")
        .def("setTestImagePaths", &I3DR::Phase::StereoVision::setTestImagePaths, R"(TODOC)")
        .def("getCamera", &I3DR::Phase::StereoVision::getCamera, py::return_value_policy::reference, R"(TODOC)")
        .def("getMatcher", &I3DR::Phase::StereoVision::getMatcher, py::return_value_policy::reference, R"(TODOC)")
        .def("getCalibration", &I3DR::Phase::StereoVision::getCalibration, py::return_value_policy::reference, R"(TODOC)")
        .def("getHFOV", &I3DR::Phase::StereoVision::getHFOV, R"(TODOC)")
        .def("setDownsampleFactor", &I3DR::Phase::StereoVision::setDownsampleFactor, R"(TODOC)")
        .def("read", &I3DR::Phase::StereoVision::read, py::arg("timeout") = 1000, py::arg("rectify") = true, R"(TODOC)")
        .def("startReadThread", &I3DR::Phase::StereoVision::startReadThread, py::arg("timeout") = 1000, py::arg("rectify") = true, R"(TODOC)")
        .def("isReadThreadRunning", &I3DR::Phase::StereoVision::isReadThreadRunning, R"(TODOC)")
        .def("getReadThreadResult", &I3DR::Phase::StereoVision::getReadThreadResult, R"(TODOC)")
        .def("disconnect", &I3DR::Phase::StereoVision::disconnect, R"(TODOC)");
        //TODO add callback funtion for read results (https://pybind11.readthedocs.io/en/stable/advanced/cast/functional.html)
}