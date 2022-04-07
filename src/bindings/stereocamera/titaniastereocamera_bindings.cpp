/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file titaniastereocamera_bindings.cpp
 * @brief Titania Stereo Camera class python bindings
 * @details Python bindings generated using pybind11
 */


#include"pybind11/pybind11.h"
#include "ndarray_converter.h"

#include <phase/stereocamera/titaniastereocamera.h>

namespace py = pybind11;

void init_titaniastereocamera(py::module_ &m) {
    NDArrayConverter::init_numpy();

    py::class_<I3DR::Phase::TitaniaStereoCamera>(m, "TitaniaStereoCamera")
        .def(py::init<I3DR::Phase::CameraDeviceInfo>());
}