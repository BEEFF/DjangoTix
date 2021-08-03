#!/bin/bash

source ./dev/setup-python.sh
pip3 install django
django-admin startproject rosa
cd rosa
ls

echo ""