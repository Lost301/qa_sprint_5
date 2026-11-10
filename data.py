from datetime import datetime


class Urls:
    BASE_URL = "https://stellarburgers.education-services.ru/"


class UserData:
    PASSWORD = "testpass123"


class DataGenerator:
    @staticmethod
    def generate_credentials():
        stamp = datetime.now().strftime("%d%m%H%M%S%f")
        email = f"test_user_8_{stamp[-6:]}@yandex.ru"
        return email, UserData.PASSWORD
