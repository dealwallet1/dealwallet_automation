# from pages.base_page import BasePage

# class CategoriesPage(BasePage):

#     def __init__(self, page):
#         super().__init__(page)
#         self.page = page
#         self.url = f"{self.config.BASE_URL}/en/categories"

#         # PAGE TITLE / HEADER
#         self.PAGE_HEADER = "h1:has-text('Categories'), h2:has-text('Categories')"

#         # CATEGORY CARDS
#         self.CATEGORY_CARD = "div.category-card, div:has(a):has(img)"

#         # CATEGORY SEARCH BAR
#         self.CATEGORY_SEARCH = (
#             "input[placeholder='Search categories'], "
#             "input[type='text'], input.input-bordered"
#         )

#     # NAVIGATION
#     def navigate(self):
#         self.page.goto(self.url, wait_until="domcontentloaded", timeout=60000)
#         self.handle_cookie_popup()
#         self.wait_for_overlays_to_disappear()
#         self.wait_for_page_ready()

#     def verify_page_loaded(self):
#         return "categories" in self.page.url.lower()

#     def get_category_count(self):
#         try:
#             return self.page.locator(self.CATEGORY_CARD).count()
#         except:
#             return 0

#     def search_category(self, query):
#         try:
#             locator = self.page.locator(self.CATEGORY_SEARCH)
#             if locator.count() == 0:
#                 return False
#             locator.first.fill(query)
#             self.page.keyboard.press("Enter")
#             self.page.wait_for_timeout(1200)
#             return True
#         except:
#             return False


from pages.base_page import BasePage

class CategoriesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = f"{self.base_url}/en/categories"
        self.CARD = "a[href*='/category']"

    def navigate(self):
        self.page.goto(self.url)
        self.handle_cookie_popup()
        self.wait_for_page_ready()

    def get_category_count(self):
        self.handle_cookie_popup()
        self.page.wait_for_timeout(1500)
        return self.page.locator(self.CARD).count()
