#!/bin/bash

pwd
cd sel/
#virtualenv login
source bin/activate
# mv selTest login/
# pip3 -q install selenium
cd selTest/tests
python3 alarm_test.py
cd ..
cd reports
pwd
echo 'testsim@123' | sudo -S cp Alarm_test.html /var/www/testReports/
echo 'testsim@123' | sudo -S sudo service nginx restart
rm -r selTest
rm testScript.sh

