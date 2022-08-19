/*!
 * @authors Ben Knight (bknight@i3drobotics.com)
 * @date 2021-05-26
 * @copyright Copyright (c) I3D Robotics Ltd, 2021
 * 
 * @file bindings.cpp
 * @brief Python bindings module
 * @details Python bindings generated using pybind11.
 * Bindings for classes defined in other '_bindings' files
 * are brought together in this file to form the 'pyphase' module.
 */

#include "pybind11/pybind11.h"
#include "ndarray_converter.h"

namespace py = pybind11;

// pyphase
void init_version(py::module &);
void init_utils(py::module &);

// types
void init_mat(py::module &);
void init_stereo(py::module &);

// calib
void init_cameracalibration(py::module &);
void init_stereocalibration(py::module &);

// stereo camera
void init_cameradeviceinfo(py::module &);
void init_abstractstereocamera(py::module &);
void init_stereocamera(py::module &);
void init_pylonstereocamera(py::module &);
void init_uvcstereocamera(py::module &);
void init_deimosstereocamera(py::module &);
void init_phobosstereocamera(py::module &);
void init_titaniastereocamera(py::module &);

// stereo matcher
void init_abstractstereomatcher(py::module &);
void init_stereomatcher(py::module &);
void init_stereobm(py::module &);
void init_stereosgbm(py::module &);
void init_stereoi3drsgm(py::module &);

PYBIND11_MODULE(pyphase, m) {
    NDArrayConverter::init_numpy();

    m.doc() = R"(
        pyPhase is a python wrapper package over I3DR's Phase C++ library.
    )";
    
    // pyphase
    init_version(m);
    init_utils(m);

    // types
    py::module_ types_module = m.def_submodule("types", "custom Phase types");
    init_mat(types_module);
    init_stereo(types_module);

    // calib
    py::module_ calib_module = m.def_submodule("calib", "camera calibration");
    init_cameracalibration(calib_module);
    init_stereocalibration(calib_module);

    // stereo camera
    py::module_ stereocamera_module = m.def_submodule("stereocamera", "stereo camera");
    init_cameradeviceinfo(stereocamera_module);
    init_abstractstereocamera(stereocamera_module);
    init_stereocamera(stereocamera_module);
    init_pylonstereocamera(stereocamera_module);
    init_uvcstereocamera(stereocamera_module);
    init_deimosstereocamera(stereocamera_module);
    init_phobosstereocamera(stereocamera_module);
    init_titaniastereocamera(stereocamera_module);
    
    // stereo matcher
    py::module_ stereomatcher_module = m.def_submodule("stereomatcher", "stereo matcher");
    init_abstractstereomatcher(stereomatcher_module);
    init_stereomatcher(stereomatcher_module);
    init_stereobm(stereomatcher_module);
    init_stereosgbm(stereomatcher_module);
    init_stereoi3drsgm(stereomatcher_module);
}