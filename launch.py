from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
SE = webdriver.Chrome()
# URL = 'https://members.helium10.com'
URL = 'https://members.helium10.com/cerebro'
SE.get(URL)
# time.sleep(5)
# browser.find_element_by_id("twotabsearchtextbox").send_keys("basketball knee pad")
# browser.find_element_by_class_name("nav-input").click()

#login first
SE.find_element_by_id('loginform-email').send_keys('hi920@139.com')
SE.find_element_by_id('loginform-password').send_keys('GDjhd698VV+')
SE.find_element_by_css_selector('#login-form > button').click()

#cerebro
time.sleep(5)
# SE.find_element_by_css_selector('body > nav > ul > li:nth-child(4) > a > i').click()
# time.sleep(5)
# SE.find_element_by_css_selector('#wrapper > div.content > div > div > div.panel-body > div > div > div.multi-asin-search-container > span > span.selection > span > ul > li').send_keys('B07VD4NTX7')
SE.find_element_by_xpath('//*[@id="wrapper"]/div[3]/div/div/div[2]/div/div/div[1]/span/span[1]/span/ul/li/input')
.send_keys('B07VD4NTX7')
SE.find_element_by_xpath('//*[@id="search-form"]/a[1]').click()

#alert
# SE.find_element_by_class_name("cancel").click()
time.sleep(5)
SE.find_element_by_xpath('/html/body/div[17]/div[7]').click()

#select number
# NU = Select(SE.find_element_by_class_name('per-page'))
# NU.select_by_index(3)

#find the table 
all_data = SE.find_element_by_xpath('//*[@id="w3"]/table')
