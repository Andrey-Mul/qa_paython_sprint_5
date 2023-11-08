from selenium.webdriver.common.by import By


class HeaderLocators:
    link_personal_account = (By.XPATH, ".//p[text()='Личный Кабинет']")  # - Надпись личный кабинет
    logo_link = (By.XPATH, "/html/body/div/div/header/nav/div/a")  # - логотип
    button_constructor = (By.XPATH, "/html/body/div/div/header/nav/ul/li[1]/a")  # - Кнопка "Конструктор"


class MainPageLocators:  # - Главная страница https://stellarburgers.nomoreparties.site/

    button_enter_account = (By.XPATH, "//button[text()='Войти в аккаунт']")  # - кнопка "Войти в аккаунт"
    constructor_link_bread = (By.XPATH, ".//span[text()='Булки']")  # - Ссылка "Булки"
    constructor_link_sauce = (By.XPATH, ".//span[text()='Соусы']")  # -Ссылка "Соусы"
    constructor_link_fillings = (By.XPATH, ".//span[text()='Начинки']")  # - Ссылка "Начинки"

    constructor_text_bread = (By.XPATH, ".//h2[1][text()='Булки']")  # - Надпись "Булки"
    constructor_text_sauce = (By.XPATH, ".//h2[2][text()='Соусы']")  # -Надпись "Соусы"
    constructor_text_fillings = (By.XPATH, ".//h2[3][text()='Начинки']")  # - Надпись "Начинки"
    text_collect_burger = (By.XPATH, ".//h1[text()='Соберите бургер']")  # - Надпись "Соберите бургер"
    button_order = (By.XPATH, "//button[text()='Оформить заказ']")  # - Кнопка "оформить заказ"


class AuthPageLocators:  # - Страница входа https://stellarburgers.nomoreparties.site/login

    input_field_email_auth = (By.XPATH, ".//fieldset[last()-1]/div/div/input")  # - Поле ввода Email
    input_field_pass_auth = (By.XPATH, ".//fieldset[last()]/div/div/input")  # - Поле ввода Пароль
    button_auth_enter = (By.XPATH, ".//button[text()='Войти']")  # - Кнопка "Войти"
    link_register = (By.XPATH, "/html/body/div/div/main/div/div/p[1]/a")  # - cсылка "Зарегистрироваться"
    link_recover_password = (By.XPATH, "/html/body/div/div/main/div/div/p[2]/a")  # - ссылка "Востановить пароль"


class RegistrationLocators:  # - Страница регистрации https://stellarburgers.nomoreparties.site/register

    input_field_email_reg = (By.XPATH, ".//fieldset[last()-1]/div/div/input")  # - Поле ввода Email
    input_field_pass_reg = (By.XPATH, ".//fieldset[last()]/div/div/input")  # - Поле ввода Пароль
    input_field_name_reg = (
        By.XPATH, "/html/body/div/div/main/div/form/fieldset[last()-2]/div/div/input")  # - Поле ввода Имя
    link_enter = (By.XPATH, "/html/body/div/div/main/div/div/p/a")  # - Ссылка Войти
    text_registration = (By.XPATH, "/html/body/div/div/main/div/h2")  # - Надпись "Регистрация"
    button_registration = (By.XPATH, "/html/body/div/div/main/div/form/button")  # - Кнопка Зарегистрироваться
    error_pass_text = (By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/p")  # - Надпись ошибки


class Personal_Account:  # - Личный кабинет https://stellarburgers.nomoreparties.site/account/profile

    button_exit_per_acc = (By.XPATH, "//button[text()='Выход']")  # - Кнопка "Выход"
    text_profile = (By.XPATH, "/html/body/div/div/main/div/nav/ul/li[1]")  # - Надпись "Профиль"


class ForgotPassword:
    button_enter_forg = (By.XPATH, "/html/body/div/div/main/div/div/p/a")  # - Ссылка Востановить пароль
