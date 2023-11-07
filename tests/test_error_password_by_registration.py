from data import RegisterData
from locators import RegistrationLocators


def test_error_password_by_registration(browser, register_user):
    """
    Тест ошибку для некорректного пароля.
    Пароль — менее шести символов.
    """
    name = RegisterData.name_text_reg
    email = RegisterData.email_text_reg
    password = RegisterData.not_correct_pass
    register_user(name, email, password)
    error_text = browser.find_element(*RegistrationLocators.error_pass_text).text
    result = "Некорректный пароль"
    assert result == error_text
