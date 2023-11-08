# Тестирование Stellar Burgers url = https://stellarburgers.nomoreparties.site/

1. WebDriver  119.0.6045.105

2. Команда для запуска — pytest -v
__________________________________________________
Фикстуры - conftest.py:

- browser
инициализирует webdriver
открывает - ссылку на тестируемый сайт

- register_user
функция пошагового проходжения регистраций

___________________________________________________
# Тесты:

# Тест успешной регистрации файл -test_successful_registration.py

 test_successful_registration
 для каждой проверки нужно увеличить число на 1 Andrey_mul_23 -> Andrey_mul_24
 для каждой проверки нужно увеличить число на 1 Andrey_mul_23@yandex.ru -> Andrey_mul_24@yandex.ru


 # Тест наличия ошибки при пароле менее 6-и символов - Файл test_error_password_by_registration.py
 test_error_password_less_6_characters_by_registration

 
# Тест вход по кнопке «Войти в аккаунт» на главной странице - Файл test_enter.py
test_enter_button_on_main_list

# Тест вход через личный кабинет
test_enter_button_on_personal_account

# Тест вход через кнопку в форме регистрации
test_enter_button_in_registration_form

# Тест вход через кнопку в форме восстановления пароля.
test_button_in_password_recovery

# Тест переход по клику на «Личный кабинет» с пользователем, который сделал вход.
test_follow_personal_account

# Тест переход по клику на Логотип «Stellar Burgers»
test_follow_in_personal_account_to_logo

# Тест переход по клику на "Конструктор"
test_follow_in_personal_account_to_designer


# Тест выход по кнопке «Выйти» в личном кабинете - Файл test_log_out_inpersonal_account.py
test_quit_in_personal_account


# Тест переходы к разделу Булки - Файл section_constructor.py
test_go_to_bread

# Тест переходы к разделу Соусы
test_go_to_sauce

# Тест переходы к разделу Начинки
test_go_to_fillings

