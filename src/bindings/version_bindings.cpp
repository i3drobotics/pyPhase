/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file stereovision_bindings.cpp
 * @brief Phase class python bindings
 * @details Python bindings generated using pybind11
 */

#include "pybind11/pybind11.h"
#include "ndarray_converter.h"

#include <phase/version.h>

namespace py = pybind11;

void init_version(py::module_ &m) {
    m.def("getVersionString", &I3DR::Phase::getVersionString, R"(
        Get version of Phase

        Returns
        -------
        string : str
        )");
    m.def("getVersionMajor", &I3DR::Phase::getVersionMajor, R"(
        Get major of Phase

        Returns
        -------
        value : int
        )");
    m.def("getVersionMinor", &I3DR::Phase::getVersionMinor, R"(
        Get minor of Phase

        Returns
        -------
        value : int
        )");
    m.def("getVersionPatch", &I3DR::Phase::getVersionPatch, R"(
        Get version patch of Phase

        Returns
        -------
        value : int
        )");
}