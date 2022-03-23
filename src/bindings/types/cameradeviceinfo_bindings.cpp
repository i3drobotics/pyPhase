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

#include <phase/types/cameradeviceinfo.h>

namespace py = pybind11;

void init_cameradeviceinfo(py::module_ &m) {
    NDArrayConverter::init_numpy();

    py::class_<I3DR::Phase::CameraDeviceInfo>(m, "CameraDeviceInfo")
        .def(py::init<const char*,const char*,const char*,
            I3DR::Phase::CameraDeviceType,I3DR::Phase::CameraInterfaceType>())
        .def("setLeftCameraSerial", &I3DR::Phase::CameraDeviceInfo::setLeftCameraSerial)
        .def("setRightCameraSerial", &I3DR::Phase::CameraDeviceInfo::setRightCameraSerial)
        .def("setUniqueSerial", &I3DR::Phase::CameraDeviceInfo::setUniqueSerial)
        .def("getLeftCameraSerial", &I3DR::Phase::CameraDeviceInfo::getLeftCameraSerial)
        .def("getRightCameraSerial", &I3DR::Phase::CameraDeviceInfo::getRightCameraSerial)
        .def("getUniqueSerial", &I3DR::Phase::CameraDeviceInfo::getUniqueSerial)
        .def_readwrite("device_type", &I3DR::Phase::CameraDeviceInfo::device_type)
        .def_readwrite("interface_type", &I3DR::Phase::CameraDeviceInfo::interface_type);
}