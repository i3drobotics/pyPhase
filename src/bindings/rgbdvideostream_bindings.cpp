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
        //TODOC Description of functions in RGBDVideoStream class
        .def(py::init<const char*, const char* >(), R"(TODOC)")
        .def("load", &I3DR::Phase::RGBDVideoStream::load, R"(TODOC)")
        .def("loadThreaded", &I3DR::Phase::RGBDVideoStream::loadThreaded, R"(TODOC)")
        .def("isLoadThreadRunning", &I3DR::Phase::RGBDVideoStream::isLoadThreadRunning, R"(TODOC)")
        .def("getLoadThreadResult", &I3DR::Phase::RGBDVideoStream::getLoadThreadResult, R"(TODOC)")
        .def("restart", &I3DR::Phase::RGBDVideoStream::restart, R"(TODOC)")
        .def("read", &I3DR::Phase::RGBDVideoStream::read, R"(TODOC)")
        .def("readThreaded", &I3DR::Phase::RGBDVideoStream::readThreaded, R"(TODOC)")
        .def("isReadThreadRunning", &I3DR::Phase::RGBDVideoStream::isReadThreadRunning, R"(TODOC)")
        .def("getReadThreadResult", &I3DR::Phase::RGBDVideoStream::getReadThreadResult, R"(TODOC)")
        .def("isOpened", &I3DR::Phase::RGBDVideoStream::isOpened, R"(TODOC)")
        .def("isLoaded", &I3DR::Phase::RGBDVideoStream::isLoaded, R"(TODOC)")
        .def("isFinished", &I3DR::Phase::RGBDVideoStream::isFinished, R"(TODOC)")
        .def("getWidth", &I3DR::Phase::RGBDVideoStream::getWidth, R"(TODOC)")
        .def("getHeight", &I3DR::Phase::RGBDVideoStream::getHeight, R"(TODOC)")
        .def("getHFOV", &I3DR::Phase::RGBDVideoStream::getHFOV, R"(TODOC)")
        .def("getDownsampleFactor", &I3DR::Phase::RGBDVideoStream::getDownsampleFactor, R"(TODOC)")
        .def("setDownsampleFactor", &I3DR::Phase::RGBDVideoStream::setDownsampleFactor, R"(TODOC)")
        .def("close", &I3DR::Phase::RGBDVideoStream::close, R"(TODOC)");
}