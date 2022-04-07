/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file utils_bindings.cpp
 * @brief Stereo Utility functions python bindings
 * @details Python bindings generated using pybind11
 */

#include"pybind11/pybind11.h"
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include "ndarray_converter.h"

#include <phase/utils.h>

namespace py = pybind11;

void init_utils(py::module_ &m) {
    NDArrayConverter::init_numpy();

    m.def("scaleImage", &I3DR::Phase::scaleImage, R"(
        Scale image to a new size.

        Parameters
        ----------
        image : numpy.ndarray
            Image to scale
        scale_factor : float
            Scale factor to apply to image

        Returns
        -------
        numpy.ndarray
            Scaled image
        )");
    // m.def("toMono", &I3DR::Phase::toMono);
    m.def("normaliseDisparity", &I3DR::Phase::normaliseDisparity, R"(
        Normalise disparity image.

        Parameters
        ----------
        disparity : numpy.ndarray
            Dispairty image to normalise

        Returns
        -------
        numpy.ndarray
            Normalised disparity image
        )");
    m.def("bgra2rgba", &I3DR::Phase::bgra2rgba, R"(
        Convert BGRA image to RGBA.

        Parameters
        ----------
        bgra : numpy.ndarray
            BGRA image to convert

        Returns
        -------
        numpy.ndarray
            RGBA image
        )");
    m.def("bgr2rgba", &I3DR::Phase::bgr2rgba, R"(
        Convert BGR image to RGBA.

        Parameters
        ----------
        bgr : numpy.ndarray
            BGR image to convert

        Returns
        -------
        numpy.ndarray
            RGBA image
        )");
    m.def("bgr2bgra", &I3DR::Phase::bgr2bgra, R"(
        Convert BGR image to BGRA.

        Parameters
        ----------
        bgr : numpy.ndarray
            BGR image to convert

        Returns
        -------
        numpy.ndarray
            BGRA image
        )");
    m.def("disparity2xyz", &I3DR::Phase::disparity2xyz, R"(
        Calculate point cloud (xyz) from disparity image.

        Parameters
        ----------
        disparity : numpy.ndarray
            Disparity image
        Q: numpy.ndarray
            Q Matrix from calibration (e.g. 'calibration.getQ()')

        Returns
        -------
        numpy.ndarray
            Point clouds (xyz)
        )");
    m.def("disparity2depth", &I3DR::Phase::disparity2depth, R"(
        Calculate depth image from disparity image.

        Parameters
        ----------
        disparity : numpy.ndarray
            Disparity image
        Q: numpy.ndarray
            Q Matrix from calibration (e.g. 'calibration.getQ()')

        Returns
        -------
        numpy.ndarray
            Depth image
        )");
    m.def("xyz2depth", &I3DR::Phase::xyz2depth, R"(
        Calculate depth image from point cloud (xyz).

        Parameters
        ----------
        xyz : numpy.ndarray
            Point cloud (xyz)

        Returns
        -------
        numpy.ndarray
            Depth image
        )");
    m.def("depth2xyz", &I3DR::Phase::depth2xyz, R"(
        Calculate Point cloud (xyz) from depth image.

        Parameters
        ----------
        xyz : numpy.ndarray
            Point cloud (xyz)
        hfov : float
            Horizontal field of view (degrees)

        Returns
        -------
        numpy.ndarray
            Point cloud (xyz)
        )");
    m.def("showImage", &I3DR::Phase::showImage, R"(
        Display image in GUI window.

        Parameters
        ----------
        window_name : str
            Name of window
        image : numpy.ndarray
            Point cloud (xyz)
        )");
    m.def("readImage", &I3DR::Phase::readImage, R"(
        Read image from file.

        Parameters
        ----------
        image_filepath : str
            Filepath of image

        Returns
        -------
        numpy.ndarray
            Image
        )");
    m.def("flip", &I3DR::Phase::flip, R"(
        Flip image horizontally or vertically based on flip code.

        Parameters
        ----------
        image : numpy.ndarray
            Image to flip
        flip_code : int
            Flip code (0 = horizontal, 1 = vertical)

        Returns
        -------
        numpy.ndarray
            Flipped image
        )");
    m.def("savePLY", &I3DR::Phase::savePLY, R"(
        Save point cloud to PLY file.

        Parameters
        ----------
        ply_filepath : str
            Filepath of PLY file
        xyz : numpy.ndarray
            Point cloud (xyz)
        rgb : numpy.ndarray
            RGB image for point cloud colours

        Returns
        -------
        bool
            True if successful
        )");
    m.def("cvMatIsEqual", &I3DR::Phase::cvMatIsEqual, R"(
        Check if two cv::Mat objects are equal.

        Parameters
        ----------
        mat1 : cv::Mat
            First cv::Mat object
        mat2 : cv::Mat
            Second cv::Mat object

        Returns
        -------
        bool
            True if equal
        )");
}