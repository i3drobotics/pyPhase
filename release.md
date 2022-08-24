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
- Added documentation for all classes [#31](https://github.com/i3drobotics/pyphase/pull/31)
- Improved gitpod development speed [#32](https://github.com/i3drobotics/pyphase/pull/32)
- Improved unit tests [#41](https://github.com/i3drobotics/pyphase/pull/41)
- Upgrade to Phase v0.1.2-10 [#42](https://github.com/i3drobotics/pyphase/pull/42)
    - Improved placement of types in modules
- Added performance tests [#43](https://github.com/i3drobotics/pyphase/pull/43)
- Added Titania demo script [#47](https://github.com/i3drobotics/pyphase/pull/47)

### Breaking changes
- Phase v0.1.2-10 upgrade has breaking changes [#42](https://github.com/i3drobotics/pyphase/pull/42)
    - Removed StereoProcess and StereoVision
    - Removed RGBDVideoStreamer and RGBDVideoWriter
    - Moved CameraDeviceInfo from 'types' to 'stereocamera' folder
    - Moved all contents in 'types/common.py' to other classes and removed 'types/common.py'
    - Moved StereoMatcherType and StereoMatcherComputeResult to AbstractStereoMatcher
    - Moved CameraReadResult to AbstractStereoCamera
    - Created 'types/stereo.py'
    - Moved StereoImagePair to 'types/stereo.py'
    - Renamed phaseversion.py to version.py
