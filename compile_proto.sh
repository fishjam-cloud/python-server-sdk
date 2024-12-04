#!/bin/bash

# Terminate on errors
set -e

printf "Synchronising submodules... "
git submodule sync --recursive >>/dev/null
git submodule update --recursive --remote --init >>/dev/null
printf "DONE\n\n"

server_file="./protos/fishjam/server_notifications.proto"
printf "Compiling: file $server_file\n"
protoc -I . --python_betterproto_out=./fishjam/events/_protos $server_file
printf "\tDONE\n"
