from pages.base_page import BasePage

class StoresPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        
        self.url = f"{self.base_url}/stores"

        
        self.CARD = "a[href*='store']"

       
        self.FILTER_BUTTONS = "button:has(span.whitespace-nowrap)"

 
    def navigate(self):
        self.page.goto(
            self.url,
            timeout=60000,
            wait_until="domcontentloaded"
        )
        self.handle_cookie_popup()
        self.wait_for_page_ready()

    
    def get_store_count(self):
        self.handle_cookie_popup()

        try:
            self.page.wait_for_selector(self.CARD, timeout=10000)
        except:
            print(" Store cards not found, returning 0")
            return 0

        return self.page.locator(self.CARD).count()

   
    def search_store(self, store_name):
        self.handle_cookie_popup()

        search_box = self.page.locator(
            "input[type='search'], input[placeholder*='Search']"
        )

        if search_box.count() == 0:
            print(" Search input not found")
            return False

        search_box.first.fill(store_name)
        self.page.keyboard.press("Enter")

        self.page.wait_for_timeout(2000)

        results = self.page.locator(self.CARD).count()
        return results > 0

   
    def verify_page_loaded(self):
        return "stores" in self.page.url.lower()

   

    def get_all_filters(self):
        self.handle_cookie_popup()

        filters = self.page.locator(self.FILTER_BUTTONS)
        count = filters.count()

        names = []
        for i in range(count):
            text = filters.nth(i).inner_text().strip()
            names.append(text)

        print(f" Store Filters found: {names}")
        return filters, count

    def open_filter_by_index(self, index):
        filters, count = self.get_all_filters()

        if index >= count:
            return False

        btn = filters.nth(index)

        try:
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
                "div[role='menu'], div[role='listbox'], div.absolute"
            )

            if dropdown.count() > 0:
                return dropdown.first.is_visible()

            return False

        except Exception as e:
            print(f" Dropdown detection failed: {e}")
            return False

    def verify_sort_dropdown_opened(self):
        try:
           
            options = self.page.locator("li, button")

            return options.count() > 3

        except Exception as e:
            print(f" Sort dropdown detection failed: {e}")
            return False

    def close_dropdown(self):
        try:
            self.page.keyboard.press("Escape")
            self.page.wait_for_timeout(500)
        except:
            pass

  
    def scroll_full_page(self):
        print(" Scrolling Stores page...")

        last_height = self.page.evaluate("document.body.scrollHeight")

        while True:
            self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            self.page.wait_for_timeout(1000)

            new_height = self.page.evaluate("document.body.scrollHeight")

            if new_height == last_height:
                break

            last_height = new_height

        print(" Scrolling back to top...")
        self.page.evaluate("window.scrollTo(0, 0)")
        self.page.wait_for_timeout(500)