/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file abstractstereocamera_bindings.cpp
 * @brief Abstract Stereo Camera class python bindings
 * @details Python bindings generated using pybind11
 */

#include"pybind11/pybind11.h"
#include "ndarray_converter.h"

#include <phase/stereocamera/abstractstereocamera.h>

namespace py = pybind11;

void init_abstractstereocamera(py::module_ &m) {
    NDArrayConverter::init_numpy();

    py::class_<I3DR::Phase::CameraReadResult>(m, "CameraReadResult")
        .def(py::init<bool,cv::Mat,cv::Mat>())
        .def_readwrite("valid", &I3DR::Phase::CameraReadResult::valid)
        .def_readwrite("left_image", &I3DR::Phase::CameraReadResult::left_image)
        .def_readwrite("right_image", &I3DR::Phase::CameraReadResult::right_image);

    py::class_<I3DR::Phase::AbstractStereoCamera>(m, "AbstractStereoCamera")
        .def(py::init<I3DR::Phase::CameraDeviceInfo>());

    //TODO add callback funtion for read results (https://pybind11.readthedocs.io/en/stable/advanced/cast/functional.html)

}