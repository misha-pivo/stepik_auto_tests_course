from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

try:
    browser.find_element(by=By.XPATH, value='/html/body/form/div/div/button').click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(by=By.XPATH, value='//*[@id="input_value"]')
    x = int(x_element.text)
    x = calc(x)
    browser.find_element(by=By.XPATH, value='//*[@id="answer"]').send_keys(x)
    browser.find_element(by=By.XPATH, value='/html/body/form/div/div/button').click()
    time.sleep(3)

    alert = browser.switch_to.alert
    alert.accept()

finally:
    time.sleep(1)
    browser.quit