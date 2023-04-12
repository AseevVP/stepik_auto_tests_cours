"""example 2"""
import math
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


def stringg(result):
    new_string = ''
    new_string += result

    return new_string


@pytest.mark.parametrize('lnk', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_login(browser, lnk):
    link = f"https://stepik.org/lesson/{lnk}/step/1"

    browser.get(link)

    """login"""
    WebDriverWait(browser, 30).until(EC.element_to_be_clickable(
        (By.ID, 'ember33')))
    browser.find_element(By.ID, 'ember33').click()
    browser.find_element(By.ID, 'id_login_email').send_keys('aseev.vp86@gmail.com')
    browser.find_element(By.ID, 'id_login_password').send_keys('vladislav1986')
    browser.find_element(By.CSS_SELECTOR, '.sign-form__btn.button_with-loader').click()

    """ждем загрузки страницы"""
    WebDriverWait(browser, 30).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '.ember-text-area.ember-view.textarea.string-quiz__textarea'))
    )
    """очищаем, отправляем ответ"""
    browser.find_element(By.CSS_SELECTOR, '.ember-text-area.ember-view.textarea.string-quiz__textarea').clear()
    browser.find_element(By.CSS_SELECTOR, '.ember-text-area.ember-view.textarea.string-quiz__textarea').send_keys(
        str(math.log(int(time.time() + 1))))
    """submit answer"""
    WebDriverWait(browser, 30).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '.submit-submission')))
    browser.find_element(By.CSS_SELECTOR, '.submit-submission').click()

    """"""
    WebDriverWait(browser, 30).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '.smart-hints__hint'))
    )
    result = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text

    print(stringg(result))
    assert result == 'Correct!'




