from selenium import webdriver
from selenium.webdriver.common.by import By
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
    
x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
x = x_element.text
y = calc(x)

browser.find_element_by_xpath('//*[@id="answer"]').send_keys(y)

browser.find_element_by_xpath('//*[@id="robotCheckbox"]').click()
browser.find_element_by_xpath('//*[@id="robotsRule"]').click()
browser.find_element_by_xpath('/html/body/div/form/button').click()