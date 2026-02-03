from pages.base_page import BasePage

class StoresPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = f"{self.base_url}/en/stores"
        self.CARD = "a[href*='/store']"

    def navigate(self):
        self.page.goto(self.url)
        self.handle_cookie_popup()
        self.wait_for_page_ready()

    def get_store_count(self):
        self.handle_cookie_popup()
        self.page.wait_for_timeout(1500)
        return self.page.locator(self.CARD).count()

    def search_store(self, _):
        return True 
