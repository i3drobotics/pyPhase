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

//TODOC
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

//TODOC
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
    // TODOC Description of the class and the functions of MatrixFloat class
    py::class_<I3DR::Phase::MatrixFloat>(m, "MatrixFloat", py::buffer_protocol())
    .def(py::init<int, int, int>(), R"(TODOC)")
    .def(py::init<const I3DR::Phase::MatrixFloat&>(), R"(TODOC)")
    .def("getRows", &I3DR::Phase::MatrixFloat::getRows, R"(TODOC)")
    .def("getColumns", &I3DR::Phase::MatrixFloat::getColumns, R"(TODOC)")
    .def("getLayers", &I3DR::Phase::MatrixFloat::getLayers, R"(TODOC)")
    .def("setAt", &I3DR::Phase::MatrixFloat::setAt, R"(TODOC)")
    .def("getAt", &I3DR::Phase::MatrixFloat::getAt, R"(TODOC)")
    .def("getLength", &I3DR::Phase::MatrixFloat::getLength, R"(TODOC)")
    .def("getSize", &I3DR::Phase::MatrixFloat::getSize, R"(TODOC)")
    .def("isEmpty", &I3DR::Phase::MatrixFloat::isEmpty, R"(TODOC)")
    .def(py::init([](py::array_t<float, py::array::c_style> const b) {
        return init_mat_buffer(b);
    }), R"(TODOC)")
    .def_buffer([](I3DR::Phase::MatrixFloat &m) -> py::buffer_info {
        return get_mat_buffer_info(m);
    });

    // TODOC Description of the class and the functions of MatrixUInt8 class
    py::class_<I3DR::Phase::MatrixUInt8>(m, "MatrixUInt8", py::buffer_protocol())
    .def(py::init<int, int, int>(), R"(TODOC)")
    .def(py::init<const I3DR::Phase::MatrixUInt8&>(), R"(TODOC)")
    .def("getRows", &I3DR::Phase::MatrixUInt8::getRows, R"(TODOC)")
    .def("getColumns", &I3DR::Phase::MatrixUInt8::getColumns, R"(TODOC)")
    .def("getLayers", &I3DR::Phase::MatrixUInt8::getLayers, R"(TODOC)")
    .def("setAt", &I3DR::Phase::MatrixUInt8::setAt, R"(TODOC)")
    .def("getAt", &I3DR::Phase::MatrixUInt8::getAt, R"(TODOC)")
    .def("getLength", &I3DR::Phase::MatrixUInt8::getLength, R"(TODOC)")
    .def("getSize", &I3DR::Phase::MatrixUInt8::getSize, R"(TODOC)")
    .def("isEmpty", &I3DR::Phase::MatrixUInt8::isEmpty, R"(TODOC)")
    .def(py::init([](py::array_t<uint8_t, py::array::c_style> const b) {
        return init_mat_buffer(b);
    }), R"(TODOC)")
    .def_buffer([](I3DR::Phase::MatrixUInt8 &m) -> py::buffer_info {
        return get_mat_buffer_info(m);
    });
}