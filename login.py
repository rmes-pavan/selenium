#import psycopg2
#import pandas as pd
#import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import unittest
import time


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        cls.driver = webdriver.Chrome(options=chrome_options)
#       cls.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_login_test(self):
        self.driver.get(f'http://192.168.60.79/admin')
        self.driver.find_element(By.XPATH,"/html/body/app-root/div/app-login/div[1]/form/div[1]/input").send_keys("demo@rmes.com")
        self.driver.find_element(By.XPATH,"/html/body/app-root/div/app-login/div[1]/form/div[2]/input").send_keys("test")
        self.driver.find_element(By.XPATH,"/html/body/app-root/div/app-login/div[1]/form/div[4]/button").click()
        self.driver.find_element(By.XPATH, "/html/body/app-root/div/app-admin-layout/app-header-nav/header/div[2]/div[2]/button").click()
        self.driver.find_element(By.XPATH, "/html/body/app-root/div/app-admin-layout/app-header-nav/header/div[2]/div[2]/div/div/button[2]").click()
#        time.sleep(5)

#    def test_2ndlogin(self):
#        self.driver.get(f'http://192.168.60.79/resource/transformer/6/summary')
#        self.driver.find_element(By.XPATH,"/html/body/app-root/div/app-login/div[1]/form/div[1]/input").send_keys("demo@rmes.com")
#        self.driver.find_element(By.XPATH,"/html/body/app-root/div/app-login/div[1]/form/div[2]/input").send_keys("test")
#        self.driver.find_element(By.XPATH,"/html/body/app-root/div/app-login/div[1]/form/div[4]/button").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if __name__ == "__main__":
    unittest.main()
# login = LoginTest()
# login.setUpClass()
# login.login_test()
# login.tearDownClass()


# try:
#     tag20 = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.CLASS_NAME,'user-icon')))
# except:
#     pass
# driver.find_elements_by_class_name('user-icon')[0].click()
# driver.find_elements_by_class_name('signOutBtn')[0].click()
# try:
#     tag20 = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div/snack-bar-container/div/div/simple-snack-bar/span')))
# except:
#     pass




# asset_id =[]
# count = 0
# for row in result:
#     count+=1
#     asset_id.append(row[0])
#     driver.execute_script(f"window.open('about:blank','{row[0]}');")
#     driver.switch_to.window(f"{row[0]}")
#     driver.get(f'http://192.168.60.200/resource/transformer/{row[0]}/summary')
#     username = driver.find_element_by_xpath("/html/body/app-root/div/app-login/div[1]/form/div[1]/input")
#     username.send_keys("pguntupalli@ruggedmonitoring.com")
#     password = driver.find_element_by_xpath("/html/body/app-root/div/app-login/div[1]/form/div[2]/input")
#     password.send_keys("test")
#     username.send_keys(Keys.RETURN)
#     if count == 10:
#         break



