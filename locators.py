from selenium.webdriver.common.by import By


class Locators:
    LOGIN_MAIN = (By.CSS_SELECTOR, "button[class*='button_size_large']")  # Кнопка «Войти в аккаунт»
    PERSONAL_ACCOUNT = (By.CSS_SELECTOR, "a[href='/account']")  # Личный кабинет
    CONSTRUCTOR = (By.CSS_SELECTOR, "a[href='/'] p")  # Конструктор
    LOGO = (By.CSS_SELECTOR, "a[href='/'] svg")  # Логотип
    REGISTER_EMAIL = (By.XPATH, "(//label[normalize-space()='Email']/following-sibling::input)[1]")  # Email регистрации
    LOGIN_EMAIL = (By.XPATH, "(//input[@type='text'])[1]")  # Email входа
    PASSWORD = (By.CSS_SELECTOR, "input[type='password']")  # Пароль
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "form button")  # Вход
    REGISTER_LINK = (By.CSS_SELECTOR, "a[href='/register']")  # Регистрация
    REGISTER_SUBMIT = (By.CSS_SELECTOR, "form button")  # Регистрация
    NAME = (By.XPATH, "(//div[contains(@class, 'input_type_text')])[1]//input")  # Имя
    LOGIN_FROM_REGISTER = (By.CSS_SELECTOR, "a[href='/login']")  # Вход из регистрации
    FORGOT_PASSWORD = (By.CSS_SELECTOR, "a[href='/forgot-password']")  # Восстановление
    LOGIN_FROM_FORGOT = (By.XPATH, "(//a[@href='/login'])[last()]")  # Вход из восстановления
    INVALID_PASSWORD = (By.CSS_SELECTOR, "form p")  # Ошибка пароля
    PROFILE = (By.CSS_SELECTOR, "a[href='/account/profile']")  # Профиль
    LOGOUT = (By.CSS_SELECTOR, "button[type='button']")  # Выход
    BUNS = (By.XPATH, "//div[contains(@class, 'tab_tab')][.//span]")  # Булки
    SAUCES = (By.XPATH, "(//div[contains(@class, 'tab_tab')][.//span])[2]")  # Соусы
    FILLINGS = (By.XPATH, "(//div[contains(@class, 'tab_tab')][.//span])[3]")  # Начинки
