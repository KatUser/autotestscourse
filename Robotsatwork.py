from selenium import webdriver
browser = webdriver.Chrome()
browser.execute_script("document.title='Shit executing';alert('Robots at work');")