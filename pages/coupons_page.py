from pages.base_page import BasePage


class CouponsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.url = f"{self.base_url}/coupons"

       
        self.CARD = "button:has-text('View Deal'), button:has-text('Get Coupon')"

       
        self.FILTER_CONTAINER = "div.flex.gap-2.pb-1"
        self.FILTER_BUTTONS = f"{self.FILTER_CONTAINER} button:visible"

   
    def navigate(self):
        self.page.goto(
            self.url,
            timeout=60000,
            wait_until="domcontentloaded"
        )
        self.handle_cookie_popup()
        self.wait_for_page_ready()

       
        self.scroll_full_page()

 
    def verify_page_loaded(self):
        return "coupons" in self.page.url.lower()


    def get_coupon_count(self):
        self.handle_cookie_popup()

        try:
            self.page.wait_for_selector(self.CARD, timeout=15000)
        except:
            print(" Coupons not loaded")
            return 0

        return self.page.locator(self.CARD).count()

   

    def get_all_filters(self):
        self.handle_cookie_popup()

        filters = self.page.locator(self.FILTER_BUTTONS)
        count = filters.count()

        names = []
        valid_indexes = []

        for i in range(count):
            text = filters.nth(i).inner_text().strip()

            
            if text and not any(x in text for x in ["Quick", "Legal", "Sync", "+"]):
                names.append(text)
                valid_indexes.append(i)

        print(f" Coupon Filters: {names}")
        return filters, valid_indexes

    def open_filter_by_index(self, index):
        filters = self.page.locator(self.FILTER_BUTTONS)

        try:
            btn = filters.nth(index)

          
            btn.wait_for(state="visible", timeout=5000)
            btn.scroll_into_view_if_needed()

            btn.click(force=True)

            
            self.page.wait_for_timeout(1000)
            return True

        except Exception as e:
            print(f" Failed to open filter {index}: {e}")
            return False

   

    def verify_dropdown_opened(self):
        try:
            dropdown = self.page.locator(
                "div[role='menu']:visible, "
                "div[role='listbox']:visible, "
                "div.absolute:visible"
            )

            return dropdown.count() > 0 and dropdown.first.is_visible()

        except:
            return False

 

    def get_sort_options(self):
        try:
            options = self.page.locator(
                "div[role='menu']:visible li, "
                "div[role='listbox']:visible li, "
                "div.absolute:visible li, "
                "div.absolute:visible button"
            )

            texts = []
            for i in range(options.count()):
                txt = options.nth(i).inner_text().strip()
                if txt:
                    texts.append(txt)

            print(f" Sort options: {texts}")
            return texts

        except Exception as e:
            print(f" Sort options error: {e}")
            return []

    def verify_sort_dropdown_opened(self):
        options = self.get_sort_options()
        return len(options) > 1

    

    def close_dropdown(self):
        try:
            # Try ESC first
            self.page.keyboard.press("Escape")
            self.page.wait_for_timeout(500)

            # Fallback: click outside
            self.page.mouse.click(10, 10)
            self.page.wait_for_timeout(500)

        except:
            pass

  
    def scroll_full_page(self):
        print(" Scrolling Coupons page...")

        last_height = 0

        for _ in range(6):
            self.page.mouse.wheel(0, 3000)
            self.page.wait_for_timeout(1200)

            new_height = self.page.evaluate("document.body.scrollHeight")

            if new_height == last_height:
                break

            last_height = new_height

        print(" Back to top")
        self.page.evaluate("window.scrollTo(0, 0)")