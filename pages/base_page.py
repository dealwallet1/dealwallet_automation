from playwright.sync_api import Page, expect
from utils.config import Config

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.config = Config()
        self.page.set_default_timeout(self.config.TIMEOUT)
    
    def navigate_to(self, url: str):
        """Navigate to a specific URL"""
        self.page.goto(url)
    
    def click(self, selector: str):
        """Click on an element"""
        self.page.click(selector)
    
    def fill(self, selector: str, text: str):
        """Fill input field with text"""
        self.page.fill(selector, text)
    
    def get_text(self, selector: str) -> str:
        """Get text content of an element"""
        return self.page.locator(selector).text_content()
    
    def is_visible(self, selector: str, timeout: int = 5000) -> bool:
        """Check if element is visible"""
        try:
            self.page.wait_for_selector(selector, state='visible', timeout=timeout)
            return True
        except:
            return False
    
    def wait_for_selector(self, selector: str, state: str = 'visible', timeout: int = None):
        """Wait for a selector to be in a specific state"""
        if timeout is None:
            timeout = self.config.TIMEOUT
        self.page.wait_for_selector(selector, state=state, timeout=timeout)
    
    def get_attribute(self, selector: str, attribute: str) -> str:
        """Get attribute value of an element"""
        return self.page.locator(selector).get_attribute(attribute)
    
    def handle_cookie_popup(self):
        """Handle cookie consent popup if it appears"""
        try:
            accept_button = 'button:has-text("Accept All")'
            if self.is_visible(accept_button, timeout=3000):
                self.click(accept_button)
                self.page.wait_for_timeout(1000)
        except:
            pass 