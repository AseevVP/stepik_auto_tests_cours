# """unittest"""
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import unittest
#
#
# class TestAbs(unittest.TestCase):
#     def test_registration1(self):
#         global browser
#         try:
#             link = "http://suninjuly.github.io/registration1.html"
#             browser = webdriver.Chrome()
#             browser.get(link)
#
#             browser.find_element(By.CSS_SELECTOR,
#                                  'body > div > form > div.first_block > div.form-group.first_class > input').send_keys(
#                 'Name')
#             browser.find_element(By.CSS_SELECTOR,
#                                  'body > div > form > div.first_block > div.form-group.second_class > input').send_keys(
#                 'Surname')
#             browser.find_element(By.CSS_SELECTOR,
#                                  'body > div > form > div.first_block > div.form-group.third_class > input').send_keys(
#                 'asd@asd.as')
#
#             button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
#             button.click()
#
#             time.sleep(1)
#
#             welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#             welcome_text = welcome_text_elt.text
#             self.assertEqual(welcome_text, "Congratulations! You have successfully registered!"), "There is no any congrats"
#
#         finally:
#             # ожидание чтобы визуально оценить результаты прохождения скрипта
#             time.sleep(5)
#             # закрываем браузер после всех манипуляций
#             browser.quit()
#
#     def test_registration2(self):
#         try:
#             link = "http://suninjuly.github.io/registration2.html"
#             browser = webdriver.Chrome()
#             browser.get(link)
#
#             browser.find_element(By.CSS_SELECTOR,
#                                  'body > div > form > div.first_block > div.form-group.first_class > input').send_keys(
#                 'Name')
#             browser.find_element(By.CSS_SELECTOR,
#                                  'body > div > form > div.first_block > div.form-group.second_class > input').send_keys(
#                 'Surname')
#             browser.find_element(By.CSS_SELECTOR,
#                                  'body > div > form > div.first_block > div.form-group.third_class > input').send_keys(
#                 'asd@asd.as')
#
#             button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
#             button.click()
#
#             time.sleep(1)
#
#             welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#             welcome_text = welcome_text_elt.text
#             self.assertEqual(welcome_text, "Congratulations! You have successfully registered!"), "There is no any congrats"
#
#         finally:
#             # ожидание чтобы визуально оценить результаты прохождения скрипта
#             time.sleep(5)
#             # закрываем браузер после всех манипуляций
#             browser.quit()
#
#
# if __name__ == "__main__":
#     unittest.main()


"""unittest"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_registration1():
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR,
                         'body > div > form > div.first_block > div.form-group.first_class > input').send_keys(
        'Name')
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
    assert welcome_text == "Congratulations! You have successfully registered!"

    time.sleep(5)
    browser.quit()


def test_registration2():
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR,
                         'body > div > form > div.first_block > div.form-group.first_class > input').send_keys(
        'Name')
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
    assert welcome_text == "Congratulations! You have successfully registered!"

    time.sleep(5)
    browser.quit()
