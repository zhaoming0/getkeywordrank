#-*- coding: utf-8 -*-
from selenium import webdriver
import time
import csv
import re
import datetime

ASIN = 'B000UVZK0Y'
driver = webdriver.Chrome()
driver.get('https://members.helium10.com/cerebro')

# class test1(driver):
#     def isElementExist(self, element):
#         flag = True
#         browser = self.driver
#         try:
#             browser.find_element_by_xpath(element)
#             return flag
#         except:
#             flag = False
#             return flag

driver.find_element_by_id("loginform-email").send_keys("hi920@139.com")
driver.find_element_by_id("loginform-password").send_keys("GDjhd698VV+")
driver.find_element_by_css_selector('#login-form > button').click()
time.sleep(10)
#input
driver.find_element_by_xpath('//*[@id="wrapper"]/div[3]/div/div/div[2]/div/div/div[1]/span/span[1]/span/ul/li/input').send_keys(ASIN)
driver.find_element_by_xpath('//*[@id="search-form"]/a[1]').click()
time.sleep(5)
# result = driver.find_element_by_xpath('/html/body/div[17]/div[7]').is_displayed()
# print (result)   /html/body/div[20]/div[7]/div/button
# /html/body/div[17]/div[7]
# /html/body/div[17]/div[7]
# /html/body/div[17]/div[7]/button

flags = False
try:
    driver.find_element_by_xpath('/html/body/div[17]/div[7]/button')
    flags = True
except:
    flags = False
print (flags)
if(flags):
    print('sleep 5 second')
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[17]/div[7]/button').click()
    