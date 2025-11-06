from pages.base_page import BasePage
from playwright.sync_api import Page

class LoginPage(BasePage):
    EMAIL_INPUT = 'input[type="email"][placeholder="you@example.com"]'
    PASSWORD_INPUT = 'input[type="password"][placeholder="••••••••"]'
    SIGNIN_BUTTON = 'button[type="submit"]:has-text("Sign In")'
    ERROR_MESSAGE = 'text=Invalid login credentials'  
    SUCCESS_INDICATOR = 'text=Welcome'  
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = f"{self.config.BASE_URL}/en/signin"
    
    def navigate(self):
        """Navigate to login page"""
        self.navigate_to(self.url)
        self.handle_cookie_popup()
    
    def enter_email(self, email: str):
        """Enter email in the email field"""
        self.fill(self.EMAIL_INPUT, email)
    
    def enter_password(self, password: str):
        """Enter password in the password field"""
        self.fill(self.PASSWORD_INPUT, password)
    
    def click_signin(self):
        """Click the Sign In button"""
        self.click(self.SIGNIN_BUTTON)
    
    def login(self, email: str, password: str):
        """Complete login process"""
        self.enter_email(email)
        self.enter_password(password)
        self.click_signin()
        self.page.wait_for_timeout(2000) 
    
    def get_error_message(self) -> str:
        """Get error message text if present"""
        try:
        
            error_selector = 'div[role="alert"]:has-text("Invalid")'
            if self.is_visible(error_selector, timeout=3000):
                return self.get_text(error_selector)
            return ""
        except:
            return ""
    
    def is_login_successful(self) -> bool:
        """Check if login was successful"""
        try:

            self.page.wait_for_timeout(2000)
            current_url = self.page.url
            
            if 'signin' not in current_url and 'login' not in current_url:
                return True
            
            
            error = self.get_error_message()
            if error:
                return False
            
            return False
        except:
            return False
    
    def get_login_result(self) -> dict:
        """Get login result with status and message"""
        is_success = self.is_login_successful()
        error_msg = self.get_error_message() if not is_success else ""
        
        return {
            'success': is_success,
            'message': error_msg if error_msg else ('Login successful' if is_success else 'Login failed')
        }