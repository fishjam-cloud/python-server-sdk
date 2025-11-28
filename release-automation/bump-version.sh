#!/bin/bash
set -e

# Usage: ./bump-version.sh <version>
VERSION="$1"

if [ -z "$VERSION" ]; then
    echo "Usage: $0 <version>"
    exit 1
fi

BRANCH_NAME="release-$VERSION"
git checkout -b "$BRANCH_NAME"

echo "Installing asdf dependencies..."
# add plugins from .tool-versions
while read -r line; do
    PLUGIN_NAME=$(echo "$line" | awk '{print $1}')
    if ! asdf plugin list | grep -q "^$PLUGIN_NAME$"; then
        echo "Adding asdf plugin: $PLUGIN_NAME"
        asdf plugin add "$PLUGIN_NAME"
    else
        echo "asdf plugin $PLUGIN_NAME already added"
    fi
done < .tool-versions

asdf install

uv version "$VERSION"
uv run ./compile_proto.sh

# Update OpenAPI client
curl -H "Authorization: token $GH_TOKEN" \
    -H "Accept: application/vnd.github.v3.raw" \
    -L "https://raw.githubusercontent.com/fishjam-cloud/fishjam/main/openapi.yaml" \
     -o openapi.yaml

uv run update_client ./openapi.yaml
rm openapi.yaml

echo "✅ Version bump complete for $VERSION"
echo "BRANCH_NAME:$BRANCH_NAME"
