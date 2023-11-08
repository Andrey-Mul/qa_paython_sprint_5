from data import AuthData
from locators import AuthPageLocators
from locators import MainPageLocators
from locators import HeaderLocators
from locators import RegistrationLocators
from locators import ForgotPassword


def test_enter_button_on_main_list(browser, authorization):
    """
    Тест входа по кнопке «Войти в аккаунт» на главной странице
    """
    browser.find_element(*MainPageLocators.button_enter_account).click()
    email = AuthData.email_text_auth
    password = AuthData.pass_text_auth
    authorization(email, password)
    browser.find_element(*AuthPageLocators.button_auth_enter).click()
    expected = browser.find_element(*MainPageLocators.button_order).text
    result = "Оформить заказ"
    assert expected == result


def test_enter_button_on_personal_account(browser, authorization):
    """
    Тест входа через кнопку «Личный кабинет»
    """
    browser.find_element(*HeaderLocators.link_personal_account).click()
    email = AuthData.email_text_auth
    password = AuthData.pass_text_auth
    authorization(email, password)
    browser.find_element(*AuthPageLocators.button_auth_enter).click()
    expected = browser.find_element(*MainPageLocators.button_order).text
    result = "Оформить заказ"
    assert expected == result


def test_enter_button_in_registration_form(browser, authorization):
    """
    Тест входа через кнопку в форме регистрации
    """
    browser.find_element(*HeaderLocators.link_personal_account).click()
    browser.find_element(*AuthPageLocators.link_register).click()
    browser.find_element(*RegistrationLocators.link_enter).click()
    email = AuthData.email_text_auth
    password = AuthData.pass_text_auth
    authorization(email, password)
    browser.find_element(*AuthPageLocators.button_auth_enter).click()
    expected = browser.find_element(*MainPageLocators.button_order).text
    result = "Оформить заказ"
    assert expected == result


def test_button_in_password_recovery(browser, authorization):
    """
    Тест вход через кнопку в форме восстановления пароля
    """
    browser.find_element(*HeaderLocators.link_personal_account).click()
    browser.find_element(*AuthPageLocators.link_recover_password).click()
    browser.find_element(*ForgotPassword.button_enter_forg).click()
    email = AuthData.email_text_auth
    password = AuthData.pass_text_auth
    authorization(email, password)
    browser.find_element(*AuthPageLocators.button_auth_enter).click()
    expected = browser.find_element(*MainPageLocators.button_order).text
    result = "Оформить заказ"
    assert expected == result
