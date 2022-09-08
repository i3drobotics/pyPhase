/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file stereocamera_bindings.cpp
 * @brief Stereo Camera class python bindings
 * @details Python bindings generated using pybind11
 */

#include "pybind11/pybind11.h"
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include "ndarray_converter.h"

#include <phase/stereocamera/stereocamera.h>

namespace py = pybind11;

void init_stereocamera(py::module_ &m) {
    NDArrayConverter::init_numpy();
    // Create a stereo camera variable stored with device info 
    m.def("createStereoCamera", &I3DR::Phase::createStereoCamera, py::return_value_policy::reference, R"(
            Read device type and return in related camera variable
            
    )");
}