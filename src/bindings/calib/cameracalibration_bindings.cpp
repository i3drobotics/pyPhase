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
    //TODOC Description of the class and functions in CalibrationFileType class
    py::enum_<I3DR::Phase::CalibrationFileType>(m, "CalibrationFileType", R"(TODOC)")
        .value("ROS_YAML", I3DR::Phase::CalibrationFileType::ROS_YAML, R"(TODOC)")
        .value("OPENCV_YAML", I3DR::Phase::CalibrationFileType::OPENCV_YAML, R"(TODOC)")
        .value("INVALID", I3DR::Phase::CalibrationFileType::INVALID, R"(TODOC)")
        .export_values();
    //TODOC Description of the class and functions in CameraCalibration class
    py::class_<I3DR::Phase::CameraCalibration>(m, "CameraCalibration", R"(TODOC)")
        .def(py::init<const char*>(), R"(TODOC)")
        .def(py::init<int, int, cv::Mat, cv::Mat, cv::Mat, cv::Mat>(), R"(TODOC)")
        .def_static("calibrationFromIdeal", &I3DR::Phase::CameraCalibration::calibrationFromIdeal, R"(TODOC)")
        //.def("rectify", &I3DR::Phase::CameraCalibration::rectify)
        .def("remapPoint", &I3DR::Phase::CameraCalibration::remapPoint, R"(TODOC)")
        .def("isValid", &I3DR::Phase::CameraCalibration::isValid, R"(TODOC)")
        .def("setDownsampleFactor", &I3DR::Phase::CameraCalibration::setDownsampleFactor, R"(TODOC)")
        .def("getDownsampleFactor", &I3DR::Phase::CameraCalibration::getDownsampleFactor, R"(TODOC)")
        .def("getImageHeight", &I3DR::Phase::CameraCalibration::getImageHeight, R"(TODOC)")
        .def("getImageWidth", &I3DR::Phase::CameraCalibration::getImageWidth, R"(TODOC)")
        .def("getCameraMatrix", &I3DR::Phase::CameraCalibration::getCameraMatrix, R"(TODOC)")
        .def("getDistortionCoefficients", &I3DR::Phase::CameraCalibration::getDistortionCoefficients, R"(TODOC)")
        .def("getRectificationMatrix", &I3DR::Phase::CameraCalibration::getRectificationMatrix, R"(TODOC)")
        .def("getProjectionMatrix", &I3DR::Phase::CameraCalibration::getProjectionMatrix, R"(TODOC)")
        .def("getCameraFX", &I3DR::Phase::CameraCalibration::getCameraFX, R"(TODOC)")
        .def("getCameraFY", &I3DR::Phase::CameraCalibration::getCameraFY, R"(TODOC)")
        .def("getCameraCX", &I3DR::Phase::CameraCalibration::getCameraCX, R"(TODOC)")
        .def("getCameraCY", &I3DR::Phase::CameraCalibration::getCameraCY, R"(TODOC)")
        .def("getProjectionFX", &I3DR::Phase::CameraCalibration::getProjectionFX, R"(TODOC)")
        .def("getProjectionFY", &I3DR::Phase::CameraCalibration::getProjectionFY, R"(TODOC)")
        .def("getProjectionCX", &I3DR::Phase::CameraCalibration::getProjectionCX, R"(TODOC)")
        .def("getProjectionCY", &I3DR::Phase::CameraCalibration::getProjectionCY, R"(TODOC)")
        .def("getProjectionTX", &I3DR::Phase::CameraCalibration::getProjectionTX, R"(TODOC)");
}