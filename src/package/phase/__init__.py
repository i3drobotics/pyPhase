#!/usr/bin/env python3

"""!
 @authors Ben Knight (bknight@i3drobotics.com)
 @date 2021-05-26
 @copyright Copyright (c) I3D Robotics Ltd, 2021
 @file __init__.py
 @brief Entry file for python module
 @details Adds libraries folder to path
"""

import os
import sys


def get_phase_url(phase_version):
    return "https://github.com/i3drobotics/phase/releases/tag/v{}".format(
        phase_version)


def import_phase():
    if sys.platform == "win32":
        lib_path_list = []
        # pyPhase module path
        PYPHASE_PATH = os.path.abspath(
            os.path.dirname(os.path.realpath(__file__)))
        lib_path_list.append(PYPHASE_PATH)
        # add pyphase install path to library search paths
        for p in lib_path_list:
            if (sys.version_info.major == 3 and sys.version_info.minor >= 8):
                os.add_dll_directory(p)
            else:
                os.environ['PATH'] = p + os.pathsep + os.environ['PATH']
    if sys.platform == "linux" or sys.platform == "linux2":
        # TODO use rpath to find libs
        pass


def check_phase_version(phase_version):
    # check Phase library included version matches expected version
    from phase.pyphase import getVersionString

    m_phase_version = getVersionString()
    if m_phase_version != phase_version:
        error_msg = \
            "Phase library version mismatch. Expected v{} but got v{}.\n" \
            "This may occur if another version of the Phase library \n" \
            "is installed and library files are accessable globally.".format(
                phase_version, m_phase_version)
        raise Exception(error_msg)


# Define phase version
phase_version = "0.0.25"

# Check valid phase import
import_phase()
check_phase_version(phase_version)

# Cleanup variables/functions so they are accessible after import
del import_phase
del check_phase_version
del phase_version
