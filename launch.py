from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.amazon.com')
# time.sleep(5)
browser.find_element_by_id("twotabsearchtextbox").send_keys("basketball knee pad")
browser.find_element_by_class_name("nav-input").click()