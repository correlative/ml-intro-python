#!/bin/zsh

python3 -m pip install virtualenv

venvname="venv"

virtualenv "$(pwd)/$venvname"



python3 -m pip install -r requirements.txt

bazel run //:generate_requirements_txt
bazel run //:create_venv

source "$venvname/bin/activate"
# source "$(pwd)/bin/activate'
