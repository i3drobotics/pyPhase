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
        
        .def(py::init<const char*, const char*, int, int>(), R"(
            Class to write RGBD video
            
            )")
        .def("add", &I3DR::Phase::RGBDVideoWriter::add, R"(
            Add colour channel RGB and the depth to form 4 channels

            Parameters
            ----------
            rgb : numpy.ndarray
            depth : numpy.ndarray
            )")
        .def("isOpened", &I3DR::Phase::RGBDVideoWriter::isOpened, R"(
            Check if RGBD writer is opened

            Returns
            -------
            bool
                True if RGBD writer is opened
            )")
        .def("save", &I3DR::Phase::RGBDVideoWriter::save, R"(
            Save RGBD video

            Returns
            -------
            bool
                True if RGBD video is saved
            )")
        .def("saveThreaded", &I3DR::Phase::RGBDVideoWriter::saveThreaded, R"(
            Save threaded

            )")
        .def("isSaveThreadRunning", &I3DR::Phase::RGBDVideoWriter::isSaveThreadRunning, R"(
            Check if save thread is running

            Returns
            -------
            bool
                True if save thread is running
            )")
        .def("getSaveThreadResult", &I3DR::Phase::RGBDVideoWriter::getSaveThreadResult, R"(
            Get save thread
            
            Returns
            -------
            bool
                True if equal
            )")
        .def("close", &I3DR::Phase::RGBDVideoWriter::close, R"(
            Close RGBD video writer

            )");
}