cmake_minimum_required(VERSION 3.9)

if (NOT (WIN32 OR UNIX))
    message(FATAL_ERROR "Unsupport OS. Only WIN32, UNIX currently supported.")
elseif (APPLE)
    message(FATAL_ERROR "APPLE not currently supported.")
endif ()

# Create temporary version file if it does not exist
# Automatic versioning is handelled by GitHub workflow so 0.0.0 is used when running locally
if(NOT EXISTS "${CMAKE_SOURCE_DIR}/version.txt")
    file(WRITE "${CMAKE_SOURCE_DIR}/version.txt" "0.0.0")
endif()

# Read version from file
file(READ "${CMAKE_SOURCE_DIR}/version.txt" VER)
string(REGEX REPLACE "(\r?\n)+" "" VER ${VER}) # remove newlines
message(STATUS "version: ${VER}")

# Remove prerelease suffix from version
string(FIND ${VER} "-" PREDASH)
if (NOT ${PREDASH} EQUAL -1)
    string(SUBSTRING ${VER} ${PREDASH} -1 VER_PRE)
    string(REPLACE "${VER_PRE}" "" VER ${VER})
endif()

# Define languages used in project
set(PROJECT_LANGS CXX)

project(pyphase LANGUAGES ${PROJECT_LANGS} VERSION ${VER})

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
# Get Phase library files
set(PHASE_ROOT_DIR "${Phase_DIR}/../..")
get_filename_component(PHASE_ROOT_DIR "${PHASE_ROOT_DIR}" ABSOLUTE)
set(PHASE_BIN_DIR 
    "${PHASE_ROOT_DIR}/bin"
)
set(PHASE_LIB_DIR 
    "${PHASE_ROOT_DIR}/lib"
)
if (WIN32)
    file (GLOB PHASE_LIBRARY_FILES
        "${PHASE_BIN_DIR}/*.dll"
    )
elseif(UNIX)
    file (GLOB PHASE_LIBRARY_FILES
        "${PHASE_LIB_DIR}/*.so*"
    )
    file (GLOB PHASE_I3DRSGM_LIBRARY_FILES
        "${PHASE_LIB_DIR}/i3drsgm/*.so*"
    )
endif()

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
    COMMAND ${CMAKE_COMMAND} -E copy_directory 
    ${PROJECT_SOURCE_DIR}/src/package/phase ${CMAKE_BINARY_DIR}/lib/phase
)

if (UNIX)
    add_custom_command(TARGET ${PROJECT_NAME} PRE_BUILD
        COMMAND mkdir -p $<TARGET_FILE_DIR:${PROJECT_NAME}>/i3drsgm)
    foreach(PHASE_LIBRARY_FILEPATH ${PHASE_I3DRSGM_LIBRARY_FILES})
        get_filename_component(PHASE_LIBRARY_FILE "${PHASE_LIBRARY_FILEPATH}" NAME)
        get_filename_component(PHASE_LIBRARY_FILE_EXT "${PHASE_LIBRARY_FILEPATH}" EXT)
        # copy library file to target directory
        add_custom_command(TARGET ${PROJECT_NAME} PRE_BUILD
                        COMMAND cp -a -u
                        ${PHASE_LIBRARY_FILEPATH} $<TARGET_FILE_DIR:${PROJECT_NAME}>/i3drsgm/)
    endforeach()
endif()

foreach(PHASE_LIBRARY_FILEPATH ${PHASE_LIBRARY_FILES})
    get_filename_component(PHASE_LIBRARY_FILE "${PHASE_LIBRARY_FILEPATH}" NAME)
    get_filename_component(PHASE_LIBRARY_FILE_EXT "${PHASE_LIBRARY_FILEPATH}" EXT)
    # copy library file to target directory
    if (WIN32)
        add_custom_command(TARGET ${PROJECT_NAME} PRE_BUILD
                           COMMAND ${CMAKE_COMMAND} -E copy 
                           ${PHASE_LIBRARY_FILEPATH} $<TARGET_FILE_DIR:${PROJECT_NAME}>)
    elseif (UNIX)
        add_custom_command(TARGET ${PROJECT_NAME} PRE_BUILD
                           COMMAND cp -a -u
                           ${PHASE_LIBRARY_FILEPATH} $<TARGET_FILE_DIR:${PROJECT_NAME}>)
        set(PHASE_LIBRARY_FILEPATH_FULL 
            ${CMAKE_BINARY_DIR}/lib/phase/${PHASE_LIBRARY_FILE}
        )
        # change rpath for dynamic library to find dependencies in local directory
        set(origin_var "\\$$ORIGIN")
        add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
            COMMAND if ! [ -L ${PHASE_LIBRARY_FILEPATH_FULL} ] \; then patchelf --set-rpath ${origin_var} ${PHASE_LIBRARY_FILEPATH_FULL} \; fi
        )
    endif()
endforeach()

if (UNIX)
    set(origin_var "\\$$ORIGIN:\\$$ORIGIN/i3drsgm")
    # change rpath for dynamic library to find dependencies in local directory
    add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
        COMMAND patchelf --set-rpath ${origin_var}
        ${CMAKE_BINARY_DIR}/lib/phase/libphase.so
    )
    add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
        COMMAND patchelf --set-rpath ${origin_var}
        $<TARGET_FILE:${PROJECT_NAME}>
    )
endif()
