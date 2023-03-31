"""example 1"""
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
# class TestMainPage1():
#
#     @pytest.mark.smoke
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")
#
#     @pytest.mark.regression
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


"""example 2"""

# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
# class TestMainPage1():
#
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
#
#     @pytest.mark.xfail(reason="fixing this bug right now")
#     def test_guest_should_see_search_button_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "input.btn.btn-default")


import pytest


class TestMainPage():
    # номер 1
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_1(self, browser):
        print(1)
        assert True

    # номер 2
    @pytest.mark.regression
    def test_2(self, browser):
        print(2)
        assert True


class TestBasket():
    # номер 3
    @pytest.mark.skip(reason="not implemented yet")
    @pytest.mark.smoke
    def test_3(self, browser):
        print(3)
        assert True

    # номер 4
    @pytest.mark.smoke
    def test_4(self, browser):
        print(4)
        assert True


@pytest.mark.skip
class TestBookPage():
    # номер 5
    @pytest.mark.smoke
    def test_5(self, browser):
        print(5)
        assert True

    # номер 6
    @pytest.mark.regression
    def test_6(self, browser):
        print(6)
        assert True


# номер 7
@pytest.mark.beta_users
@pytest.mark.smoke
def test_7(browser):
    print(7)
    assert True
