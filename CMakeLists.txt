cmake_minimum_required(VERSION 3.9)

if (NOT (WIN32 OR UNIX OR APPLE))
    message(FATAL_ERROR "Unsupport os. WIN32, UNIX and APPLE currently supported.")
endif ()

# Create temporary version file if it does not exist
# Automatic versioning is handelled by GitHub workflow so 0.0.0 is used when running locally
if(NOT EXISTS "${CMAKE_SOURCE_DIR}/version.txt")
    file(WRITE "${CMAKE_SOURCE_DIR}/version.txt" "0.0.0")
endif()

# Read version from file
file(READ "${CMAKE_SOURCE_DIR}/version.txt" ver)
string(REGEX REPLACE "(\r?\n)+" "" ver ${ver}) # remove newlines
message("version: ${ver}")

# Define languages used in project
set(PROJECT_LANGS CXX)

project(pyphase LANGUAGES ${PROJECT_LANGS} VERSION ${ver})

# Define names
string(TOUPPER ${PROJECT_NAME} PROJECT_NAME_UPPER)
string(TOLOWER ${PROJECT_NAME} PROJECT_NAME_LOWER)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Define names
set(PYTHON_MODULE_INSTALL_DIR ${PROJECT_SOURCE_DIR}/phase)

# Find Phase
find_package(Phase REQUIRED)

include(FetchContent)

# Get pybind11 from git repository for python binding
FetchContent_Declare(
    pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11
    GIT_TAG        v2.9.1
    GIT_SHALLOW    ON
)

FetchContent_GetProperties(pybind11)
if(NOT pybind11_POPULATED)
    FetchContent_Populate(pybind11)
    add_subdirectory(${pybind11_SOURCE_DIR} ${pybind11_BINARY_DIR})
endif()
# find numpy location
execute_process(COMMAND ${PYTHON_EXECUTABLE} -c "import numpy; print(numpy.get_include())" OUTPUT_VARIABLE NUMPY_INCLUDE OUTPUT_STRIP_TRAILING_WHITESPACE)
message(STATUS "NUMPY_INCLUDE: " ${NUMPY_INCLUDE})
if ("${NUMPY_INCLUDE}" STREQUAL "")
    message(FATAL_ERROR "\nFailed to find required python package numpy.\nInstall using `pip install numpy`.")
endif()

# Get pybind11_opencv_numpy from git repository for opencv->numpy conversion
FetchContent_Declare(
    pybind11_opencv_numpy
    GIT_REPOSITORY https://github.com/edmBernard/pybind11_opencv_numpy
    GIT_SHALLOW    ON
)
if(NOT pybind11_opencv_numpy_POPULATED)
    FetchContent_Populate(pybind11_opencv_numpy)
endif()

# Define python binding include/source files
file (GLOB SRC_FILES
    "src/bindings/*.cpp"
    "src/bindings/types/*.cpp"
    "src/bindings/calib/*.cpp"
    "src/bindings/stereocamera/*.cpp"
    "src/bindings/stereomatcher/*.cpp"
)
set (SRC_FILES
    ${SRC_FILES}
    "${pybind11_opencv_numpy_SOURCE_DIR}/ndarray_converter.cpp"
)

# Build python module using pybind11
pybind11_add_module(${PROJECT_NAME} ${SRC_FILES})
target_link_libraries(${PROJECT_NAME} PRIVATE ${Phase_LIBS})
target_include_directories(${PROJECT_NAME} PRIVATE
    ${Phase_INCLUDE_DIRS}
    ${NUMPY_INCLUDE}
    ${pybind11_opencv_numpy_SOURCE_DIR}
)
target_compile_definitions(${PROJECT_NAME} PRIVATE ${Phase_DEFINITIONS})
set_target_properties(${PROJECT_NAME_LOWER} PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib/phase
    LIBRARY_OUTPUT_DIRECTORY_DEBUG ${CMAKE_BINARY_DIR}/lib/phase
    LIBRARY_OUTPUT_DIRECTORY_RELEASE ${CMAKE_BINARY_DIR}/lib/phase
)

add_custom_command(TARGET ${PROJECT_NAME} PRE_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_directory ${PROJECT_SOURCE_DIR}/src/package/phase ${CMAKE_BINARY_DIR}/lib/phase
)

install(TARGETS ${PROJECT_NAME}
    COMPONENT python
    RUNTIME DESTINATION ${PYTHON_MODULE_INSTALL_DIR}
    LIBRARY DESTINATION ${PYTHON_MODULE_INSTALL_DIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)
