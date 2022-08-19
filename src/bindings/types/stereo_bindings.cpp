/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file stereo_bindings.cpp
 * @brief Stereo types python bindings
 * @details Python bindings generated using pybind11
 */

#include "pybind11/pybind11.h"
#include "ndarray_converter.h"

#include <phase/types/stereo.h>

namespace py = pybind11;

void init_stereo(py::module_ &m) {
    NDArrayConverter::init_numpy();
    py::class_<I3DR::Phase::StereoImagePair>(m, "StereoImagePair", R"(
        Structure of StereoImagePair

        )")
        .def(py::init<cv::Mat,cv::Mat>())
        .def_readwrite("left", &I3DR::Phase::StereoImagePair::left)
        .def_readwrite("right", &I3DR::Phase::StereoImagePair::right);

}