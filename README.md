Для запуска тестов в терминале: `pytest`

Если необходимо запустить только один тест, 
то нужно указать его название через двоеточие; 
`pytest test_google.py::test_first`

Для запуска Allure отчета:
`allure serve allure-results`

`pytest --co`,  `pytest --collect-only` - позволяет вывести все доступные тесты в директории/проекте

`pytest --setup-plan` # тесты не запускает, но выводит план запуска тестов

`pytest -v (pytest --verbose)` # выводит более подробную информацию о тестах

`pytest -s` выводит вывод тестов в реальном времени

`pytest -rfEX` - выводит только ошибки и отчёт о тестах