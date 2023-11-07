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
 Тесты:

 файл -test_successful_registration.py
# тест успешной регистрации
 test_successful_registration
 для каждой проверки нужно увеличить число на 1 Andrey_mul_23 -> Andrey_mul_24
 для каждой проверки нужно увеличить число на 1 Andrey_mul_23@yandex.ru -> Andrey_mul_24@yandex.ru


 Файл - test_error_password_by_registration.py
 # тест наличия ошибки при пароле менее 6-и символов
 test_error_password_less_6_characters_by_registration

 Файл - test_enter.py
 #Тест вход по кнопке «Войти в аккаунт» на главной странице
 test_enter_button_on_main_list

 # Тест вход через личный кабинет
 test_enter_button_on_personal_account

 # Тест вход через кнопку в форме регистрации
 test_button_in_registration_form

 # Тест вход через кнопку в форме восстановления пароля.
 def test_button_in_password_recovery

 # Тест переход по клику на «Личный кабинет» с пользователем, который сделал вход.
 test_follow_personal_account

 # Тест переход по клику на Логотип «Stellar Burgers»
def test_follow_in_personal_account_to_logo

# Тест переход по клику на "Конструктор"
def test_follow_in_personal_account_to_designer

Файл - test_log_out_inpersonal_account.py

# Тест выход по кнопке «Выйти» в личном кабинете.
def test_quit_in_personal_account(browser, enter_on_main):

Файл - section_constructor.py

# Тест переходы к разделу Булки
test_go_to_bread

# Тест переходы к разделу Соусы
test_go_to_sauce

# Тест переходы к разделу Начинки
test_go_to_fillings

____________________________________________________
Локаторы:

Кнопка "Войти в аккаунт" на главной странице
- By.XPATH, "//button[text()='Войти в аккаунт']"

Страница с надпиью "Вход" (ссылка на надпись "Востановление пароля")- url https://stellarburgers.nomoreparties.site/login
- By.XPATH, "/html/body/div/div/main/div/div/p[2]/a"

Ссылка "Зарегистрироваться" - url https://stellarburgers.nomoreparties.site/login
- By.XPATH, "/html/body/div/div/main/div/div/p[1]/a"

Ссылка Войти в окне регистрация
- By.XPATH, "/html/body/div/div/main/div/div/p/a"

Окно регистраций - url https://stellarburgers.nomoreparties.site/register
- By.XPATH, "/html/body/div/div/main/div/h2"

Поле ввода Имя
- By.XPATH, "/html/body/div/div/main/div/form/fieldset[last()-2]/div/div/input"

Поле ввода Email
-By.XPATH, "/html/body/div/div/main/div/form/fieldset[last()-1]/div/div/input"

Поле ввода Пароль
-By.XPATH, "/html/body/div/div/main/div/form/fieldset[last()]/div/div/input"

Кнопка Зарегистрироваться
- By.XPATH, "/html/body/div/div/main/div/form/button"

Надпись ошибки при пароле менее 6-и символов
-By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/p"

Кнопка оформить заказ на главной странице
-By.XPATH, "//button[text()='Оформить заказ']"

Кнопка вход (ввод логина и пароля) - https://stellarburgers.nomoreparties.site/login
-By.XPATH, ".//button[text()='Войти']"

Надпись личный кабинет
-By.XPATH, ".//p[text()='Личный Кабинет']"

Ссылка на восстановление пароля
- By.XPATH, "/html/body/div/div/main/div/div/p[2]/a"

Надпись "Соберите бургер"
-By.XPATH, "/html/body/div/div/main/section[1]/h1"

Ссылка на логотип
-By.XPATH, "/html/body/div/div/header/nav/div/a"

Кнопка "Выход" в личном кабинете
-By.XPATH, "//button[text()='Выход']"

Ссылка для перехода к Булкам
By.XPATH, ".//span[text()='Соусы']"

Ссылка для перехода к Соусам
By.XPATH, ".//span[text()='Соусы']"

Ссылка для перехода к Начинкам
By.XPATH, ".//span[text()='Начинки']"

Надпись Булки
By.XPATH,"/html/body/div/div/main/section[1]/div[2]/h2[1]"

Надпись Соусы
By.XPATH, "/html/body/div/div/main/section[1]/div[2]/h2[2]"

Надпись Начинки
By.XPATH, "/html/body/div/div/main/section[1]/div[2]/h2[3]"
________________________________________________________________________