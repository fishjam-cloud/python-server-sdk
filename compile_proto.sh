#!/bin/bash

# Terminate on errors
set -e

printf "Synchronising submodules... "
git submodule sync --recursive >>/dev/null
git submodule update --recursive --remote --init >>/dev/null
printf "DONE\n\n"

FILES=("protos/fishjam/agent_notifications.proto" "protos/fishjam/server_notifications.proto")

printf "Compiling file: %s\n" "${FILES[@]}"
uv run protoc -I protos --python_betterproto_out="./fishjam/events/_protos" "${FILES[@]}"
printf "\tDONE\n"
