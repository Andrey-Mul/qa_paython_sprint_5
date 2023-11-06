from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_quit_in_personal_account(browser, enter_on_main):
    browser.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
    email = "Andrey_mul_23@yandex.ru"
    password = "123456"
    url = "https://stellarburgers.nomoreparties.site/login"
    enter_on_main(email, password)
    browser.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
    browser.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/nav/ul/li[1]")))
    browser.find_element(By.XPATH, "//button[text()='Выход']").click()
    WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/p[1]/a")))

    assert url == browser.current_url
