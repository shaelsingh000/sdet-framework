from pages.login_page import LoginPage
import pytest

@pytest.mark.xfail(reason="Demo site has no login form")
def test_valid_login(browser):
    login = LoginPage(browser)
    login.login("admin", "password")
