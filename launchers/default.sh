#!/bin/bash
set -e

source /opt/ros/humble/setup.bash

if [ -d "/code/install" ]; then
    source /code/install/setup.bash
fi

exec bash
