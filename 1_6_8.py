from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("//html/body/div/form/div[1]/input")
    print(input1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//html/body/div/form/div[2]/input")
    print(input2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("/html/body/div/form/div[3]/input")
    print(input3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_xpath("//html/body/div/form/div[4]/input")
    print(input4)
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath("/html/body/div[1]/form/div[6]/button[3]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
