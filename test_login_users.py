from selene import browser, have

from pages.login_page import LoginPage

base_url = 'https://www.saucedemo.com/'
login = LoginPage()

def test_login_standard_user():
    browser.open(base_url)
    login.fill_user_name('standard_user')
    login.fill_password('secret_sauce')
    login.click_login_button()
    login.check_after_ok_login()


def test_locked_out_user():
    browser.open(base_url)
    login.fill_user_name('locked_out_user')
    login.fill_password('secret_sauce')
    login.click_login_button()
    login.check_after_no_login()


def test_problem_user():
    browser.open(base_url)
    login.fill_user_name('problem_user')
    login.fill_password('secret_sauce')
    login.click_login_button()
    login.check_after_ok_login()


def test_performance_glitch_user():
    browser.open(base_url)
    login.fill_user_name('performance_glitch_user')
    login.fill_password('secret_sauce')
    login.click_login_button()
    login.check_after_ok_login()


def test_error_user():
    browser.open(base_url)
    login.fill_user_name('error_user')
    login.fill_password('secret_sauce')
    login.click_login_button()
    login.check_after_ok_login()


def test_visual_user():
    browser.open(base_url)
    login.fill_user_name('visual_user')
    login.fill_password('secret_sauce')
    login.click_login_button()
    login.check_after_ok_login()