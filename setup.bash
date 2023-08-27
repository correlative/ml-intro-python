#!/bin/zsh

python3 -m pip install virtualenv

venvname="venv"

virtualenv "$venvname"

source "$venvname/bin/activate"

python3 -m pip install -r requirements.txt

