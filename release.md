# pyPhase
***WARNING: This is an early alpha release so may be unstable with breaking changes and have missing documentaiton. Use with caution.***

## Features
 - Upgrade to Phase v0.0.26
 - Added test for Pylon virtual cameras image size
 - Added simpified demo drivers (demo_read, demo_match, demo_read_thread, demo_match_thread)
 - Improved thread safety for camera read threads
 - Added read callback example to documentation

## Bug fixes
 - Fixed unstable read rates
 - Fixed camera image size is incorrect for Pylon virtual cameras
 - Fixed thread lock when reading frame rate

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
