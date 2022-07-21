import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file.txt"
file_path = os.path.join('C:\\Users\m.belousov\Desktop\Stepik_Python+Selenium+WebDriver', 'file.txt')

browser.find_element_by_xpath('/html/body/div/form/div/input[1]').send_keys('Ivan')
browser.find_element_by_xpath('/html/body/div/form/div/input[2]').send_keys('Ivanov')
browser.find_element_by_xpath('/html/body/div/form/div/input[3]').send_keys('test@test.com')
browser.find_element_by_xpath('//*[@id="file"]').send_keys(file_path)
time.sleep (1)
browser.find_element_by_xpath('/html/body/div/form/button').click()