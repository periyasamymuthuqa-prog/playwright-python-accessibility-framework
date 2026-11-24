from playwright.sync_api import Page, expect


class LoginPage:
    URL = "https://saucedemo.com"

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_banner = page.locator("[data-test='error']")

    def navigate(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_login_success(self):
        expect(self.page).to_have_url("https://saucedemo.cominventory.html")
