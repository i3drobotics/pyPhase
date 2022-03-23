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


def find_phase():
    if sys.platform == "win32":
        lib_path_list = []
        PYPHASE_PATH = os.path.abspath(
            os.path.dirname(os.path.realpath(__file__)))
        PHASE_DIR_REL_TO_BUILD = os.path.abspath(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "../../../../../install/bin"))
        PHASE_DIR_REL_TO_INSTALL = os.path.abspath(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "../../../install/bin"))
        if os.path.exists(PHASE_DIR_REL_TO_BUILD):
            lib_path_list.append(PHASE_DIR_REL_TO_BUILD)
        elif os.path.exists(PHASE_DIR_REL_TO_INSTALL):
            lib_path_list.append(PHASE_DIR_REL_TO_INSTALL)
        elif "PHASE_DIR" in os.environ:
            # get path from PHASE_DIR environment variable
            PHASE_DIR = os.environ["PHASE_DIR"]
            PHASE_BIN = os.path.join(PHASE_DIR, "bin")
            if os.path.exists(PHASE_BIN):
                lib_path_list.append(PHASE_BIN)
            else:
                raise Exception(
                    "phase import failed: PHASE_DIR path does not exist")
        else:
            raise Exception("phase import failed: PHASE_DIR not set")
        lib_path_list.append(PYPHASE_PATH)
        for p in lib_path_list:
            if (sys.version_info.major == 3 and sys.version_info.minor >= 8):
                os.add_dll_directory(p)
            else:
                os.environ['PATH'] = p + os.pathsep + os.environ['PATH']
                # sys.path.insert(1, p)
    if sys.platform == "linux" or sys.platform == "linux2":
        pass


find_phase()
del find_phase
