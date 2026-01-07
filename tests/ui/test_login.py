from pages.login_page import LoginPage

def test_valid_login(browser):
    login = LoginPage(browser)
    login.login("admin", "password")
