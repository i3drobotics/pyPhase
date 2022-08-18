FROM gitpod/workspace-full

RUN curl --output phase.deb -L https://github.com/i3drobotics/phase/releases/download/v0.0.27-1/phase-v0.0.27-1-ubuntu-20.04-x86_64.deb && \
    sudo apt update && \
    sudo apt install -y ./phase.deb && \
    sudo rm -rf ./phase.deb && \
    sudo apt-get install -y patchelf doxygen
