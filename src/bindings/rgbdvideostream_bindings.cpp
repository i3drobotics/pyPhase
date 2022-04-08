/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file rgbdvideostream_bindings.cpp
 * @brief RGBD Video Stream class python bindings
 * @details Python bindings generated using pybind11
 */

#include "pybind11/pybind11.h"
#include "ndarray_converter.h"

#include <phase/rgbdvideostream.h>

namespace py = pybind11;

void init_rgbdvideostream(py::module_ &m) {
    NDArrayConverter::init_numpy();

    py::class_<I3DR::Phase::RGBDVideoStream>(m, "RGBDVideoStream", py::module_local(), R"(
        RGBD Video Stream
        

        Stream RGB and Depth video

        )")
        .def(py::init<const char*, const char* >())
        .def("load", &I3DR::Phase::RGBDVideoStream::load)
        .def("loadThreaded", &I3DR::Phase::RGBDVideoStream::loadThreaded)
        .def("isLoadThreadRunning", &I3DR::Phase::RGBDVideoStream::isLoadThreadRunning)
        .def("getLoadThreadResult", &I3DR::Phase::RGBDVideoStream::getLoadThreadResult)
        .def("restart", &I3DR::Phase::RGBDVideoStream::restart)
        .def("read", &I3DR::Phase::RGBDVideoStream::read)
        .def("readThreaded", &I3DR::Phase::RGBDVideoStream::readThreaded)
        .def("isReadThreadRunning", &I3DR::Phase::RGBDVideoStream::isReadThreadRunning)
        .def("getReadThreadResult", &I3DR::Phase::RGBDVideoStream::getReadThreadResult)
        .def("isOpened", &I3DR::Phase::RGBDVideoStream::isOpened)
        .def("isLoaded", &I3DR::Phase::RGBDVideoStream::isLoaded)
        .def("isFinished", &I3DR::Phase::RGBDVideoStream::isFinished)
        .def("getWidth", &I3DR::Phase::RGBDVideoStream::getWidth)
        .def("getHeight", &I3DR::Phase::RGBDVideoStream::getHeight)
        .def("getHFOV", &I3DR::Phase::RGBDVideoStream::getHFOV)
        .def("getDownsampleFactor", &I3DR::Phase::RGBDVideoStream::getDownsampleFactor)
        .def("setDownsampleFactor", &I3DR::Phase::RGBDVideoStream::setDownsampleFactor)
        .def("close", &I3DR::Phase::RGBDVideoStream::close);
}