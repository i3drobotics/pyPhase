# pyPhase
***WARNING: This is an early alpha release so may be unstable with breaking changes and have missing documentaiton. Use with caution.***

## Features
 - Upgrade to Phase v0.0.27 [#28](https://github.com/i3drobotics/pyphase/issues/28)

## Bug fixes
 - Added access to left and right calibration objects in stereo calibration [#25](https://github.com/i3drobotics/pyphase/issues/25)
 - Added test for CameraCalibration [#27](https://github.com/i3drobotics/pyphase/issues/27)

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
