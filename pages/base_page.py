from playwright.sync_api import TimeoutError

class BasePage:
    def __init__(self, page):
        self.page = page
        self.base_url = "https://dealwallet.com"


    def handle_cookie_popup(self):
        try:
           
            self.page.wait_for_selector("text=Cookie", timeout=5000)

            buttons = [
                "button:has-text('Accept All')",
                "button:has-text('Accept')",
                "button:has-text('Agree')",
                "button:has-text('Got it')"
            ]

            for btn in buttons:
                if self.page.locator(btn).count() > 0:
                    self.page.locator(btn).first.click(force=True)
                    print(f" Cookie popup closed using {btn}")
                    self.page.wait_for_timeout(1000)
                    return

          
            self.page.evaluate("""
                document.querySelectorAll('[role="dialog"], .modal, .overlay')
                .forEach(el => el.remove());
            """)
            print(" Cookie popup force removed")

        except:
            pass

    
    def safe_click(self, selector):
        self.handle_cookie_popup()
        el = self.page.locator(selector).first
        el.wait_for(state="visible", timeout=10000)
        el.click(force=True)

    def safe_fill(self, selector, value):
        self.handle_cookie_popup()
        el = self.page.locator(selector).first
        el.wait_for(state="visible", timeout=10000)
        el.fill(value)

    def is_visible(self, selector, timeout=5000):
        try:
            self.handle_cookie_popup()
            self.page.wait_for_selector(selector, timeout=timeout)
            return self.page.locator(selector).first.is_visible()
        except Exception:
            return False

    def wait_for_page_ready(self):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(800)

  
    def verify_page_loaded(self, expected_path=None):
        if expected_path:
            return expected_path in self.page.url
        return self.page.url.startswith(self.base_url)