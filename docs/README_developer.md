# pyPhase (Developer)
Documenation for developers of pyPhase. pyPhase is a python wrapper over I3DR's Phase C++ library.

***WARNING: This documentation is for members of Industrial 3D Robotics only.***  
***This contains private code that should not be shared publicly.***

## Install
Phase library is required to be installed to use pyPhase.  
>### Linux
>Download debian package from [v0.0.27 release](https://github.com/i3drobotics/phase/releases/tag/v0.0.27).  
>Install debian package using apt package manager:
>```
>sudo apt install -f ./phase_vx.x.x-amd64.deb
>```
>This should install to `/opt/i3dr/phase`
>### Windows
>Download Windows installer from the [v0.0.27 release](https://github.com/i3drobotics/phase/releases/tag/v0.0.27).  
>Install using the installer GUI, this should install to `C:\Program Files\i3DR\Phase`
>

Then install pyPhase using pip:
```
pip install phase
```

## Dependencies
Phase library is required to be installed for use in the build process.  
### Linux
Download debian package from [v0.0.27 release](https://github.com/i3drobotics/phase/releases/tag/v0.0.27).  
Install debian package using apt package manager:
```
sudo apt install -f ./phase_vx.x.x-amd64.deb
```
This should install to `/opt/i3dr/phase`
### Windows
Download Windows installer from the [v0.0.27 release](https://github.com/i3drobotics/phase/releases/tag/v0.0.27).  
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
