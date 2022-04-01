# pyPhase
***WARNING: This is an early alpha release so may be unstable with breaking changes and have missing documentaiton. Use with caution.***

Phase library is required to be installed to use pyPhase.  
>### Linux
>Download debian package from [v0.0.20 release](https://github.com/>i3drobotics/phase-dev/releases/tag/v0.0.20).  
>Install debian package using apt package manager:
>```
>sudo apt install -f ./phase_vx.x.x-amd64.deb
>```
>This should install to `/opt/i3dr/phase`
>### Windows
>Download Windows installer from the [v0.0.20 release](https://github.com/>i3drobotics/phase-dev/releases/tag/v0.0.20).  
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

Documentation is available [here](https://i3drobotics.github.io/pyphase/)