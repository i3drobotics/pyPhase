# pyPhase
pyPhase is a python wrapper package over I3DR's Phase C++ library.

[![Pyversions](https://img.shields.io/pypi/pyversions/phase.svg?style=flat-square)](https://pypi.python.org/pypi/phase)

[![Release](https://github.com/i3drobotics/pyphase/actions/workflows/release.yml/badge.svg)](https://github.com/i3drobotics/pyphase/actions/workflows/release.yml)
[![Build](https://github.com/i3drobotics/pyphase/actions/workflows/build.yml/badge.svg)](https://github.com/i3drobotics/pyphase/actions/workflows/build.yml)

## Install
Phase library is required to be installed to use pyPhase.  
>### Linux
>Download debian package from [v0.0.24 release](https://github.com/i3drobotics/phase/releases/tag/v0.0.24).  
>Install debian package using apt package manager:
>```
>sudo apt install -f ./phase_vx.x.x-amd64.deb
>```
>This should install to `/opt/i3dr/phase`
>### Windows
>Download Windows installer from the [v0.0.24 release](https://github.com/i3drobotics/phase/releases/tag/v0.0.24).  
>Install using the installer GUI, this should install to `C:\Program Files\i3DR\Phase`
>

Then install pyPhase from pypi using pip:
```
pip install phase
```
This is not yet available on pypi for Linux. Please download the wheel for your version of python from the release and install using:
```
pip install ./phase-X.X.X-cpXXX-cpXXX-linux_x86_64.whl
```

## Dependencies
Phase library is required to be installed for use in the build process.  
### Linux
Download debian package from [v0.0.24 release](https://github.com/i3drobotics/phase/releases/tag/v0.0.24).  
Install debian package using apt package manager:
```
sudo apt install -f ./phase_vx.x.x-amd64.deb
```
This should install to `/opt/i3dr/phase`
### Windows
Download Windows installer from the [v0.0.24 release](https://github.com/i3drobotics/phase/releases/tag/v0.0.24).  
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
Doxygen is used for documentation.  
On Linux install with the following command:
```
sudo apt-get install doxygen
```
On Windows download and install doxygen from [here](https://www.doxygen.nl/download.html)

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
patchelf --set-rpath "\$ORIGIN:\$ORIGIN/i3drsgm" "./lib/phase/libphase.so"
patchelf --set-rpath "\$ORIGIN:\$ORIGIN/i3drsgm" "./lib/phase/pyphase.cpython-X-x86_64-linux-gnu.so"
```
*Note: Make sure to run this from the repository root directory*  
*Note: Change pyphase.cpython-X-x86_64-linux-gnu.so for your python version. e.g. pyphase.cpython-38-x86_64-linux-gnu.so*

## Test
### Unit tests
Test using pytest by running the following commands:
```bash
cd build/lib
python3 -m pytest ../../test/src/
```
*Note: Make sure to run this from the repository root directory*

On linux currently libopencv_flann.so.4.5 and libopencv_features2d.so.4.5 are not found.  
The temporary fix for this is to set LD_LIBRARY_PATH
```bash
cd build/lib
export LD_LIBRARY_PATH=$(pwd)/phase:$LD_LIBRARY_PATH
python3 -m pytest ../../test/src/
```

### Drivers
```bash
# [windows]
cd build/lib
python ../../test/drivers/demo_3d_from_image_files.py
python ../../test/drivers/demo_cam_read.py
python ../../test/drivers/demo_mat_numpy_conversion.py
python ../../test/drivers/demo_rgbd.py
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
