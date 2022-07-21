import time
import unittest
from selenium import webdriver


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element_by_css_selector("input[placeholder='Input your first name']")
        first_name.send_keys('1')

        last_name = browser.find_element_by_css_selector("input[placeholder='Input your last name']")
        last_name.send_keys('1')

        email = browser.find_element_by_css_selector("input[placeholder='Input your email']")
        email.send_keys('1')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        # assert welcome_text == "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element_by_css_selector("input[placeholder='Input your first name']")
        first_name.send_keys('1')

        last_name = browser.find_element_by_css_selector("input[placeholder='Input your last name']")
        last_name.send_keys('1')

        email = browser.find_element_by_css_selector("input[placeholder='Input your email']")
        email.send_keys('1')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()