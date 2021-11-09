#!/bin/bash

virtualenv login
source login/bin/activate
mv selTest login/
cd login/
pip3 -q install selenium
 python3 selTest/tests/login.py
cd
rm -r login
rm login.sh

