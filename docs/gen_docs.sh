#!/bin/bash

# exit on command failure
set -e

SCRIPT_PATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

cd "$SCRIPT_PATH/../"

VERSION=$(cat version.txt)
VERSION=${VERSION//$'\n'/} # Remove newlines.
VERSION=${VERSION//$'\r'/} # Remove carriage returns.

# remove previous docs
rm -rf deployment/docs
mkdir -p deployment/docs

# generate developer docs using doxygen
( cat "$SCRIPT_PATH/../docs/doxygen/Doxyfile_developer" ; echo "PROJECT_NUMBER=$VERSION" ) | "doxygen" -

# build python docs with sphinx
# (requires build files in 'install' to generate)
INIT_PYTHONPATH="$PYTHONPATH"
export PYTHONPATH="$SCRIPT_PATH/../build/lib"
cd "$SCRIPT_PATH/../docs/sphinx/"
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    ./make.bat html
else
    make html
fi
export PYTHONPATH="$INIT_PYTHONPATH"
cd "$SCRIPT_PATH/../deployment/docs/external/html/"
mv * ../
cd "$SCRIPT_PATH/../"
rm -rf "$SCRIPT_PATH/../deployment/docs/external/doctrees"
rm -rf "$SCRIPT_PATH/../deployment/docs/external/html"

# create nojekyll file needed for static github pages release
touch deployment/docs/external/.nojekyll