from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

"""подтверждение действия в всплывающем окне"""
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

answer = browser.find_element(By.ID, "answer")
answer.send_keys(y)


button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()
time.sleep(10)
browser.quit()
