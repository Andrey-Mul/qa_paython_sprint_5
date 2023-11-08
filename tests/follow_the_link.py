from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators, HeaderLocators, AuthPageLocators, Personal_Account
from tests.data import AuthData


def test_follow_personal_account(browser, authorization):
    """
    Тест перехода по клику на «Личный кабинет».
    """
    browser.find_element(*MainPageLocators.button_enter_account).click()
    email = AuthData.email_text_auth
    password = AuthData.pass_text_auth
    authorization(email, password)
    browser.find_element(*AuthPageLocators.button_auth_enter).click()
    browser.find_element(*HeaderLocators.link_personal_account).click()
    expected = browser.find_element(*Personal_Account.text_profile).text
    result = "Профиль"
    assert expected == result


def test_follow_in_personal_account_to_designer(browser, authorization):
    """
    Тест по клику на «Конструктор».
    """
    browser.find_element(*MainPageLocators.button_enter_account).click()
    email = AuthData.email_text_auth
    password = AuthData.pass_text_auth
    authorization(email, password)
    browser.find_element(*AuthPageLocators.button_auth_enter).click()
    WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located(MainPageLocators.button_order))
    browser.find_element(*HeaderLocators.link_personal_account).click()
    WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located(Personal_Account.text_profile))
    browser.find_element(*HeaderLocators.button_constructor).click()
    result = browser.find_element(*MainPageLocators.text_collect_burger).text

    assert "Соберите бургер" in result


def test_follow_in_personal_account_to_logo(browser, authorization):
    """
    Тест по клику на логотип Stellar Burgers.
    """
    browser.find_element(*MainPageLocators.button_enter_account).click()
    email = AuthData.email_text_auth
    password = AuthData.pass_text_auth
    authorization(email, password)
    browser.find_element(*AuthPageLocators.button_auth_enter).click()
    WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located(MainPageLocators.button_order))
    browser.find_element(*HeaderLocators.link_personal_account).click()
    browser.find_element(*HeaderLocators.logo_link).click()
    result = browser.find_element(*MainPageLocators.text_collect_burger).text

    assert "Соберите бургер" in result
