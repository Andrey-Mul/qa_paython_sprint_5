import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# Фикстура для создания и завершения сеанса браузера
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# Фикстура для регистрации
@pytest.fixture
def register_user(browser):
    def _register_user(name, email, password):
        browser.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/button").click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/p[2]/a")))
        browser.find_element(By.XPATH, "/html/body/div/div/main/div/div/p[1]/a").click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/h2")))
        browser.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[last()-2]/div/div/input").send_keys(
            name)
        browser.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[last()-1]/div/div/input").send_keys(
            email)
        browser.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[last()]/div/div/input").send_keys(
            password)
        browser.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()

    return _register_user


# Фикстура для входа
@pytest.fixture
def enter_on_main(browser):
    def _enter_on_main(email, password):
        browser.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[last()-1]/div/div/input").send_keys(
            email)
        browser.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[last()]/div/div/input").send_keys(
            password)

    return _enter_on_main
