from selenium import webdriver
from selenium.webdriver.common.by import By  # tyuyf
import time
import math

"""Переход на новую вкладку браузера"""


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/redirect_accept.html")
time.sleep(3)
button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()
browser.switch_to.window(browser.window_handles[1])

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

answer = browser.find_element(By.ID, "answer")
answer.send_keys(y)


button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()
time.sleep(10)
browser.quit()
