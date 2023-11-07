from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import AuthPageLocators
from data import RegisterData


def test_successful_registration(browser, register_user):
    """
    Тест на успешную регистрацию.
    Поле «Имя» должно быть не пустым;
    в поле Email введён email в формате логин@домен: например, 123@ya.ru.
    Минимальный пароль — шесть символов.
    Перед запуском теста нужно увеличить Имя и логин на еденицу "Andrey_mul_34" -> "Andrey_mul_35"
    """
    name = RegisterData.name_text_reg  # для проверки увеличить на 1 цифру
    email = RegisterData.email_text_reg  # для проверки увеличить на 1 цифру
    password = RegisterData.pass_text_reg
    register_user(name, email, password)
    WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located(AuthPageLocators.button_auth_enter))
    result = browser.find_element(*AuthPageLocators.button_auth_enter).text

    assert "Войти" in result
