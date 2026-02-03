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

