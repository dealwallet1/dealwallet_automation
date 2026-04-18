from pages.base_page import BasePage

class CategoriesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

       
        self.url = f"{self.base_url}/categories"

       
        self.CARD = "a[href*='category'], a[href*='categories']"

    def navigate(self):
        
        self.page.goto(
            self.url,
            timeout=60000,
            wait_until="domcontentloaded"
        )
        self.handle_cookie_popup()
        self.wait_for_page_ready()

    def get_category_count(self):
       
        self.handle_cookie_popup()

        try:
            self.page.wait_for_selector(self.CARD, timeout=10000)
        except:
            print(" Category cards not found, returning 0")
            return 0

        return self.page.locator(self.CARD).count()

    def verify_page_loaded(self):
       
        return "categories" in self.page.url.lower()