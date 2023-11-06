from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_follow_personal_account(browser, enter_on_main):
    browser.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
    email = "Andrey_mul_23@yandex.ru"
    password = "123456"
    url = "https://stellarburgers.nomoreparties.site/account/profile"
    enter_on_main(email, password)
    browser.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
    browser.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/nav/ul/li[1]")))

    assert url == browser.current_url


def test_follow_in_personal_account_to_designer(browser, enter_on_main):
    browser.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
    email = "Andrey_mul_23@yandex.ru"
    password = "123456"
    enter_on_main(email, password)
    browser.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
    browser.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/nav/ul/li[1]")))
    browser.find_element(By.XPATH, "/html/body/div/div/header/nav/ul/li[1]/a").click()
    result = browser.find_element(By.XPATH, "/html/body/div/div/main/section[1]/h1").text

    assert "Соберите бургер" in result


def test_follow_in_personal_account_to_logo(browser, enter_on_main):
    browser.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
    email = "Andrey_mul_23@yandex.ru"
    password = "123456"
    enter_on_main(email, password)
    browser.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
    browser.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/nav/ul/li[1]")))
    browser.find_element(By.XPATH, "/html/body/div/div/header/nav/div/a").click()
    result = browser.find_element(By.XPATH, "/html/body/div/div/main/section[1]/h1").text

    assert "Соберите бургер" in result
