from selenium import webdriver
from selenium.webdriver.common.by import By  # tyuyf
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""ждем нужный текст на странице"""


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()


browser.get("http://suninjuly.github.io/explicit_wait2.html")
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "100")
    )
book = browser.find_element(By.ID, "book")
book.click()
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

answer = browser.find_element(By.ID, "answer")
answer.send_keys(y)


button = browser.find_element(By.ID, "solve")
button.click()
time.sleep(10)
browser.quit()
