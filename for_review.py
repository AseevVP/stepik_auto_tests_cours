from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR,
                         'body > div > form > div.first_block > div.form-group.first_class > input').send_keys('Name')
    browser.find_element(By.CSS_SELECTOR,
                         'body > div > form > div.first_block > div.form-group.second_class > input').send_keys(
        'Surname')
    browser.find_element(By.CSS_SELECTOR,
                         'body > div > form > div.first_block > div.form-group.third_class > input').send_keys(
        'asd@asd.as')

    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
