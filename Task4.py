import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    option1 = browser.find_element(By.TAG_NAME, "button")
    option1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    option2 = browser.find_element(By.ID, "input_value")
    x = option2.text
    y = calc(x)

    input2 = browser.find_element(By.ID, "answer")
    input2.send_keys(y)

    option3 = browser.find_element(By.TAG_NAME, "button")
    option3.click()

finally:
    time.sleep(10)
    browser.close()

