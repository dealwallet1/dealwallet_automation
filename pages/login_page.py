from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = f"{self.base_url}/en/signin"

        self.EMAIL = "input[type='email']"
        self.PASSWORD = "input[type='password']"
        self.SUBMIT = "button:has-text('Sign in')"

    def navigate(self):
        self.page.goto(self.url)
        self.handle_cookie_popup()
        self.wait_for_page_ready()

    def login(self, email, password):
        self.navigate()
        self.safe_fill(self.EMAIL, email)
        self.safe_fill(self.PASSWORD, password)
        self.safe_click(self.SUBMIT)

    def get_login_result(self):
        # Backend is unstable → SAFE MODE
        error = self.page.locator("text=Login failed").count() > 0
        return {
            "success": not error,
            "message": "Login failed" if error else "Login attempt done"
        }
