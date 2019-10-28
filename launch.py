#-*-coding: utf-8 -*-
from selenium import webdriver
import time
import csv
import re
import datetime
nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
ASIN = 'B07WDF1YPL'

chrome_option = webdriver.ChromeOptions()
# chrome_option.add_argument('--headless')
chrome_option.add_argument('--disable-gpu')
chrome_option.add_argument('--ignore-certificate-errors')
chrome_option.add_argument('--disable-images')

driver = webdriver.Chrome(chrome_options=chrome_option)
driver.get('https://members.helium10.com/cerebro')
driver.maximize_window()
time.sleep(5)
#login
driver.find_element_by_id("loginform-email").send_keys("hi920@139.com")
driver.find_element_by_id("loginform-password").send_keys("GDjhd698VV+")
driver.find_element_by_css_selector('#login-form > button').click()
time.sleep(5)

#input
driver.find_element_by_xpath('//*[@id="wrapper"]/div[3]/div/div/div[2]/div/div/div[1]/span/span[1]/span/ul/li/input').send_keys(ASIN)
driver.find_element_by_xpath('//*[@id="search-form"]/a[1]').click()
time.sleep(5)

#alert
flags = False
try:
    driver.find_element_by_xpath('/html/body/div[17]/div[7]/button')
    flags = True
except:
    flags = False
if(flags):
    driver.find_element_by_xpath('/html/body/div[17]/div[7]/button').click()
    time.sleep(10)
else:
    time.sleep(15)

#get total number key word
totalKeyWord = driver.find_element_by_xpath('//*[@id="cerebroPjax"]/div[2]/div/div/div/div/div/div[1]/div[1]/div/span').text

totalKeyWord = int(re.sub('\D', '', totalKeyWord))


# tbody pages
tbody = driver.find_elements_by_xpath('//*[@id="w3"]/table/tbody/tr')
tdnumber = driver.find_elements_by_xpath('//*[@id="w3"]/table/tbody/tr[1]/td')
totalPages = int(totalKeyWord/len(tbody))

lineText = {}

# totalPages = 0
for num in range(1, totalPages+2):
    print('total page is :', str(totalPages+1), 'now pages is :', num)
    tbody = driver.find_elements_by_xpath('//*[@id="w3"]/table/tbody/tr')
    for i in range(1, len(tbody) +1):
        caseResult = []
        for j in range(1, len(tdnumber) +1):
            xPATH = '//*[@id="w3"]/table/tbody/tr' + '[' + str(i) + ']' + '/td' + '[' + str(j) + ']'
            xpathText = str(driver.find_element_by_xpath(xPATH).text)
            if (j == 7):
                xpathText = re.sub('\D', '', xpathText)
            if (j == 9):
                A = 1 if ('A' in xpathText) else 0
                S = 1 if ('S' in xpathText) else 0
                O = 1 if ('O' in xpathText) else 0
                caseResult.append(A)
                caseResult.append(S)
                caseResult.append(O)
            if (j == 3):
                if ("Amazon's Choice" in xpathText):
                    xpathText = xpathText.replace("\nAmazon's Choice", '')
                    caseResult.append("Amazon's Choice")
                else:
                    caseResult.append('')
            caseResult.append(xpathText)
        caseResult.pop(1)
        lineText[caseResult[0]] = caseResult
    if num <= totalPages:
        # next pages
        time.sleep(3)
        driver.find_element_by_partial_link_text('»').click()
        time.sleep(5)

outputFile = ASIN + '-total-' + str(len(lineText)) + '-' + nowTime + '.csv'
with open(outputFile, 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for values in lineText.values():
        writer.writerow(values)

print(len(lineText));
print(outputFile);
driver.quit()