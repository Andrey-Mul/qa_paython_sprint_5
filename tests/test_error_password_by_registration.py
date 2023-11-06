# Тест для успешной регистрации
from selenium.webdriver.common.by import By


def test_error_password_by_registration(browser, register_user):
    name = "Andrey_mul_23"
    email = "Andrey_mul_23@yandex.ru"
    password = "12345"
    register_user(name, email, password)
    error_text = browser.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/p").text
    result = "Некорректный пароль"
    assert result in error_text
