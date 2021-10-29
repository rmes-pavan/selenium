#!/bin/bash

virtualenv login
source login/bin/activate
mv login.py login/
mv login.sh login/
python3 login/login.py
cd
rm -r login
