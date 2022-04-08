/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file stereocalibration_bindings.cpp
 * @brief Stereo Calibration class python bindings
 * @details Python bindings generated using pybind11
 */

#include "pybind11/pybind11.h"
#include "ndarray_converter.h"

#include <phase/calib/cameracalibration.h>

namespace py = pybind11;

void init_cameracalibration(py::module_ &m) {
    NDArrayConverter::init_numpy();

    py::enum_<I3DR::Phase::CalibrationFileType>(m, "CalibrationFileType")
        .value("ROS_YAML", I3DR::Phase::CalibrationFileType::ROS_YAML)
        .value("OPENCV_YAML", I3DR::Phase::CalibrationFileType::OPENCV_YAML)
        .value("INVALID", I3DR::Phase::CalibrationFileType::INVALID)
        .export_values();
    
    py::class_<I3DR::Phase::CameraCalibration>(m, "CameraCalibration")
        .def(py::init<const char*>())
        .def(py::init<int, int, cv::Mat, cv::Mat, cv::Mat, cv::Mat>())
        .def_static("calibrationFromIdeal", &I3DR::Phase::CameraCalibration::calibrationFromIdeal)
        //.def("rectify", &I3DR::Phase::CameraCalibration::rectify)
        .def("remapPoint", &I3DR::Phase::CameraCalibration::remapPoint)
        .def("isValid", &I3DR::Phase::CameraCalibration::isValid)
        .def("setDownsampleFactor", &I3DR::Phase::CameraCalibration::setDownsampleFactor)
        .def("getDownsampleFactor", &I3DR::Phase::CameraCalibration::getDownsampleFactor)
        .def("getImageHeight", &I3DR::Phase::CameraCalibration::getImageHeight)
        .def("getImageWidth", &I3DR::Phase::CameraCalibration::getImageWidth)
        .def("getCameraMatrix", &I3DR::Phase::CameraCalibration::getCameraMatrix)
        .def("getDistortionCoefficients", &I3DR::Phase::CameraCalibration::getDistortionCoefficients)
        .def("getRectificationMatrix", &I3DR::Phase::CameraCalibration::getRectificationMatrix)
        .def("getProjectionMatrix", &I3DR::Phase::CameraCalibration::getProjectionMatrix)
        .def("getCameraFX", &I3DR::Phase::CameraCalibration::getCameraFX)
        .def("getCameraFY", &I3DR::Phase::CameraCalibration::getCameraFY)
        .def("getCameraCX", &I3DR::Phase::CameraCalibration::getCameraCX)
        .def("getCameraCY", &I3DR::Phase::CameraCalibration::getCameraCY)
        .def("getProjectionFX", &I3DR::Phase::CameraCalibration::getProjectionFX)
        .def("getProjectionFY", &I3DR::Phase::CameraCalibration::getProjectionFY)
        .def("getProjectionCX", &I3DR::Phase::CameraCalibration::getProjectionCX)
        .def("getProjectionCY", &I3DR::Phase::CameraCalibration::getProjectionCY)
        .def("getProjectionTX", &I3DR::Phase::CameraCalibration::getProjectionTX);
}