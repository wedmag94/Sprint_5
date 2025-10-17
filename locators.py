from selenium.webdriver.common.by import By


class MainPageLocators:
    # Локаторы для главной страницы
    LOGIN_IN_TO_ACCOUNT_BUTTON = (
        By.XPATH,
        "//button[text()='Войти в аккаунт']",
    )  # Кнопка Войти в аккаунт
    PERSONAL_ACCAUNT_BUTTON = (
        By.XPATH,
        "//p[text() = 'Личный Кабинет']",
    )  # Кнопка Личный кабнет
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text() = 'Конструктор']")  # Кнопка Конструктор
    STELLAR_BURGERS_LOGO = (
        By.CLASS_NAME,
        "AppHeader_header__logo__2D0X2",
    )  # Логотип StellarBurgers


class LoginPageLocators:
    # Локаторы для страницы входа
    EMAIL = (By.NAME, "name")  # Поле ввода email
    PASSWORD = (By.NAME, "Пароль")  # Поле ввода пароля
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')  # Кнопка "Войти"
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")  # Ссылка Зарегистрироваться
    RECOVER_PASSWORD_LINK = (
        By.LINK_TEXT,
        "Восстановить пароль",
    )  # Ссылка на восстановление пароля


class RegisterPageLocators:
    # Локаторы для регистрации
    NAME = (By.XPATH, "//div[label[text()='Имя']]//input")  # Поле ввода имени
    EMAIL = (By.XPATH, "//div[label[text()='Email']]//input")  # Поле ввода email
    PASSWORD = (By.XPATH, "//div[label[text()='Пароль']]//input")  # Поле ввода пароля
    REG_BUTTON = (
        By.XPATH,
        "//button[text()='Зарегистрироваться']",
    )  # Кнопка Зарегистрироваться
    LOGIN_LINK = (By.LINK_TEXT, "Войти")  # Ссылка Войти
    PASSWORD_ERROR = (
        By.XPATH,
        "//p[contains(@class, 'input__error')]",
    )  # Ошибка пароля


class ProfilePageLocators:
    # Локаторы для личного кабинета
    PROFILE_LINK = (By.XPATH, "//a[text() = 'Профиль']")  # Ссылка "Профиль" в меню
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка выхода
    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//p[text()='Конструктор']",
    )  # Кнопка конструктора из ЛК


class ForgotPasswordLocators:
    LOG_LINK = (By.XPATH, "//a[text()='Войти']")


class ConstructorLocators:
    BUNS = (
        By.XPATH,
        "//div[contains(@class, 'tab_tab__1SPyG') and span[text()='Булки']]",
    )  # Кнопка раздела "Булки"
    SAUCES = (
        By.XPATH,
        "//div[contains(@class, 'tab_tab__1SPyG') and span[text()='Соусы']]",
    )  # Кнопка раздела "Соусы"
    TOPPINGS = (
        By.XPATH,
        "//div[contains(@class, 'tab_tab__1SPyG') and span[text()='Начинки']]",
    )  # Кнопка раздела "Начинки"

    BUNS_ACTIVE = (
        By.XPATH,
        "//div[contains(@class,'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect') and span[text()='Булки']]",
    )  # Активная кнопка раздела "Булки"
    SAUCES_ACTIVE = (
        By.XPATH,
        "//div[contains(@class,'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect') and span[text()='Соусы']]",
    )  # Активная кнопка раздела "Соусы"
    TOPPINGS_ACTIVE = (
        By.XPATH,
        "//div[contains(@class,'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect') and span[text()='Начинки']]",
    )  # Активная кнопка раздела "Начинки"

    CONSTRUCTOR = (
        By.XPATH,
        "//div[contains(@class,'BurgerIngredients_ingredients__menuContainer__Xu3Mo')]",
    )
