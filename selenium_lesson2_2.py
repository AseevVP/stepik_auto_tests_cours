from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")

x_element = browser.find_element(By.ID, "treasure")
x = x_element.get_attribute("valuex")
y = calc(x)
answer = browser.find_element(By.ID, "answer")
answer.send_keys(y)

robots_radio = browser.find_element(By.ID, "robotCheckbox")
robots_radio.click()


radiobutton = browser.find_element(By.ID, "robotsRule")
radiobutton.click()
time.sleep(5)
button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
button.click()
time.sleep(10)
browser.quit()
