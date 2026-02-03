
from playwright.sync_api import TimeoutError

class BasePage:
    def __init__(self, page):
        self.page = page
        self.base_url = "https://dealwallet.com"

    def handle_cookie_popup(self):
        modal = self.page.locator("div:has-text('Cookie Settings')")

        if modal.count() == 0:
            return

        buttons = [
            "button:has-text('Accept All')",
            "button:has-text('Accept')",
            "button:has-text('Confirm My Choices')",
        ]

        for btn in buttons:
            try:
                b = self.page.locator(btn).first
                if b.is_visible(timeout=3000):
                    b.click(force=True)
                    self.wait_for_overlays_to_disappear()
                    print(f"Cookie popup closed using {btn}")
                    return
            except Exception:
                pass

        print("Cookie popup detected but not clickable")

    def wait_for_overlays_to_disappear(self):
        try:
            self.page.wait_for_selector(
                "div:has-text('Cookie Settings')",
                state="hidden",
                timeout=8000
            )
        except TimeoutError:
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
            return self.page.locator(selector).first.is_visible(timeout=timeout)
        except Exception:
            return False

    def wait_for_page_ready(self):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(800)

    def verify_page_loaded(self):
        return self.page.url.startswith(self.base_url)
