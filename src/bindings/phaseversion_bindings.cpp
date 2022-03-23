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

#include <phase/phaseversion.h>

namespace py = pybind11;

void init_phaseversion(py::module_ &m) {
    m.def("getVersionString", &I3DR::Phase::getVersionString);
    m.def("getVersionMajor", &I3DR::Phase::getVersionMajor);
    m.def("getVersionMinor", &I3DR::Phase::getVersionMinor);
    m.def("getVersionPatch", &I3DR::Phase::getVersionPatch);
}