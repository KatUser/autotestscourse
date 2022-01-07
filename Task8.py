import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Qatya")

    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Sh")

    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("psyno@psyno.com")

    option1 = browser.find_element(By.NAME, "file")
    button_click = option1.get_attribute("file")

    #option1.click()
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

    option1.send_keys(file_path)

    option2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    option2.click()

finally:
    time.sleep(5)
    browser.close()