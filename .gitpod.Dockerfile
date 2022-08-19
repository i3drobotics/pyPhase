FROM gitpod/workspace-full

RUN mkdir -p /home/gitpod/phase_install && \
    curl --output phase-v0.1.2-8-ubuntu-20.04-x86_64.tar.gz -L https://github.com/i3drobotics/phase/releases/download/v0.1.2-8/phase-v0.1.2-8-ubuntu-20.04-x86_64.tar.gz && \
    tar -xf phase-v0.1.2-8-ubuntu-20.04-x86_64.tar.gz -C /home/gitpod/phase_install && \
    rm -rf phase-v0.1.2-8-ubuntu-20.04-x86_64.tar.gz && \
    sudo apt update && \
    sudo apt install -y libavcodec-dev libavformat-dev libswscale-dev && \
    sudo apt install -y libgl-dev liblapack-dev libblas-dev libgtk2.0-dev && \
    sudo apt install -y libgstreamer1.0-0 libgstreamer-plugins-base1.0-0 && \
    sudo apt install -y zlib1g libstdc++6 && \
    sudo apt install -y libc6 libgcc1 && \
    sudo apt-get install -y patchelf doxygen
