import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls
from locators import AuthPageLocators, MainPageLocators, RegistrationLocators

# Фикстура для создания и завершения сеанса браузера
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get(Urls.url_main)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# Фикстура для регистрации
@pytest.fixture
def register_user(browser):
    def _register_user(name, email, password):
        browser.find_element(*MainPageLocators.button_enter_account).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(AuthPageLocators.link_recover_password))
        browser.find_element(*AuthPageLocators.link_register).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(RegistrationLocators.text_registration))
        browser.find_element(*RegistrationLocators.input_field_name_reg).send_keys(name)
        browser.find_element(*RegistrationLocators.input_field_email_reg).send_keys(email)
        browser.find_element(*RegistrationLocators.input_field_pass_reg).send_keys(password)
        browser.find_element(*RegistrationLocators.button_registration).click()

    return _register_user


# Фикстура-функция для авторизации
@pytest.fixture
def authorization(browser):
    def _authorization(email, password):
        browser.find_element(*AuthPageLocators.input_field_email_auth).send_keys(email)
        browser.find_element(*AuthPageLocators.input_field_pass_auth).send_keys(password)

    return _authorization
