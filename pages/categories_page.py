from pages.base_page import BasePage


class CategoriesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.url = f"{self.base_url}/categories"

        self.CARD = "a[href*='category'], a[href*='categories']"

        self.CATEGORY_UI_CARD = "div.group.relative.cursor-pointer"

        self.TABS_CONTAINER = "div.flex.rounded-full.border"
        self.TABS = f"{self.TABS_CONTAINER} button"

        self.CATEGORY_NAME = "h1.text-xl.font-bold.text-black"

    def navigate(self):
        self.page.goto(
            self.url,
            timeout=60000,
            wait_until="domcontentloaded"
        )
        self.handle_cookie_popup()
        self.wait_for_page_ready()

    def verify_page_loaded(self):
        return "categories" in self.page.url.lower()

    def get_category_count(self):
        self.handle_cookie_popup()

        try:
            self.page.wait_for_selector(self.CARD, timeout=10000)
        except:
            print("Category cards not found, returning 0")
            return 0

        count = self.page.locator(self.CARD).count()
        print(f"Total categories: {count}")
        return count

    def scroll_to_footer(self):
        print("Scrolling categories page...")

        last_height = 0

        for _ in range(10):
            self.page.mouse.wheel(0, 3000)
            self.page.wait_for_timeout(800)

            try:
                new_height = self.page.evaluate("document.body.scrollHeight")
            except:
                break

            if new_height == last_height:
                break

            last_height = new_height

        print("Reached footer")

    def click_first_category(self):
        try:
            self.page.wait_for_selector(self.CATEGORY_UI_CARD, timeout=10000)

            card = self.page.locator(self.CATEGORY_UI_CARD).first
            card.scroll_into_view_if_needed()

            print("Clicking first category...")

            with self.page.expect_navigation(timeout=15000):
                card.click()

            print(f"Redirected to: {self.page.url}")
            return True

        except Exception as e:
            print(f"Category click failed: {e}")
            return False

    def verify_category_landing_page(self):
        try:
            url = self.page.url.lower()
            print(f"Category URL: {url}")

            return any(x in url for x in ["category", "categories"])

        except:
            return False

    def get_category_name(self):
        try:
            heading = self.page.locator(self.CATEGORY_NAME).first
            heading.wait_for(state="visible", timeout=5000)

            name = heading.inner_text().strip()
            print(f"Category Name: {name}")

            return name

        except Exception as e:
            print(f"Failed to get category name: {e}")
            return None

    def click_all_tabs(self):
        try:
            
            self.page.wait_for_selector(self.TABS_CONTAINER, timeout=10000)

            tabs = self.page.locator(self.TABS)
            count = tabs.count()

            print(f"Tabs found: {count}")

            if count == 0:
                return False

            for i in range(count):
                
                tab = self.page.locator(self.TABS).nth(i)

                tab.wait_for(state="visible", timeout=5000)

                tab_text = tab.inner_text().strip()
                print(f"Clicking tab: {tab_text}")

                tab.click()

                self.page.wait_for_timeout(1000)

            return True

        except Exception as e:
            print(f"Tabs interaction failed: {e}")
            return False