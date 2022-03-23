# pyPhase
pyPhase is a wrapper over the I3DR's Phase C++ library.

## Install
```
pip install phase
```

## Dependencies
Phase library is required to be installed for use in the build process.  
### Linux
Download debian package from latest release.  
Install debian package using apt package manager:
```
sudo apt install -f ./phase_vx.x.x-amd64.deb
```
This should install to `/opt/i3dr/phase`
### Windows
Download Windows installer from the latest release.  
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
Test using pytest by running the following commands:
```bash
cd build/lib
python3 -m pytest ../../test/src/
```
*Note: Make sure to run this from the repository root directory*

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