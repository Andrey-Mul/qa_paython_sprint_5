from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators, AuthPageLocators, HeaderLocators, Personal_Account
from data import AuthData


def test_quit_in_personal_account(browser, authorization):
    """
    Тест выхода по кнопке «Выйти» в личном кабинете.
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
    browser.find_element(*Personal_Account.button_exit_per_acc).click()
    browser.find_element(*HeaderLocators.link_personal_account).click()
    result = browser.find_element(*AuthPageLocators.button_auth_enter).text

    assert "Войти" in result
