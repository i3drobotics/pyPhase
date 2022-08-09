/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file common_bindings.cpp
 * @brief Common class python bindings
 * @details Python bindings generated using pybind11
 */

#include "pybind11/pybind11.h"
#include "ndarray_converter.h"

#include <phase/types/common.h>

namespace py = pybind11;

void init_common(py::module_ &m) {
    NDArrayConverter::init_numpy();
    //TODOC
    py::class_<I3DR::Phase::StereoImagePair>(m, "StereoImagePair", R"(TODOC)")
        .def(py::init<cv::Mat,cv::Mat>())
        .def_readwrite("left", &I3DR::Phase::StereoImagePair::left)
        .def_readwrite("right", &I3DR::Phase::StereoImagePair::right);
    //TODOC
    py::class_<I3DR::Phase::CameraReadResult>(m, "CameraReadResult", R"(TODOC)")
        .def(py::init<bool,cv::Mat,cv::Mat>())
        .def_readwrite("valid", &I3DR::Phase::CameraReadResult::valid)
        .def_readwrite("left", &I3DR::Phase::CameraReadResult::left)
        .def_readwrite("right", &I3DR::Phase::CameraReadResult::right);
    //TODOC
    py::class_<I3DR::Phase::StereoVisionReadResult>(m, "StereoVisionReadResult", R"(TODOC)")
        .def(py::init<bool,cv::Mat,cv::Mat,cv::Mat>())
        .def_readwrite("valid", &I3DR::Phase::StereoVisionReadResult::valid)
        .def_readwrite("left", &I3DR::Phase::StereoVisionReadResult::left)
        .def_readwrite("right", &I3DR::Phase::StereoVisionReadResult::right)
        .def_readwrite("disparity", &I3DR::Phase::StereoVisionReadResult::disparity);
    //TODOC
    py::class_<I3DR::Phase::StereoMatcherComputeResult>(m, "StereoMatcherComputeResult", R"(TODOC)")
        .def(py::init<bool,cv::Mat>())
        .def_readwrite("valid", &I3DR::Phase::StereoMatcherComputeResult::valid)
        .def_readwrite("disparity", &I3DR::Phase::StereoMatcherComputeResult::disparity);
    //TODOC
    py::class_<I3DR::Phase::RGBDVideoFrame>(m, "RGBDVideoFrame", R"(TODOC)")
        .def(py::init<bool,cv::Mat,cv::Mat>())
        .def_readwrite("valid", &I3DR::Phase::RGBDVideoFrame::valid)
        .def_readwrite("image", &I3DR::Phase::RGBDVideoFrame::image)
        .def_readwrite("depth", &I3DR::Phase::RGBDVideoFrame::depth);
    //TODOC
    py::class_<I3DR::Phase::Point2d>(m, "Point2d", R"(TODOC)")
        .def(py::init<double,double>())
        .def_readwrite("x", &I3DR::Phase::Point2d::x)
        .def_readwrite("y", &I3DR::Phase::Point2d::y);
    //TODOC
    py::class_<I3DR::Phase::Point2f>(m, "Point2f", R"(TODOC)")
        .def(py::init<float,float>())
        .def_readwrite("x", &I3DR::Phase::Point2f::x)
        .def_readwrite("y", &I3DR::Phase::Point2f::y);
    //TODOC
    py::class_<I3DR::Phase::Point2i>(m, "Point2i", R"(TODOC)")
        .def(py::init<int,int>())
        .def_readwrite("x", &I3DR::Phase::Point2i::x)
        .def_readwrite("y", &I3DR::Phase::Point2i::y);
    //TODOC
    py::enum_<I3DR::Phase::LeftOrRight>(m, "LeftOrRight", R"(TODOC)")
        .value("LEFT", I3DR::Phase::LeftOrRight::LEFT)
        .value("RIGHT", I3DR::Phase::LeftOrRight::RIGHT)
        .export_values();
    //TODOC
    py::enum_<I3DR::Phase::CameraDeviceType>(m, "CameraDeviceType", R"(TODOC)")
        .value("DEVICE_TYPE_GENERIC_PYLON", I3DR::Phase::CameraDeviceType::DEVICE_TYPE_GENERIC_PYLON)
        .value("DEVICE_TYPE_GENERIC_UVC", I3DR::Phase::CameraDeviceType::DEVICE_TYPE_GENERIC_UVC)
        .value("DEVICE_TYPE_DEIMOS", I3DR::Phase::CameraDeviceType::DEVICE_TYPE_DEIMOS)
        .value("DEVICE_TYPE_PHOBOS", I3DR::Phase::CameraDeviceType::DEVICE_TYPE_PHOBOS)
        .value("DEVICE_TYPE_TITANIA", I3DR::Phase::CameraDeviceType::DEVICE_TYPE_TITANIA)
        .value("DEVICE_TYPE_INVALID", I3DR::Phase::CameraDeviceType::DEVICE_TYPE_INVALID)
        .export_values();
    //TODOC
    py::enum_<I3DR::Phase::CameraInterfaceType>(m, "CameraInterfaceType", R"(TODOC)")
        .value("INTERFACE_TYPE_USB", I3DR::Phase::CameraInterfaceType::INTERFACE_TYPE_USB)
        .value("INTERFACE_TYPE_GIGE", I3DR::Phase::CameraInterfaceType::INTERFACE_TYPE_GIGE)
        .value("INTERFACE_TYPE_VIRTUAL", I3DR::Phase::CameraInterfaceType::INTERFACE_TYPE_VIRTUAL)
        .export_values();
    //TODOC
    py::enum_<I3DR::Phase::StereoMatcherType>(m, "StereoMatcherType", R"(TODOC)")
        .value("STEREO_MATCHER_BM", I3DR::Phase::StereoMatcherType::STEREO_MATCHER_BM)
        .value("STEREO_MATCHER_SGBM", I3DR::Phase::StereoMatcherType::STEREO_MATCHER_SGBM)
        .value("STEREO_MATCHER_I3DRSGM", I3DR::Phase::StereoMatcherType::STEREO_MATCHER_I3DRSGM)
        .value("STEREO_MATCHER_HOBM", I3DR::Phase::StereoMatcherType::STEREO_MATCHER_HOBM)
        .export_values();
}