from selenium import webdriver
from selenium.webdriver.common.by import By
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
    
x_element = browser.find_element_by_id("treasure")
x = x_element.get_attribute('valuex')
y = calc(x)

browser.find_element_by_xpath('//*[@id="answer"]').send_keys(y)
browser.find_element_by_xpath('//*[@id="robotCheckbox"]').click()
browser.find_element_by_xpath('//*[@id="robotsRule"]').click()
browser.find_element_by_xpath('/html/body/div/form/div/div/button').click()