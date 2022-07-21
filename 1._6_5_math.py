import math
from selenium import webdriver
driver = webdriver.Chrome()

driver.get (str(math.ceil(math.pow(math.pi, math.e)*10000)))


