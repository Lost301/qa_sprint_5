from datetime import datetime

BASE_URL = "https://stellarburgers.education-services.ru/"
PASSWORD = "testpass123"


def generate_credentials():
    # возвращает уникальные email и пароль для регистрации тестового пользователя.
    stamp = datetime.now().strftime("%d%m%H%M%S%f")
    return f"test_user_8_{stamp[-6:]}@yandex.ru", PASSWORD
