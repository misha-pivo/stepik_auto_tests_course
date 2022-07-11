from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
browser.find_element(by=By.XPATH, value='//*[@id="book"]').click()

x_element = browser.find_element(by=By.XPATH, value='//*[@id="input_value"]')
x = int(x_element.text)
x = calc(x)

browser.find_element(by=By.XPATH, value='//*[@id="answer"]').send_keys(x)
browser.find_element(by=By.XPATH, value='//*[@id="solve"]').click()

time.sleep(5)
alert = browser.switch_to.alert
alert.accept()

browser.quit