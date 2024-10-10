import allure
from selene import browser, have


class LoginPage:
    def __init__(self):
        self.user_name = browser.element('//input[@id="user-name"]')
        self.password = browser.element('//input[@id="password"]')
        self.login_button = browser.element('//input[@id="login-button"]')
        self.check_ok_login_by_title = browser.element('//span[@class="title"]')
        self.check_no_login_by_title = browser.element('//h3[@data-test="error"]')

    @allure.step("Вводим логин")
    def fill_user_name(self, value):
        self.user_name.type(value)
        return self

    @allure.step("Вводим пароль")
    def fill_password(self, value):
        self.password.type(value)
        return self

    @allure.step("Нажимаем кнопку логина")
    def click_login_button(self):
        self.login_button.click()
        return self

    @allure.step("Проверка успешного логина")
    def check_after_ok_login(self):
        self.check_ok_login_by_title.should(have.exact_text('Products'))
        return self

    @allure.step("Проверка неуспешного логина")
    def check_after_no_login(self):
        self.check_no_login_by_title.should(have.text('Epic sadface'))
        return self