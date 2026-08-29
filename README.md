# Sprint_5

Автотесты учебного сайта Stellar Burgers на Selenium и pytest.

Тестируемый сайт: https://stellarburgers.education-services.ru/

## Запуск

```powershell
python -m pip install -r requirements.txt
pytest -v
```

Тесты используют Google Chrome и Selenium Manager для автоматического подбора драйвера. Каждый тест запускает собственный браузер и закрывает его через фикстуру `driver`.
