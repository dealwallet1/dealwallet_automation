from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.url = f"{self.base_url}/"

        
        self.LOGO = "header a"

        self.SEARCH_INPUT = "input[type='search'], input[placeholder*='Search']"

        self.BANNER = "h1, h2"

        self.FEATURE_CARD = "a[href*='deal']"

        self.FOOTER = "footer"

        self.SOCIAL_LINKS = [
            "a[href*='facebook']",
            "a[href*='twitter']",
            "a[href*='instagram']"
        ]

        self.SIGNIN_BUTTON = "a[href*='signin']"

    def navigate(self):
        
        self.page.goto(
            self.url,
            timeout=60000,
            wait_until="domcontentloaded"
        )
        self.handle_cookie_popup()
        self.wait_for_page_ready()

    # ❗ FIX 5: Strong banner validation
    def verify_banner_visible(self):
        try:
            self.page.wait_for_selector(self.BANNER, timeout=5000)
            return self.page.locator(self.BANNER).count() > 0
        except:
            return False

    def get_feature_card_count(self):
        self.handle_cookie_popup()
        return self.page.locator(self.FEATURE_CARD).count()

    def verify_footer_visible(self):
        return self.is_visible(self.FOOTER)

    def verify_social_links(self):
        found = []
        for sel in self.SOCIAL_LINKS:
            if self.is_visible(sel):
                found.append(sel)
        return found

    def click_logo(self):
        self.page.wait_for_selector(self.LOGO)
        self.safe_click(self.LOGO)

    def click_signin(self):
        self.safe_click(self.SIGNIN_BUTTON)

    def perform_search(self, query):
        self.handle_cookie_popup()

        locator = self.page.locator(self.SEARCH_INPUT)

        if locator.count() == 0:
            print(" Search input not found")
            return False

        locator.first.fill(query)
        self.page.keyboard.press("Enter")

        self.page.wait_for_timeout(2000)

        return True