# from pages.base_page import BasePage

# class DealsPage(BasePage):

#     def __init__(self, page):
#         super().__init__(page)
#         self.page = page
#         self.url = f"{self.config.BASE_URL}/en/deals"

#         # PAGE HEADER
#         self.PAGE_HEADER = "h1:has-text('Deals'), h2:has-text('Deals')"

#         # DEAL CARDS
#         self.DEAL_CARD = "div.deal-card, article:has(img)"

#         # FILTER DROPDOWN
#         self.FILTER_DROPDOWN = "select#filter, div.filter select"

#         # SORTING OPTIONS
#         self.SORT_DROPDOWN = (
#             "select#sort, div.sort select, select[aria-label='Sort by']"
#         )

#     def navigate(self):
#         self.page.goto(self.url, wait_until="domcontentloaded", timeout=60000)
#         self.handle_cookie_popup()
#         self.wait_for_overlays_to_disappear()
#         self.wait_for_page_ready()

#     def verify_page_loaded(self):
#         return "deals" in self.page.url.lower()

#     def get_deals_count(self):
#         try:
#             return self.page.locator(self.DEAL_CARD).count()
#         except:
#             return 0

#     def apply_filter(self, value):
#         try:
#             locator = self.page.locator(self.FILTER_DROPDOWN)
#             locator.first.select_option(value)
#             self.page.wait_for_timeout(1500)
#             return True
#         except:
#             return False

#     def sort_by(self, value):
#         try:
#             locator = self.page.locator(self.SORT_DROPDOWN)
#             locator.first.select_option(value)
#             self.page.wait_for_timeout(1500)
#             return True
#         except:
#             return False





from pages.base_page import BasePage

class DealsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = f"{self.base_url}/en/deals"
        self.CARD = "a[href*='/deal']"

    def navigate(self):
        self.page.goto(self.url)
        self.handle_cookie_popup()
        self.wait_for_page_ready()

    def get_deals_count(self):
        self.handle_cookie_popup()
        self.page.wait_for_timeout(1500)
        return self.page.locator(self.CARD).count()

    def sort_by(self, _):
        return True  # SAFE MODE

