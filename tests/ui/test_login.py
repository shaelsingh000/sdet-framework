from pages.login_page import LoginPage

def test_valid_login(driver):
    login = LoginPage(driver)
    login.login("admin", "password")
