from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
   return str(math.log(abs(12*math.sin(x))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

x_elemet = browser.find_element_by_id('input_value')
x = int(x_elemet.text)
x = calc(x)
browser.execute_script("window.scrollBy(0, 100);")
browser.find_element_by_xpath('//*[@id="answer"]').send_keys(x)
browser.find_element_by_xpath('//*[@id="robotCheckbox"]').click()
browser.find_element_by_xpath('//*[@id="robotsRule"]').click()
browser.find_element_by_xpath('/html/body/div/form/button').click()
