import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_valid_user_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    login_page.assert_login_success()


@pytest.mark.smoke
def test_locked_user_shows_error(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("locked_out_user", "secret_sauce")
    expect(login_page.error_banner).to_contain_text("Sorry, this user has been locked out")
