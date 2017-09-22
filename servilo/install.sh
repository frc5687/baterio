#!/usr/bin/env bash

UBUNTU_VERSION="$(lsb_release -r -s)"

if [ "$UBUNTU_VERSION" == "17.04" ]; then
    echo "Running Ubuntu 17.04"
    sudo apt install -y python3.6 python3-pip python3-dev virtualenv
elif [ "$UBUNTU_VERSION" == "14.04" ]; then
    sudo apt install -y virtualenv python3-dev python3-pip
    echo "Running Ubuntu 14.04"
fi

if [ ! -d ".venv" ]; then
    virtualenv -p python3.6 .venv;
fi

. .venv/bin/activate; pip install -r requirements.txt
