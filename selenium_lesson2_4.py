import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""прокрутка до нужного элемента на странице"""


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
x_element = browser.find_element(By.ID, "input_value")
x = int(x_element.text)
y = calc(x)
answer = browser.find_element(By.ID, "answer")
answer.send_keys(y)


robots_checkbox = browser.find_element(By.ID, "robotCheckbox")
robots_checkbox.click()

button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
radiobutton = browser.find_element(By.ID, "robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
radiobutton.click()
button.click()
time.sleep(7)
