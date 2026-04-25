from pages.base_page import BasePage


class AboutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)


        self.ABOUT_LINK = "a[href='/aboutus']"

    
        self.HEADINGS = "h1, h2, h3"
        self.PARAGRAPHS = "p"

        self.TAB_ABOUT = "button:has-text('About Us')"
        self.TAB_CONTACT = "button:has-text('Contact Us')"
        self.TAB_HELP = "button:has-text('Help & Support')"
        self.TAB_COLLAB = "button:has-text('Collaborate With Us')"

        self.ALL_TABS = [
            self.TAB_ABOUT,
            self.TAB_CONTACT,
            self.TAB_HELP,
            self.TAB_COLLAB
        ]


    def handle_overlays(self):
        self.handle_cookie_popup()

        try:
            modal = self.page.locator(".cf_modal_container")

            if modal.count() > 0:
                print("Blocking modal detected...")
                self.page.keyboard.press("Escape")
                self.page.wait_for_timeout(1000)

        except Exception as e:
            print(f"Overlay handling issue: {e}")


    def click_about_us(self):
        try:
            self.handle_overlays()

            about_link = self.page.locator(self.ABOUT_LINK).first

            about_link.scroll_into_view_if_needed()
            about_link.wait_for(state="visible", timeout=5000)

            print("Clicking About Us...")

            try:
                about_link.click(force=True)
            except:
                print("Fallback JS click...")
                self.page.evaluate(
                    "document.querySelector('a[href=\"/aboutus\"]').click()"
                )

            self.page.wait_for_url("**/aboutus", timeout=15000)

            print(f"Redirected to: {self.page.url}")
            return True

        except Exception as e:
            print(f"About click failed: {e}")
            return False


    def verify_about_page(self):
        try:
            self.page.wait_for_selector(self.HEADINGS, timeout=10000)
            return "/aboutus" in self.page.url
        except:
            return False


    def scroll_about_page(self):
        print("Scrolling page...")

        for _ in range(5):
            self.page.mouse.wheel(0, 2000)
            self.page.wait_for_timeout(800)

        print("Scroll complete")


    def get_all_sections(self):
        try:
            headings = self.page.locator(self.HEADINGS)
            sections = []

            for i in range(headings.count()):
                text = headings.nth(i).inner_text().strip()
                if text:
                    sections.append(text)

            print(f"Sections found: {sections}")
            return sections

        except:
            return []


    def read_content(self):
        try:
            paragraphs = self.page.locator(self.PARAGRAPHS)

            for i in range(min(paragraphs.count(), 10)):
                text = paragraphs.nth(i).inner_text().strip()
                print(f"[{i+1}] {text[:100]}")

            return paragraphs.count() > 0

        except:
            return False


    def click_and_validate_tabs(self):
        results = []

        for tab in self.ALL_TABS:
            try:
                print(f"\nClicking tab: {tab}")

                tab_locator = self.page.locator(tab)

                tab_locator.scroll_into_view_if_needed()
                tab_locator.wait_for(state="visible", timeout=5000)

                tab_locator.click()
                self.page.wait_for_timeout(1500)

                has_content = self.page.locator(self.PARAGRAPHS).count() > 0
                print(f"Content present: {has_content}")

                self.scroll_about_page()

                self.read_content()

                results.append(has_content)

            except Exception as e:
                print(f"Tab failed: {e}")
                results.append(False)

        return all(results)