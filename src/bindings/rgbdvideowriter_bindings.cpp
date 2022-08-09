/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file rgbdvideowriter_bindings.cpp
 * @brief RGBD Video Writer class python bindings
 * @details Python bindings generated using pybind11
 */

#include "pybind11/pybind11.h"
#include "ndarray_converter.h"

#include <phase/rgbdvideowriter.h>

namespace py = pybind11;

void init_rgbdvideowriter(py::module_ &m) {
    NDArrayConverter::init_numpy();

    py::class_<I3DR::Phase::RGBDVideoWriter>(m, "RGBDVideoWriter", py::module_local(), R"(
        RGBD Video Writer
        

        Write RGB and Depth video

        )")
        //TODOC Description of functions in RGBDVideoWriter class
        .def(py::init<const char*, const char*, int, int>(), R"(TODOC)")
        .def("add", &I3DR::Phase::RGBDVideoWriter::add, R"(TODOC)")
        .def("isOpened", &I3DR::Phase::RGBDVideoWriter::isOpened, R"(TODOC)")
        .def("save", &I3DR::Phase::RGBDVideoWriter::save, R"(TODOC)")
        .def("saveThreaded", &I3DR::Phase::RGBDVideoWriter::saveThreaded, R"(TODOC)")
        .def("isSaveThreadRunning", &I3DR::Phase::RGBDVideoWriter::isSaveThreadRunning, R"(TODOC)")
        .def("getSaveThreadResult", &I3DR::Phase::RGBDVideoWriter::getSaveThreadResult, R"(TODOC)")
        .def("close", &I3DR::Phase::RGBDVideoWriter::close, R"(TODOC)");
}