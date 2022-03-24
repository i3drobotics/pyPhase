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

phase_version = "0.0.20"
phase_download_url = \
    "https://github.com/i3drobotics/phase/releases/tag/v{}".format(
        phase_version)


def find_phase():
    global phase_version, phase_download_url
    if sys.platform == "win32":
        lib_path_list = []
        # pyPhase module path
        PYPHASE_PATH = os.path.abspath(
            os.path.dirname(os.path.realpath(__file__)))
        # standard install location of Phase library
        # %PROGRAMFILES%\i3DR\Phase\bin
        PHASE_INSTALL_PATH = os.path.abspath(os.path.join(
            os.environ["ProgramFiles"], "i3DR", "Phase", "bin"))
        if os.path.exists(PHASE_INSTALL_PATH):
            lib_path_list.append(PHASE_INSTALL_PATH)
        elif "PHASE_DIR" in os.environ:
            # get path from PHASE_DIR environment variable
            PHASE_DIR = os.environ["PHASE_DIR"]
            PHASE_BIN = os.path.join(PHASE_DIR, "bin")
            if os.path.exists(PHASE_BIN):
                lib_path_list.append(PHASE_BIN)
            else:
                error_msg = \
                    "Cannot load Phase library. " \
                    "PHASE_DIR is set but path " \
                    "does not exist: {}".format(PHASE_DIR)
                raise Exception(error_msg)
        else:
            error_msg = \
                "Cannot load Phase library. " \
                "Phase was not found in standard " \
                "install location ({}) and PHASE_DIR " \
                "environment variable is not set.\n" \
                "Install Phase v{} from {}".format(
                    PHASE_INSTALL_PATH, phase_version, phase_download_url)
            raise Exception(error_msg)
        lib_path_list.append(PYPHASE_PATH)
        # add paths to library search paths
        for p in lib_path_list:
            if (sys.version_info.major == 3 and sys.version_info.minor >= 8):
                os.add_dll_directory(p)
            else:
                os.environ['PATH'] = p + os.pathsep + os.environ['PATH']
    if sys.platform == "linux" or sys.platform == "linux2":
        # phase shared libraries are installed to /opt/i3dr/phase/lib
        # libraries are added to search path in Phase install process
        PHASE_INSTALL_PATH = os.path.join("/opt", "i3dr", "phase")
        if not os.path.exists(PHASE_INSTALL_PATH):
            error_msg = \
                "Cannot load Phase library. " \
                "Phase was not found in standard " \
                "install location ({}).\n" \
                "Install Phase v{} from {}".format(
                    PHASE_INSTALL_PATH, phase_version, phase_download_url)
            raise Exception(error_msg)


find_phase()
del find_phase

# check Phase installed version matches expected version
from phase.pyphase import getVersionString
m_phase_version = getVersionString()
if getVersionString() != phase_version:
    error_msg = \
        "Phase version mismatch. Expected {} but got {}" \
        "Install Phase v{} from {}".format(
            phase_version, getVersionString(),
            phase_version, phase_download_url)
    raise Exception(error_msg)
del getVersionString
del phase_download_url
del phase_version
