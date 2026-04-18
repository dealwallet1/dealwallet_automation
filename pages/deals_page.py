from pages.base_page import BasePage

class DealsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.url = f"{self.base_url}/deals"
        self.CARD = "a[href*='deal']"

        
        self.FILTER_BUTTONS = "button:has(span.whitespace-nowrap)"

   
    def navigate(self):
        self.page.goto(
            self.url,
            timeout=60000,
            wait_until="domcontentloaded"
        )
        self.handle_cookie_popup()
        self.wait_for_page_ready()

    def verify_page_loaded(self):
        return "deals" in self.page.url.lower()

    def get_deals_count(self):
        self.handle_cookie_popup()
        try:
            self.page.wait_for_selector(self.CARD, timeout=10000)
        except:
            print(" Deals not loaded")
            return 0
        return self.page.locator(self.CARD).count()

 

    def get_all_filters(self):
        self.handle_cookie_popup()

        filters = self.page.locator(self.FILTER_BUTTONS)
        count = filters.count()

        names = []
        for i in range(count):
            names.append(filters.nth(i).inner_text().strip())

        print(f" Filters found: {names}")
        return filters, count

    def open_filter_by_index(self, index):
        filters, count = self.get_all_filters()

        if index >= count:
            return False

        try:
            btn = filters.nth(index)
            btn.scroll_into_view_if_needed()
            btn.click(force=True)

            # wait for UI animation
            self.page.wait_for_timeout(1000)
            return True

        except Exception as e:
            print(f" Failed to open filter {index}: {e}")
            return False

 
    def verify_dropdown_opened(self):
        try:
            panels = self.page.locator("div:visible")

            for i in range(panels.count()):
                panel = panels.nth(i)

                if panel.locator("button, label, input, li").count() > 2:
                    return True

            return False

        except Exception as e:
            print(f" Dropdown detection failed: {e}")
            return False

   
    def verify_sort_dropdown_opened(self):
        try:
            self.page.wait_for_timeout(500)

            dropdowns = self.page.locator(
                "div[role='menu'], div[class*='dropdown'], div[class*='menu']"
            )

            for i in range(dropdowns.count()):
                d = dropdowns.nth(i)

                if d.is_visible():
                    if d.locator("div, button, li").count() >= 2:
                        return True

            # fallback detection
            visible_items = self.page.locator("li:visible, button:visible")

            if visible_items.count() > 5:
                return True

            return False

        except Exception as e:
            print(f" Sort dropdown detection failed: {e}")
            return False

  
    def close_dropdown(self):
        try:
            self.page.keyboard.press("Escape")
            self.page.wait_for_timeout(500)

            self.page.mouse.click(0, 0)
            self.page.wait_for_timeout(500)

        except:
            pass

  

    def scroll_page_full(self):
        try:
            print(" Scrolling page from top to bottom...")

            last_height = self.page.evaluate("document.body.scrollHeight")

            while True:
                self.page.mouse.wheel(0, 3000)
                self.page.wait_for_timeout(1000)

                new_height = self.page.evaluate("document.body.scrollHeight")

                if new_height == last_height:
                    break

                last_height = new_height

            print(" Reached bottom of page")

        except Exception as e:
            print(f" Scrolling failed: {e}")

    def scroll_to_top(self):
        try:
            self.page.evaluate("window.scrollTo(0, 0)")
            self.page.wait_for_timeout(500)
            print(" Scrolled back to top")
        except:
            pass