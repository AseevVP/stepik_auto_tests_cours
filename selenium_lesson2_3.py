from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""выбор варианта из выпадающего списка"""

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/selects1.html")


x_element = browser.find_element(By.ID, "num1")
x = int(x_element.text)

y_element = browser.find_element(By.ID, "num2")
y = int(y_element.text)


def calc(x, y):
    return str(x + y)


browser.find_element(By.ID, "dropdown").click()
answer = calc(x, y)

browser.find_element(By.CSS_SELECTOR, f'[value="{answer}"]').click()

button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
button.click()
time.sleep(13)
browser.quit()
