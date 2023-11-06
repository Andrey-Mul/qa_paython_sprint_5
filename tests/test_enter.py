from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_enter_button_on_main_list(browser, enter_on_main):
    browser.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
    email = "Andrey_mul_23@yandex.ru"
    password = "123456"
    url = "https://stellarburgers.nomoreparties.site/"
    enter_on_main(email, password)
    browser.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
    result = browser.current_url
    assert url == result


def test_enter_button_on_personal_account(browser, enter_on_main):
    browser.find_element(By.XPATH, "/html/body/div/div/header/nav/a/p").click()
    email = "Andrey_mul_23@yandex.ru"
    password = "123456"
    url = "https://stellarburgers.nomoreparties.site/"
    enter_on_main(email, password)
    browser.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
    result = browser.current_url
    assert url == result


def test_button_in_registration_form(browser, enter_on_main):
    browser.find_element(By.XPATH, "/html/body/div/div/header/nav/a/p").click()
    browser.find_element(By.XPATH, "/html/body/div/div/main/div/div/p[1]/a").click()
    browser.find_element(By.XPATH, "/html/body/div/div/main/div/div/p/a").click()
    email = "Andrey_mul_23@yandex.ru"
    password = "123456"
    url = "https://stellarburgers.nomoreparties.site/"
    enter_on_main(email, password)
    browser.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
    result = browser.current_url
    assert url == result


def test_button_in_password_recovery(browser, enter_on_main):
    browser.find_element(By.XPATH, "/html/body/div/div/header/nav/a/p").click()
    browser.find_element(By.XPATH, "/html/body/div/div/main/div/div/p[2]/a").click()
    browser.find_element(By.XPATH, "/html/body/div/div/main/div/div/p/a").click()
    email = "Andrey_mul_23@yandex.ru"
    password = "123456"
    url = "https://stellarburgers.nomoreparties.site/"
    enter_on_main(email, password)
    browser.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
    result = browser.current_url
    assert url == result
