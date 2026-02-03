# from playwright.sync_api import Page
# from utils.config import BASE_URL

# class BasePage:
#     """Base page containing common actions and utilities for all pages"""

#     def __init__(self, page: Page):
#         self.page = page
#         self.config = type("Config", (), {"BASE_URL": BASE_URL})  # keep BASE_URL consistent

#     # Basic reusable actions
#     def navigate_to(self, url: str):
#         """Navigate to a given URL"""
#         self.page.goto(url, wait_until="load")

#     def click(self, selector: str):
#         """Click on a given selector"""
#         self.page.locator(selector).click()

#     def fill(self, selector: str, text: str):
#         """Fill text into an input field"""
#         self.page.locator(selector).fill(text)

#     def is_visible(self, selector: str, timeout: int = 5000):
#         """Check if an element is visible within timeout"""
#         try:
#             return self.page.locator(selector).is_visible(timeout=timeout)
#         except:
#             return False

#     def get_text(self, selector: str):
#         """Get text from element"""
#         try:
#             return self.page.locator(selector).text_content().strip()
#         except:
#             return None

#     # Cookie popup and overlay utils
#     def handle_cookie_popup(self):
#         """Handle cookie consent popup if visible"""
#         cookie_selectors = [
#             'button:has-text("Accept")',
#             'button:has-text("Allow all")',
#             'button:has-text("OK")',
#             'text=Accept All',
#             'text=Got it',
#         ]
#         for sel in cookie_selectors:
#             try:
#                 if self.page.locator(sel).is_visible():
#                     self.page.locator(sel).click()
#                     self.page.wait_for_timeout(1000)
#                     print(f"Cookie popup handled with selector: {sel}")
#                     return True
#             except Exception:
#                 continue 
#         return False

#     def wait_for_overlays_to_disappear(self, timeout: int = 10000):
#         """
#         Wait for Cloudflare / loading overlays / popups to disappear
#         """
#         overlay_selectors = [
#             ".cf-modal", "#cf-overlay", ".loading-overlay",
#             ".spinner", ".backdrop", "div[role='dialog']"
#         ]
#         for selector in overlay_selectors:
#             try:
#                 self.page.wait_for_selector(selector, state="hidden", timeout=timeout)
#             except Exception:
#                 pass

#     def wait_for_page_ready(self):
#         """Ensure DOM & network are stable"""
#         try:
#             self.page.wait_for_load_state("networkidle", timeout=10000)
#         except Exception:
#             pass

    
#     # Scroll helpers
#     def scroll_to_bottom(self):
#         self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
#         self.page.wait_for_timeout(1000)

#     def scroll_to_top(self):
#         self.page.evaluate("window.scrollTo(0, 0)")
#         self.page.wait_for_timeout(500)


from playwright.sync_api import TimeoutError

class BasePage:
    def __init__(self, page):
        self.page = page
        self.base_url = "https://dealwallet.com"

    # ---------------- COOKIE / OVERLAY ----------------
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

    # ---------------- SAFE ACTIONS ----------------
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

    # ---------------- GENERIC PAGE CHECK ----------------
    def verify_page_loaded(self):
        return self.page.url.startswith(self.base_url)
