# pyPhase
***WARNING: This is an early alpha release so may be unstable with breaking changes and have missing documentaiton. Use with caution.***

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

Documentation is available [here](https://i3drobotics.github.io/pyphase/)

## Changelog
### Improvements
 - Changed the suggested way to import pyPhase [#63](https://github.com/i3drobotics/pyphase/pull/63)
 - Added ability to list available cameras using `phase.stereocamera.availableDevices` [#67](https://github.com/i3drobotics/pyphase/pull/67)
 - Updated to phase version v0.2.1-3 [#70](https://github.com/i3drobotics/pyphase/pull/70)

### Bug fixes
 - Fix docstrings missing parameter names [#66](https://github.com/i3drobotics/pyphase/pull/66)

### Known issues
 - Cannot to add docstring parameters for callback functions [pybind11 #4173](https://github.com/pybind/pybind11/issues/4173)
