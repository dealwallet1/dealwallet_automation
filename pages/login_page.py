from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        
        self.url = f"{self.base_url}/signin"

        self.EMAIL = "input[type='email']"
        self.PASSWORD = "input[type='password']"

        
        self.SUBMIT = "button:has-text('Sign'), button[type='submit']"

    def navigate(self):
       
        self.page.goto(
            self.url,
            timeout=60000,
            wait_until="domcontentloaded"
        )
        self.handle_cookie_popup()
        self.wait_for_page_ready()

    def login(self, email, password):
        self.navigate()

        
        self.safe_fill(self.EMAIL, email)
        self.safe_fill(self.PASSWORD, password)
        self.safe_click(self.SUBMIT)

        
        self.page.wait_for_timeout(3000)

    def get_login_result(self):
        self.handle_cookie_popup()

        current_url = self.page.url.lower()

        
        if any(k in current_url for k in ["account", "profile", "dashboard"]):
            return {"success": True, "message": "Login successful"}

        
        error_selectors = [
            "text=invalid",
            "text=incorrect",
            "text=failed",
            "text=error"
        ]

        for err in error_selectors:
            if self.page.locator(err).count() > 0:
                return {"success": False, "message": "Login failed"}

        
        if "signin" in current_url or "login" in current_url:
            return {"success": False, "message": "Still on login page"}

       
        return {"success": False, "message": "Unknown state"}