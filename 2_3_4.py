from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    browser.find_element(by=By.XPATH, value='/html/body/form/div/div/button').click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(by=By.ID, value='input_value')
    x = int(x_element.text)
    x = calc(x)

    browser.find_element(by=By.XPATH, value='//*[@id="answer"]').send_keys(x)
    browser.find_element(by=By.XPATH, value='/html/body/form/div/div/button').click()

finally:
    time.sleep(10)
    browser.quit