from selenium import webdriver
import math

def calc(z):
    return str(x+y)

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

x_elemet = browser.find_element_by_id('num1')
x = int(x_elemet.text)
y_element = browser.find_element_by_id('num2')
y = int(y_element.text)
z = calc(x+y)

browser.find_element_by_xpath('//*[@id="dropdown"]').send_keys(z)
browser.find_element_by_xpath('/html/body/div/form/button').click()
