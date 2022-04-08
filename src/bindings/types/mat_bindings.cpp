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

    py::class_<I3DR::Phase::MatrixFloat>(m, "MatrixFloat", py::buffer_protocol())
    .def(py::init<int, int, int>())
    .def(py::init<const I3DR::Phase::MatrixFloat&>())
    .def("getRows", &I3DR::Phase::MatrixFloat::getRows)
    .def("getColumns", &I3DR::Phase::MatrixFloat::getColumns)
    .def("getLayers", &I3DR::Phase::MatrixFloat::getLayers)
    .def("setAt", &I3DR::Phase::MatrixFloat::setAt)
    .def("getAt", &I3DR::Phase::MatrixFloat::getAt)
    .def("getLength", &I3DR::Phase::MatrixFloat::getLength)
    .def("getSize", &I3DR::Phase::MatrixFloat::getSize)
    .def("isEmpty", &I3DR::Phase::MatrixFloat::isEmpty)
    .def(py::init([](py::array_t<float, py::array::c_style> const b) {
        return init_mat_buffer(b);
    }))
    .def_buffer([](I3DR::Phase::MatrixFloat &m) -> py::buffer_info {
        return get_mat_buffer_info(m);
    });

    py::class_<I3DR::Phase::MatrixUInt8>(m, "MatrixUInt8", py::buffer_protocol())
    .def(py::init<int, int, int>())
    .def(py::init<const I3DR::Phase::MatrixUInt8&>())
    .def("getRows", &I3DR::Phase::MatrixUInt8::getRows)
    .def("getColumns", &I3DR::Phase::MatrixUInt8::getColumns)
    .def("getLayers", &I3DR::Phase::MatrixUInt8::getLayers)
    .def("setAt", &I3DR::Phase::MatrixUInt8::setAt)
    .def("getAt", &I3DR::Phase::MatrixUInt8::getAt)
    .def("getLength", &I3DR::Phase::MatrixUInt8::getLength)
    .def("getSize", &I3DR::Phase::MatrixUInt8::getSize)
    .def("isEmpty", &I3DR::Phase::MatrixUInt8::isEmpty)
    .def(py::init([](py::array_t<uint8_t, py::array::c_style> const b) {
        return init_mat_buffer(b);
    }))
    .def_buffer([](I3DR::Phase::MatrixUInt8 &m) -> py::buffer_info {
        return get_mat_buffer_info(m);
    });
}