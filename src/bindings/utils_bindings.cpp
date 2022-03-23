/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file utils_bindings.cpp
 * @brief Stereo Utility functions python bindings
 * @details Python bindings generated using pybind11
 */

#include"pybind11/pybind11.h"
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include "ndarray_converter.h"

#include <phase/utils.h>

namespace py = pybind11;

void init_utils(py::module_ &m) {
    NDArrayConverter::init_numpy();

    m.def("scaleImage", &I3DR::Phase::scaleImage);
    // m.def("toMono", &I3DR::Phase::toMono);
    m.def("normaliseDisparity", &I3DR::Phase::normaliseDisparity);
    m.def("bgra2rgba", &I3DR::Phase::bgra2rgba);
    m.def("bgr2rgba", &I3DR::Phase::bgr2rgba);
    m.def("bgr2bgra", &I3DR::Phase::bgr2bgra);
    m.def("disparity2xyz", &I3DR::Phase::disparity2xyz);
    m.def("disparity2depth", &I3DR::Phase::disparity2depth);
    m.def("xyz2depth", &I3DR::Phase::xyz2depth);
    m.def("depth2xyz", &I3DR::Phase::depth2xyz);
    m.def("showImage", &I3DR::Phase::showImage);
    m.def("readImage", &I3DR::Phase::readImage);
    m.def("flip", &I3DR::Phase::flip);
    m.def("savePLY", &I3DR::Phase::savePLY);
    m.def("cvMatIsEqual", &I3DR::Phase::cvMatIsEqual);
}