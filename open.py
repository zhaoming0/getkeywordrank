#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import csv
import re
import datetime
import sys
if(len(sys.argv) > 1):
    ASIN = sys.argv[1]
else:
    ASIN = 'B07WDF1YPL'
print (ASIN, 'asin')
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
time.sleep(5)
#input
driver.find_element_by_xpath('//*[@id="wrapper"]/div[3]/div/div/div[2]/div/div/div[1]/span/span[1]/span/ul/li/input').send_keys(ASIN)
driver.find_element_by_xpath('//*[@id="search-form"]/a[1]').click()
time.sleep(10)
# result = driver.find_element_by_xpath('/html/body/div[17]/div[7]').is_displayed()
# print (result)   /html/body/div[20]/div[7]/div/button
# /html/body/div[17]/div[7]
# /html/body/div[17]/div[7]
# /html/body/div[17]/div[7]/button
# //*[@id="w3"]/div/table/thead/tr
# //*[@id="w3"]/div/table/thead/tr/th[1]
# //*[@id="w3"]/div/table/thead/tr/th[3]

# flags = False
# try:
#     # driver.find_element_by_xpath('/html/body/div[17]/div[7]/button')
#     driver.find_element_by_class_name('confirm')
#     flags = True
# except:
#     flags = False
# print (flags)
# if(flags):
#     print('sleep 5 second')
#     time.sleep(5)
#     # driver.find_element_by_xpath('/html/body/div[17]/div[7]/button').click()
#     driver.find_element_by_class_name('confirm').click()
#     time.sleep(5)

# thNum = driver.find_element_by_xpath('//*[@id="w3"]/div/table/thead/tr').find_elements_by_tag_name('th')
# headerList = []

for num in range(1, len(thNum)+1):
    xpath = '//*[@id="w3"]/div/table/thead/tr' + '/th[' + str(num) +']'
    xpathText = driver.find_element_by_xpath(xpath).text
    if (num == 2):
        headerList.append('Amazon Choise')
    elif(num == 9):
        headerList.append('Amazon Recommended')
        headerList.append('Sponsored')
        headerList.append('Organic')
        headerList.append(xpathText)
    else:
        headerList.append(xpathText)


time.sleep(7)
Select(driver.find_element_by_xpath('//*[@id="w3"]/select')).select_by_value('150')


# driver.quit()
# print (headerList)