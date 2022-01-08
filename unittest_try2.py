import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()

class TestClass(unittest.TestCase):
    def test1(self):
        browser.get('http://suninjuly.github.io/registration1.html')
        input1 = browser.find_element(By.CLASS_NAME, "form-control.first")
        input1.send_keys("Qatya")

        input2 = browser.find_element(By.CLASS_NAME, "form-control.second")
        input2.send_keys("Sh")

        input3 = browser.find_element(By.CLASS_NAME, "form-control.third")
        input3.send_keys("Qatya@sh.com")

        input4 = browser.find_element(By.XPATH, "//input[@placeholder='Input your phone:']")
        input4.send_keys("79135558899")

        input5 = browser.find_element(By.XPATH, "//input[@placeholder='Input your address:']")
        input5.send_keys("79135558899")

        button = browser.find_element(By.CLASS_NAME, "btn")
        button.click()
        expected_result = 'http://suninjuly.github.io/registration_result.html?'
        actual_result = 'http://suninjuly.github.io/registration_result.html?'
        self.assertEqual(expected_result, actual_result)


    def test2(self):
        browser.get('http://suninjuly.github.io/registration2.html')
        input1 = browser.find_element(By.CLASS_NAME, "form-control.first")
        input1.send_keys("Qatya")

        input2 = browser.find_element(By.CLASS_NAME, "form-control.second")
        input2.send_keys("Sh")

        input3 = browser.find_element(By.CLASS_NAME, "form-control.third")
        input3.send_keys("Qatya@sh.com")

        input4 = browser.find_element(By.XPATH, "//input[@placeholder='Input your phone:']")
        input4.send_keys("79135558899")

        input5 = browser.find_element(By.XPATH, "//input[@placeholder='Input your address:']")
        input5.send_keys("79135558899")

        button = browser.find_element(By.CLASS_NAME, "btn")
        button.click()
        expected_result = 'http://suninjuly.github.io/registration_result.html?'
        actual_result = 'http://suninjuly.github.io/registration_result.html?'
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()