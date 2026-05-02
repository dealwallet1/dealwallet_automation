from pages.base_page import BasePage


class DealsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.url = f"{self.base_url}/deals"

        self.CARD = "div[class*='rounded-3xl']"

        self.FILTER_BUTTONS = (
            "button:has-text('Store'), "
            "button:has-text('Category'), "
            "button:has-text('Price'), "
            "button:has-text('Discount'), "
            "button:has-text('Rating'), "
            "button:has-text('Sort')"
        )

        self.BUY_NOW_BTN = "button:has-text('Buy Now')"
        self.SHOP_NOW_BTN = "button:has-text('Shop Now')"

        self.SHARE_ICON = "button:has(svg.lucide-share2):visible"
        self.SHARE_POPUP = "h3:has-text('Share this deal'):visible"
        self.SHARE_CLOSE_BTN = "button[aria-label='Close']"

    def navigate(self):
        self.page.goto(self.url, timeout=60000, wait_until="domcontentloaded")
        self.handle_cookie_popup()
        self.wait_for_page_ready()

    def verify_page_loaded(self):
        return "deals" in self.page.url.lower()

    def get_deals_count(self):
        try:
            self.page.wait_for_selector(self.CARD, timeout=15000)
        except:
            print("Deals not loaded")
            return 0

        count = self.page.locator(self.CARD).count()
        print(f"Total deals: {count}")
        return count

    def get_all_filters(self):
        try:
            self.page.wait_for_selector(
                "button:has-text('Store'), button:has-text('Category')",
                timeout=10000
            )

            filters = self.page.locator(self.FILTER_BUTTONS)
            count = filters.count()

            names = []
            for i in range(count):
                txt = filters.nth(i).inner_text().strip()
                if txt:
                    names.append(txt)

            print(f"Filters: {names}")
            return filters, count

        except Exception as e:
            print(f"Filters not found: {e}")
            return self.page.locator("button"), 0

    def open_filter_by_index(self, index):
        filters = self.page.locator(self.FILTER_BUTTONS)

        try:
            btn = filters.nth(index)
            btn.scroll_into_view_if_needed()
            btn.click()
            return True
        except Exception as e:
            print(f"Filter open failed: {e}")
            return False

    def verify_dropdown_opened(self):
        try:
            dropdown = self.page.locator(
                "div[role='menu']:visible, div[role='listbox']:visible, div.absolute:visible"
            )
            return dropdown.count() > 0
        except:
            return False

    def verify_sort_dropdown_opened(self):
        return self.verify_dropdown_opened()

    def close_dropdown(self):
        try:
            self.page.keyboard.press("Escape")
            self.page.mouse.click(5, 5)
        except:
            pass

    def scroll_page_full(self):
        print("Scrolling page...")
        last_height = 0

        for _ in range(8):
            self.page.mouse.wheel(0, 3000)

            try:
                new_height = self.page.evaluate("document.body.scrollHeight")
            except:
                break

            if new_height == last_height:
                break

            last_height = new_height

        print("Scroll completed")

    def scroll_to_top(self):
        self.page.evaluate("window.scrollTo(0, 0)")

    def click_first_buy_now(self):
        try:
            self.page.wait_for_selector(self.BUY_NOW_BTN, timeout=15000)

            btn = self.page.locator(self.BUY_NOW_BTN).first
            btn.scroll_into_view_if_needed()

            print("Clicking Buy Now...")

            try:
                with self.page.context.expect_page(timeout=5000) as new_page_info:
                    btn.click()

                new_page = new_page_info.value
                new_page.wait_for_load_state()
                print(f"New tab opened: {new_page.url}")
                self.page = new_page
                return True

            except:
                with self.page.expect_navigation(timeout=15000):
                    btn.click()

                print(f"Redirected to: {self.page.url}")
                return True

        except Exception as e:
            print(f"Buy Now click failed: {e}")
            return False

    def verify_redirect_to_deal_page(self):
        try:
            url = self.page.url.lower()
            print(f"Deal Page URL: {url}")
            return "deal" in url or "details" in url
        except:
            return False

    def click_shop_now_on_deal_page(self):
        try:
            self.page.wait_for_selector(self.SHOP_NOW_BTN, timeout=15000)

            btn = self.page.locator(self.SHOP_NOW_BTN).first
            btn.scroll_into_view_if_needed()

            print("Clicking Shop Now...")

            existing_pages = self.page.context.pages
            btn.click()

            self.page.wait_for_timeout(3000)

            new_pages = self.page.context.pages

            if len(new_pages) > len(existing_pages):
                self.page = new_pages[-1]
                self.page.wait_for_load_state()
                print(f"New tab detected: {self.page.url}")
            else:
                self.page.wait_for_load_state()
                print(f"Same tab navigation: {self.page.url}")

            return True

        except Exception as e:
            print(f"Shop Now click failed: {e}")
            return False

    def verify_redirect_to_store_page(self):
        try:
            print("Validating external redirect...")

            self.page.wait_for_load_state("domcontentloaded")

            for _ in range(5):
                current_url = self.page.url.lower()
                print(f"Current URL: {current_url}")

                if "dealwallet.com" not in current_url:
                    print("External store reached ")
                    return True

                self.page.wait_for_timeout(3000)

            print("Still inside dealwallet domain ")
            print(f"Final URL: {self.page.url}")
            return False

        except Exception as e:
            print(f"Redirect validation error: {e}")
            return False

    def click_share_icon(self):
        try:
            btn = self.page.locator(self.SHARE_ICON).first
            btn.wait_for(state="visible", timeout=5000)
            btn.click()
            print("Clicked share icon")
            return True
        except Exception as e:
            print(f"Share click failed: {e}")
            return False

    def verify_share_popup_opened(self):
        try:
            popup = self.page.locator(self.SHARE_POPUP).first
            popup.wait_for(state="visible", timeout=5000)
            print("Share popup is visible")
            return True
        except Exception as e:
            print(f"Share popup not visible: {e}")
            return False

    def close_share_popup(self):
        try:
            btn = self.page.locator(self.SHARE_CLOSE_BTN).first
            if btn.is_visible():
                btn.click()
                print("Share popup closed")
        except:
            pass