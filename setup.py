# -*- coding: utf-8 -*-
import os
import sys
import shutil
from shutil import which
from setuptools import setup

setup_file_path = os.path.dirname(os.path.realpath(__file__))
project_root = setup_file_path
package_folder = os.path.join(project_root, "build", "lib", "phase")
python_version_lower = \
    str(sys.version_info.major) + '.' + str(sys.version_info.minor)
python_version_upper = \
    str(sys.version_info.major) + '.' + str(sys.version_info.minor + 1)

with_i3drsgm = False
if "--with_i3drsgm" in sys.argv:
    with_i3drsgm = True
    sys.argv.remove("--with_i3drsgm")


def load_long_description():
    global project_root
    readme_path = os.path.join(project_root, "description.md")
    with open(readme_path, "r") as fh:
        long_description = fh.read()
    return long_description


def load_version():
    global project_root
    with open(os.path.join(project_root, "version.txt"), "r") as fh:
        version = fh.read()
    return version


def find_package_data():
    package_data = {
        "phase":
        [
            '*',
            'pyphase/*',
            'pyphase/calib/*',
            'pyphase/stereocamera/*',
            'pyphase/stereomatcher/*',
            'pyphase/types/*',
        ]
    }
    return package_data


def gen_stubs():
    global project_root
    python_path = os.path.abspath(os.path.join(package_folder, ".."))
    if which("pybind11-stubgen") is None:
        raise Exception("Failed to find pybind11-stubgen")
    stubgen_cmd = 'pybind11-stubgen phase.pyphase -o "' + python_path + \
                  '" --ignore-invalid all --no-setup-py'
    exit_code = os.system(stubgen_cmd)
    if exit_code != 0:
        raise Exception("Failed to generate stubs")
    if os.path.exists(os.path.join(python_path, "phase", "pyphase")):
        shutil.rmtree(os.path.join(python_path, "phase", "pyphase"))
    os.rename(
        os.path.join(python_path, "phase", "pyphase-stubs"),
        os.path.join(python_path, "phase", "pyphase")
    )


try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False
except ImportError:
    bdist_wheel = None


gen_stubs()

setup(
    name="phase",
    version=load_version(),
    author="Ben Knight",
    author_email="bknight@i3drobotics.com",
    description="Python API for I3DR's Phase Library",
    long_description=load_long_description(),
    long_description_content_type="text/markdown",
    url="https://i3drobotics.github.io/phase/python/html/index.html",
    project_urls={
        "Documentation":
            "https://i3drobotics.github.io/phase/python/html/index.html",
        "Issues":
            "https://github.com/i3drobotics/phase/issues",
    },
    license_files=('LICENSE'),
    cmdclass={'bdist_wheel': bdist_wheel},
    zip_safe=False,
    packages=['phase'],
    python_requires='>=3.5',
    install_requires=['numpy'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    keywords='Industrial 3D Robotics I3DR stereo camera',
    package_dir={'phase': package_folder},
    package_data=find_package_data(),
)
