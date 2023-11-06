# Тест для успешной регистрации
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_successful_registration(browser, register_user):
    name = "Andrey_mul_30"  # для проверки увеличить на 1 цифру
    email = "Andrey_mul_30@yandex.ru"  # для проверки увеличить на 1 цифру
    password = "123456"
    url = "https://stellarburgers.nomoreparties.site/login"
    register_user(name, email, password)
    WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/p[2]/a")))
    assert url == browser.current_url


def test_error_password_less_6_characters_by_registration(browser, register_user):
    name = "Andrey_mul_23"
    email = "Andrey_mul_23@yandex.ru"
    password = "12345"
    url = "https://stellarburgers.nomoreparties.site/login"
    register_user(name, email, password)
    error_text = browser.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/p").text
    result = "Некорректный пароль"
    assert result in error_text
