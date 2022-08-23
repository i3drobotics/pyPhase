# pyPhase
pyPhase is a python wrapper package over I3DR's Phase C++ library.

[![Pyversions](https://img.shields.io/pypi/pyversions/phase.svg?style=flat-square)](https://pypi.python.org/pypi/phase)

[![Release](https://github.com/i3drobotics/pyphase/actions/workflows/release.yml/badge.svg)](https://github.com/i3drobotics/pyphase/actions/workflows/release.yml)
[![Build](https://github.com/i3drobotics/pyphase/actions/workflows/build.yml/badge.svg)](https://github.com/i3drobotics/pyphase/actions/workflows/build.yml)

## Install
### Windows
Install pyPhase from pypi using pip:
```
pip install phase
```
### Linux
Install dependencies
```
sudo apt install -y libavcodec-dev libavformat-dev libswscale-dev
sudo apt install -y libgl-dev liblapack-dev libblas-dev libgtk2.0-dev
sudo apt install -y libgstreamer1.0-0 libgstreamer-plugins-base1.0-0
sudo apt install -y zlib1g libstdc++6
sudo apt install -y libc6 libgcc1
```
Package is not yet available on pypi for Linux.  
Please download the wheel for your version of python from the release and install using:
```
pip install ./phase-X.X.X-cpXXX-cpXXX-linux_x86_64.whl
```

## Dependencies
Phase library is required to be installed for use in the build process.  
### Linux
Download debian package from [v0.1.2-10 release](https://github.com/i3drobotics/phase/releases/tag/v0.1.2-10).  
Install debian package using apt package manager:
```
sudo apt install -f ./phase_vx.x.x-amd64.deb
```
This should install to `/opt/i3dr/phase`
### Windows
Download Windows installer from the [v0.1.2-10 release](https://github.com/i3drobotics/phase/releases/tag/v0.1.2-10).  
Install using the installer GUI, this should install to `C:\Program Files\i3DR\Phase`

The following libraries are used to build pyPhase:
- [pybind11](https://github.com/pybind/pybind11)
- [pybind_opencv_numpy](https://github.com/edmBernard/pybind11_opencv_numpy)

CMake dependencies are included automatically in the cmake build process.

## Python requirements
Python requirements for building pyPhase can be install using the following command:
```
pip install -r requirements.txt
```

## Additional dependencies
### Linux
```
sudo apt-get install doxygen patchelf
```
### Windows
Download and install doxygen from [here](https://www.doxygen.nl/download.html)

## Build
Build pyPhase bindings using CMake:
```bash
mkdir build
cd build
# [windows]
cmake -G "Visual Studio 16 2019" -A x64 -DPhase_DIR="C:\Program Files\i3DR\Phase\lib\cmake" ..
cmake --build . --config Release
# [linux]
cmake -DPhase_DIR="/opt/i3dr/phase/lib/cmake" ..
make -j$(nproc)
```
*Note: Make sure to run this from the repository root directory*  

## Test
### Unit tests
Run unit tests using pytest by running the following commands:
```bash
cd build/lib
python3 -m pytest ../../test/unit/
```
*Note: Make sure to run this from the repository root directory*

### Performance tests
Run performance tests using pytest by running the following commands:
```bash
cd build/lib
python3 -m pytest ../../test/perf/
```
*Note: Make sure to run this from the repository root directory*

### Drivers
```bash
export PYTHONPATH=./build/lib
python3 test/drivers/demo_read.py
python3 test/drivers/demo_read_thread.py
python3 test/drivers/demo_match.py
python3 test/drivers/demo_match_thread.py
python3 test/drivers/demo_rgbd.py
```

*Note: Make sure to run this from the repository root directory*

## Docs
Documentation is generated and deployed in GitHub actions, however, to test documentation generation locally, run the following commands:
```bash
./docs/gen_docs.sh
```

## Deploy
Deployment is handelled by GitHub actions, however, to test deployment locally, use the following command:
```bash
export PYTHONPATH=./build/lib
python3 setup.py bdist_wheel --dist-dir="deployment"
```
