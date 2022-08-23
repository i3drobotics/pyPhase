/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file mat_bindings.cpp
 * @brief Matrix class python bindings
 * @details Python bindings generated using pybind11
 */

#include "pybind11/pybind11.h"
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include "ndarray_converter.h"

#include <phase/types/mat.h>

namespace py = pybind11;

template <typename T>
py::buffer_info get_mat_buffer_info(I3DR::Phase::Matrix<T> &m){
    return py::buffer_info(
                m.getData(),                            /* Pointer to buffer */
                sizeof(T),                       /* Size of one scalar */
                pybind11::format_descriptor<T>::format(), /* Python struct-style format descriptor */
                3,                                   /* Number of dimensions */
                { m.getRows(), m.getColumns(), m.getLayers() },              /* Buffer dimensions */
                { sizeof(T) * m.getLayers() * m.getColumns(),
                  sizeof(T) * m.getLayers(),          /* Strides (in bytes) for each index */
                  sizeof(T) }
            );
}

template <typename T>
I3DR::Phase::Matrix<T>* init_mat_buffer(py::array_t<T, py::array::c_style> const b){
    py::buffer_info info = b.request();
    if (info.format != py::format_descriptor<T>::format())
        throw std::runtime_error("Incompatible buffer format!");
    int rows = (int)info.shape[0];
    int cols = (int)info.shape[1];
    int layers = (int)info.shape[2];
    return new I3DR::Phase::Matrix<T>(rows, cols, layers, (T*)info.ptr);
}

void init_mat(py::module_ &m) {
    NDArrayConverter::init_numpy();
    // Class of accessing buffer matrix data
    py::class_<I3DR::Phase::MatrixFloat>(m, "MatrixFloat", py::buffer_protocol(), R"(
        Class to access data float type matrix
        
        )")
    .def(py::init<>(), R"(
        Matrix empty assignment contructor

        )")
    .def(py::init<int, int, int>(), R"(
        Access float type matrix data

        Parameters
        ----------
        rows : int
        cols : int
        channels : int

        )")
    .def(py::init<const I3DR::Phase::MatrixFloat&>(), R"(
        Access float type matrix data

        )")
    .def("getRows", &I3DR::Phase::MatrixFloat::getRows, R"(
        Get rows of the float type matrix
        
        Returns
        -------
        rows : int
            Row of the matrix
        )")
    .def("getColumns", &I3DR::Phase::MatrixFloat::getColumns, R"(
        Get columns of the float type matrix
        
        Returns
        -------
        columns : int
            Column of the matrix
        )")
    .def("getLayers", &I3DR::Phase::MatrixFloat::getLayers, R"(
        Get layers of the float type matrix
        
        Returns
        -------
        layers : int
            Layer of the matrix
        )")
    .def("setAt", &I3DR::Phase::MatrixFloat::setAt, R"(
        Set the data value to the desired index of matrix

        Parameters
        ----------
        row : int
        column : int
        layer : int
        value : float

    )")
    .def("getAt", &I3DR::Phase::MatrixFloat::getAt, R"(
        Get the data of the desired index of matrix

        Parameters
        ----------
        row : int
        column : int
        layer : int

        Returns
        -------
        data : float
            The value of data in float
        )")
    .def("getLength", &I3DR::Phase::MatrixFloat::getLength, R"(
        Get length of the float type matrix, defines as rows X columns X layer
        
        Returns
        -------
        value : int
            Length of the matrix
        )")
    .def("getSize", &I3DR::Phase::MatrixFloat::getSize, R"(
        Get size of the float type matrix
        
        Returns
        -------
        value : int
            Size of the matrix
        )")
    .def("isEmpty", &I3DR::Phase::MatrixFloat::isEmpty, R"(
        Check if the matrix is empty
        
        Returns
        -------
        bool
            True if empty
        )")
    .def(py::init([](py::array_t<float, py::array::c_style> const b) {
        return init_mat_buffer(b);
    }), R"(Access float type matrix data)")
    .def_buffer([](I3DR::Phase::MatrixFloat &m) -> py::buffer_info {
        return get_mat_buffer_info(m);
    });

    py::class_<I3DR::Phase::MatrixUInt8>(m, "MatrixUInt8", py::buffer_protocol(), R"(
        Class to access data UInt8 type matrix

        )")
    .def(py::init<>(), R"(
        Matrix empty assignment contructor

        )")
    .def(py::init<int, int, int>(), R"(
        Access UInt8 type matrix data

        Parameters
        ----------
        rows : int
        cols : int
        channels : int
        )")
    .def(py::init<const I3DR::Phase::MatrixUInt8&>(), R"(
        Access UInt8 type matrix data

        )")
    .def("getRows", &I3DR::Phase::MatrixUInt8::getRows, R"(
        Get rows of the UInt8 type matrix
        
        Returns
        -------
        rows : int
            Row of the matrix
        )")
    .def("getColumns", &I3DR::Phase::MatrixUInt8::getColumns, R"(
        Get columns of the UInt8 type matrix
        
        Returns
        -------
        columns : int
            Column of the matrix
        )")
    .def("getLayers", &I3DR::Phase::MatrixUInt8::getLayers, R"(
        Get layers of the UInt8 type matrix
        
        Returns
        -------
        layers : int
            Layer of the matrix
        )")
    .def("setAt", &I3DR::Phase::MatrixUInt8::setAt, R"(
        Set the data value to the desired index of matrix

        Parameters
        ----------
        row : int
        column : int
        layer : int
        value : int
        )")
    .def("getAt", &I3DR::Phase::MatrixUInt8::getAt, R"(
        Get the data of the desired index of matrix

        Parameters
        ----------
        row : int
        column : int
        layer : int

        Returns
        -------
        data : int
            The value of data in float
        )")
    .def("getLength", &I3DR::Phase::MatrixUInt8::getLength, R"(
        Get length of the UInt8 type matrix, defines as rows X columns X layer
        
        Returns
        -------
        value : int
            Length of the matrix
        )")
    .def("getSize", &I3DR::Phase::MatrixUInt8::getSize, R"(
        Get size of the UInt8 type matrix
        
        Returns
        -------
        value : int
            Size of the matrix
        )")
    .def("isEmpty", &I3DR::Phase::MatrixUInt8::isEmpty, R"(
        Check if the matrix is empty
        
        Returns
        -------
        bool
            True if empty
        )")
    .def(py::init([](py::array_t<uint8_t, py::array::c_style> const b) {
        return init_mat_buffer(b);
    }), R"(Access UInt8 type matrix data)")
    .def_buffer([](I3DR::Phase::MatrixUInt8 &m) -> py::buffer_info {
        return get_mat_buffer_info(m);
    });
}