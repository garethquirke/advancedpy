from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\chromedriver_win32\chromedriver.exe')

driver.get('http://www.github.com/garethquirke/')
driver.close()

# test inputs