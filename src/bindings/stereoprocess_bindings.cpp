/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file stereoprocess_bindings.cpp
 * @brief Stereo Filesystem python bindings
 * @details Python bindings generated using pybind11
 */

#include "pybind11/pybind11.h"
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include "ndarray_converter.h"

#include <phase/stereoprocess.h>

namespace py = pybind11;

void init_stereoprocess(py::module_ &m) {
    NDArrayConverter::init_numpy();
    m.def("processStereoFiles", &I3DR::Phase::processStereoFiles,
        py::arg("stereo_params"), py::arg("left_yaml"),  py::arg("right_yaml"),
        py::arg("left_image_path"), py::arg("right_image_path"),  py::arg("output_folder"),
        py::arg("rectify") = true, R"(
            Process stereo calibration files, returns error if failed

            )");

    m.def("processStereo", &I3DR::Phase::processStereo,
        py::arg("stereo_params"), py::arg("left_image"),  py::arg("right_image"),
        py::arg("calibration"), py::arg("rectify") = true, R"(
            Load in calibration files and process stereo images, returns error if failed

            )");
}