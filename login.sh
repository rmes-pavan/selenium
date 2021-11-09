#!/bin/bash

virtualenv login
source login/bin/activate
mv login.py login/
cd login/
pip3 install selenium
python3 login.py
cd
rm -r login
rm login.sh

