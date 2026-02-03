# from pages.base_page import BasePage
# from playwright.sync_api import TimeoutError

# class HomePage(BasePage):

#     def __init__(self, page):
#         super().__init__(page)
#         self.page = page
#         self.url = f"{self.config.BASE_URL}/en"

        
#         # HEADER
    
#         self.LOGO = "header img"

#         # User avatar when logged in
#         self.PROFILE_AVATAR = "header img, header button >> nth=1"

#         # Login button (only when logged out)
#         self.SIGNIN_BUTTON = "a:has-text('Login'), a:has-text('Sign In'), button:has-text('Login')"

        
#         # SEARCH BAR (FINAL FIX)
#         # self.SEARCH_INPUT = (
#         #     "input[placeholder='Search for products'], "
#         #     "input.input.input-bordered, "
#         #     "input[type='text'][class*='input']"
#         # )
#         self.SEARCH_INPUT = "input[placeholder='Search for products']"
        

#         # HERO SECTION
#         self.BANNER_SECTION = "h1:has-text('Discover'), h2:has-text('Real Deals')"

#         # FEATURE CARDS
#         self.FEATURE_CARD = "div:has(h3), section div:has(h3)"

#         # FOOTER
#         self.FOOTER = "footer"
#         self.SOCIAL_LINKS = [
#             "footer a[href*='facebook']",
#             "footer a[href*='linkedin']",
#             "footer a[href*='instagram']",
#             "footer a[href^='mailto']"
#         ]

#     # NAVIGATION
#     def navigate(self):
#         self.page.goto(self.url, wait_until="domcontentloaded", timeout=60000)
#         self.wait_for_overlays_to_disappear()
#         self.wait_for_page_ready()
#         self.page.wait_for_timeout(800)

#     def verify_home_loaded(self):
#         return "dealwallet" in self.page.url.lower()

    
#     # BANNER
#     def verify_banner_visible(self):
#         return self.is_visible(self.BANNER_SECTION, timeout=5000)


# pages/home_page.py
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = f"{self.base_url}/en"

        self.LOGO = "header img"
        self.SEARCH_INPUT = "input[placeholder='Search for products']"
        self.BANNER = "h1, h2"

    def navigate(self):
        self.page.goto(self.url)
        self.handle_cookie_popup()
        self.wait_for_page_ready()

    def verify_banner_visible(self):
        return self.is_visible(self.BANNER)


    # FEATURE CARDS
    def get_feature_card_count(self):
        try:
            return self.page.locator(self.FEATURE_CARD).count()
        except:
            return 0

    # FOOTER
    def verify_footer_visible(self):
        return self.is_visible(self.FOOTER, timeout=5000)

    def verify_social_links(self):
        found = []
        for sel in self.SOCIAL_LINKS:
            if self.is_visible(sel):
                found.append(sel)
        return found

    # CLICKS
    def click_logo(self):
        self.click(self.LOGO)

    def click_signin(self):
        self.click(self.SIGNIN_BUTTON)

    # SEARCH BAR ACTION
    def perform_search(self, query):
        locator = self.page.locator(self.SEARCH_INPUT)

        if locator.count() == 0:
            return False

        locator.first.fill(query)
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(1500)

        return True

