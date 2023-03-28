import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""загрузка стороннего файла на странице"""

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)


browser.find_element(By.NAME, "firstname").send_keys('John')
browser.find_element(By.NAME, "lastname").send_keys('Wick')
browser.find_element(By.NAME, "email").send_keys('qwe@qwe.wek')


current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
browser.find_element(By.ID, 'file').send_keys(file_path)


browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
time.sleep(5)


