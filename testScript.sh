#!/bin/bash

cd sel/
# virtualenv login
source bin/activate
# mv selTest login/
# pip3 -q install selenium
python3 selTest/tests/alarm_test.py
# rm -r selTest
rm testScript.sh

