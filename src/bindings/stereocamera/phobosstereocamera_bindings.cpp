/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file phobosstereocamera_bindings.cpp
 * @brief Phobos Stereo Camera class python bindings
 * @details Python bindings generated using pybind11
 */

#include"pybind11/pybind11.h"
#include "ndarray_converter.h"

#include <phase/stereocamera/phobosstereocamera.h>

namespace py = pybind11;

void init_phobosstereocamera(py::module_ &m) {
    NDArrayConverter::init_numpy();

    py::class_<I3DR::Phase::PhobosStereoCamera>(m, "PhobosStereoCamera")
        .def(py::init<I3DR::Phase::CameraDeviceInfo>());

}