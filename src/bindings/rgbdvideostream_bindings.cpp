/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file rgbdvideostream_bindings.cpp
 * @brief RGBD Video Stream class python bindings
 * @details Python bindings generated using pybind11
 */

#include "pybind11/pybind11.h"
#include "ndarray_converter.h"

#include <phase/rgbdvideostream.h>

namespace py = pybind11;

void init_rgbdvideostream(py::module_ &m) {
    NDArrayConverter::init_numpy();

    py::class_<I3DR::Phase::RGBDVideoStream>(m, "RGBDVideoStream", py::module_local(), R"(
        Stream RGB and Depth video

        Parameters
        ----------
        rgb_video_filepath : str
        depth_video_filepath : str

        )")
    
        .def(py::init<const char*, const char* >(), R"(
            Class to load RGBD video stream

            )")
        .def("load", &I3DR::Phase::RGBDVideoStream::load, R"(
            Load camera

            Returns
            -------
            bool
                True if camera loaded
            )")
        .def("loadThreaded", &I3DR::Phase::RGBDVideoStream::loadThreaded, R"(
            Load thread

            )")
        .def("isLoadThreadRunning", &I3DR::Phase::RGBDVideoStream::isLoadThreadRunning, R"(
            Check if thread load is running

            Returns
            -------
            bool
                True if thread load is running
            )")
        .def("getLoadThreadResult", &I3DR::Phase::RGBDVideoStream::getLoadThreadResult, R"(
            Check if thread is loaded with result

            Returns
            -------
            bool
                True if thread is loaded with result
        )")
        .def("restart", &I3DR::Phase::RGBDVideoStream::restart, R"(
            Restart camera

            )")
        .def("read", &I3DR::Phase::RGBDVideoStream::read, R"(
            Read camera data

            Returns
            -------
            bool
                True if opened
            numpy.ndarray
                Image
            numpy.ndarray
                Image
            )")
        .def("readThreaded", &I3DR::Phase::RGBDVideoStream::readThreaded, R"(
            Read thread

            )")
        .def("isReadThreadRunning", &I3DR::Phase::RGBDVideoStream::isReadThreadRunning, R"(
            Check if thread read is running

            Returns
            -------
            bool
                True if thread read is running
            )")
        .def("getReadThreadResult", &I3DR::Phase::RGBDVideoStream::getReadThreadResult, R"(
            Get read thread

            Returns
            -------
            bool
                True if opened
            numpy.ndarray
                Image
            numpy.ndarray
                Image
            )")
        .def("isOpened", &I3DR::Phase::RGBDVideoStream::isOpened, R"(
            Check if RGBD video stream is opened

            Returns
            -------
            bool
                True if opened
            )")
        .def("isLoaded", &I3DR::Phase::RGBDVideoStream::isLoaded, R"(
            Check if RGBD video stream is loaded

            Returns
            -------
            bool
                True if loaded
            )")
        .def("isFinished", &I3DR::Phase::RGBDVideoStream::isFinished, R"(
            Check if RGBD video stream is finished

            Returns
            -------
            bool
                True if finished
            )")
        .def("getWidth", &I3DR::Phase::RGBDVideoStream::getWidth, R"(
            Get the width of image
            
            Returns
            -------
            value : int
                Width of image
            )")
        .def("getHeight", &I3DR::Phase::RGBDVideoStream::getHeight, R"(
            Get the height of image
            
            Returns
            -------
            value : int
                Height of image
            )")
        .def("getHFOV", &I3DR::Phase::RGBDVideoStream::getHFOV, R"(
            Get horitonzal Field Of View of camera from Q matrix

            Returns
            -------
            fov_x : float
                Horitonzal Field Of View of camera from Q matrix
            )")
        .def("getDownsampleFactor", &I3DR::Phase::RGBDVideoStream::getDownsampleFactor, R"(
            Get the value of Downsample Factor
            
            Returns
            -------
            value : float
                Downsampled factor
            )")
        .def("setDownsampleFactor", &I3DR::Phase::RGBDVideoStream::setDownsampleFactor, R"(
            Set downsample factor

            Parameters
            ----------
            value : float
                Desired value of downsample factor
            )")
        .def("close", &I3DR::Phase::RGBDVideoStream::close, R"(
            Close RGBD video stream
    
            )");
}