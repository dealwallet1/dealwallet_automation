# from pages.base_page import BasePage


# class AboutPage(BasePage):
#     def __init__(self, page):
#         super().__init__(page)


#         self.ABOUT_LINK = "a[href='/aboutus']"

    
#         self.HEADINGS = "h1, h2, h3"
#         self.PARAGRAPHS = "p"

#         self.TAB_ABOUT = "button:has-text('About Us')"
#         self.TAB_CONTACT = "button:has-text('Contact Us')"
#         self.TAB_HELP = "button:has-text('Help & Support')"
#         self.TAB_COLLAB = "button:has-text('Collaborate With Us')"

#         self.ALL_TABS = [
#             self.TAB_ABOUT,
#             self.TAB_CONTACT,
#             self.TAB_HELP,
#             self.TAB_COLLAB
#         ]


#     def handle_overlays(self):
#         self.handle_cookie_popup()

#         try:
#             modal = self.page.locator(".cf_modal_container")

#             if modal.count() > 0:
#                 print("Blocking modal detected...")
#                 self.page.keyboard.press("Escape")
#                 self.page.wait_for_timeout(1000)

#         except Exception as e:
#             print(f"Overlay handling issue: {e}")


#     def click_about_us(self):
#         try:
#             self.handle_overlays()

#             about_link = self.page.locator(self.ABOUT_LINK).first

#             about_link.scroll_into_view_if_needed()
#             about_link.wait_for(state="visible", timeout=5000)

#             print("Clicking About Us...")

#             try:
#                 about_link.click(force=True)
#             except:
#                 print("Fallback JS click...")
#                 self.page.evaluate(
#                     "document.querySelector('a[href=\"/aboutus\"]').click()"
#                 )

#             self.page.wait_for_url("**/aboutus", timeout=15000)

#             print(f"Redirected to: {self.page.url}")
#             return True

#         except Exception as e:
#             print(f"About click failed: {e}")
#             return False


#     def verify_about_page(self):
#         try:
#             self.page.wait_for_selector(self.HEADINGS, timeout=10000)
#             return "/aboutus" in self.page.url
#         except:
#             return False


#     def scroll_about_page(self):
#         print("Scrolling page...")

#         for _ in range(5):
#             self.page.mouse.wheel(0, 2000)
#             self.page.wait_for_timeout(800)

#         print("Scroll complete")


#     def get_all_sections(self):
#         try:
#             headings = self.page.locator(self.HEADINGS)
#             sections = []

#             for i in range(headings.count()):
#                 text = headings.nth(i).inner_text().strip()
#                 if text:
#                     sections.append(text)

#             print(f"Sections found: {sections}")
#             return sections

#         except:
#             return []


#     def read_content(self):
#         try:
#             paragraphs = self.page.locator(self.PARAGRAPHS)

#             for i in range(min(paragraphs.count(), 10)):
#                 text = paragraphs.nth(i).inner_text().strip()
#                 print(f"[{i+1}] {text[:100]}")

#             return paragraphs.count() > 0

#         except:
#             return False


#     def click_and_validate_tabs(self):
#         results = []

#         for tab in self.ALL_TABS:
#             try:
#                 print(f"\nClicking tab: {tab}")

#                 tab_locator = self.page.locator(tab)

#                 tab_locator.scroll_into_view_if_needed()
#                 tab_locator.wait_for(state="visible", timeout=5000)

#                 tab_locator.click()
#                 self.page.wait_for_timeout(1500)

#                 has_content = self.page.locator(self.PARAGRAPHS).count() > 0
#                 print(f"Content present: {has_content}")

#                 self.scroll_about_page()

#                 self.read_content()

#                 results.append(has_content)

#             except Exception as e:
#                 print(f"Tab failed: {e}")
#                 results.append(False)

#         return all(results)













# from pages.base_page import BasePage


# class AboutPage(BasePage):

#     def __init__(self, page):
#         super().__init__(page)

#         # About Us navigation
#         self.ABOUT_LINK = "a[href='/about/us']"

#         # Page content selectors
#         self.HEADINGS = "h1, h2, h3"
#         self.PARAGRAPHS = "p"

#         # About Us tabs
#         self.TAB_ABOUT = "button:has-text('About Us')"
#         self.TAB_CONTACT = "button:has-text('Contact Us')"
#         self.TAB_HELP = "button:has-text('Help & Support')"
#         self.TAB_COLLAB = "button:has-text('Collaborate With Us')"

#         self.ALL_TABS = [
#             self.TAB_ABOUT,
#             self.TAB_CONTACT,
#             self.TAB_HELP,
#             self.TAB_COLLAB
#         ]

#     # Handle cookie popup and blocking overlays
#     def handle_overlays(self):
#         self.handle_cookie_popup()

#         try:
#             modal = self.page.locator(".cf_modal_container")

#             if modal.count() > 0 and modal.first.is_visible():
#                 print("Blocking modal detected...")
#                 self.page.keyboard.press("Escape")
#                 self.page.wait_for_timeout(1000)

#         except Exception as e:
#             print(f"Overlay handling issue: {e}")

#     # Navigate to About Us page
#     def click_about_us(self):
#         try:
#             self.handle_overlays()

#             print("Searching for About Us link...")

#             about_links = self.page.locator(self.ABOUT_LINK)

#             about_links.first.wait_for(
#                 state="visible",
#                 timeout=10000
#             )

#             about_link = None

#             for i in range(about_links.count()):
#                 link = about_links.nth(i)

#                 if link.is_visible():
#                     about_link = link
#                     break

#             if about_link is None:
#                 print("Visible About Us link not found.")
#                 return False

#             print("About Us link found.")
#             print("Link text:", about_link.inner_text())
#             print("Link URL:", about_link.get_attribute("href"))

#             about_link.scroll_into_view_if_needed()

#             print("Clicking About Us...")

#             about_link.click()

#             # Verify navigation
#             self.page.wait_for_url(
#                 "**/about/us",
#                 timeout=15000
#             )

#             print("Redirected to:", self.page.url)

#             # Wait for page content
#             self.page.locator(
#                 self.HEADINGS
#             ).first.wait_for(
#                 state="visible",
#                 timeout=10000
#             )

#             print("About Us page loaded successfully.")

#             return True

#         except Exception as e:
#             print(f"About click failed: {e}")
#             return False

#     # Verify About Us page
#     def verify_about_page(self):
#         try:
#             self.page.wait_for_url(
#                 "**/about/us",
#                 timeout=10000
#             )

#             self.page.locator(
#                 self.HEADINGS
#             ).first.wait_for(
#                 state="visible",
#                 timeout=10000
#             )

#             print("About Us page verification successful.")

#             return "/about/us" in self.page.url

#         except Exception as e:
#             print(f"About page verification failed: {e}")
#             return False

#     # Scroll down and up
#     def scroll_about_page(self):
#         print("Scrolling About Us page down...")

#         for i in range(5):
#             self.page.mouse.wheel(0, 1500)
#             self.page.wait_for_timeout(800)
#             print(f"Scroll down: {i + 1}")

#         print("Scrolling About Us page up...")

#         for i in range(5):
#             self.page.mouse.wheel(0, -1500)
#             self.page.wait_for_timeout(800)
#             print(f"Scroll up: {i + 1}")

#         print("Scrolling completed.")

#     # Get all page headings
#     def get_all_sections(self):
#         try:
#             headings = self.page.locator(self.HEADINGS)
#             sections = []

#             for i in range(headings.count()):
#                 text = headings.nth(i).inner_text().strip()

#                 if text:
#                     sections.append(text)

#             print(f"Sections found: {sections}")

#             return sections

#         except Exception as e:
#             print(f"Unable to get sections: {e}")
#             return []

#     # Read page paragraph content
#     def read_content(self):
#         try:
#             paragraphs = self.page.locator(self.PARAGRAPHS)
#             count = paragraphs.count()

#             for i in range(min(count, 10)):
#                 text = paragraphs.nth(i).inner_text().strip()

#                 if text:
#                     print(f"[{i + 1}] {text[:200]}")

#             return count > 0

#         except Exception as e:
#             print(f"Unable to read content: {e}")
#             return False

#     # Click and validate About Us tabs
#     def click_and_validate_tabs(self):
#         results = []

#         for tab in self.ALL_TABS:
#             try:
#                 print(f"\nClicking tab: {tab}")

#                 tab_locator = self.page.locator(tab).first

#                 tab_locator.scroll_into_view_if_needed()

#                 tab_locator.wait_for(
#                     state="visible",
#                     timeout=5000
#                 )

#                 tab_locator.click()

#                 self.page.wait_for_timeout(1500)

#                 has_content = (
#                     self.page.locator(
#                         self.PARAGRAPHS
#                     ).count() > 0
#                 )

#                 print(f"Content present: {has_content}")

#                 self.scroll_about_page()
#                 self.read_content()

#                 results.append(has_content)

#             except Exception as e:
#                 print(f"Tab failed: {e}")
#                 results.append(False)

#         return all(results)




import re
from pages.base_page import BasePage


class AboutPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.HEADINGS = "h1, h2, h3"
        self.PARAGRAPHS = "p"

        self.ALL_TABS = [
            "About Us",
            "Contact Us",
            "Help & Support",
            "Collaborate With Us"
        ]

    def handle_overlays(self):
        try:
            self.handle_cookie_popup()
        except Exception as e:
            print(f"Cookie popup handling: {e}")

        try:
            modal = self.page.locator(".cf_modal_container")

            if modal.count() > 0 and modal.first.is_visible():
                self.page.keyboard.press("Escape")
                self.page.wait_for_timeout(1000)

        except Exception as e:
            print(f"Overlay handling issue: {e}")

    def click_about_us(self):

        try:
            print("\nSearching for About Us link...")

            self.handle_overlays()

            # First check the complete page
            about_links = self.page.get_by_role(
                "link",
                name=re.compile(r"^\s*about\s+us\s*$", re.I)
            )

            # Scroll to footer if the link is not visible
            visible_link = None

            for i in range(about_links.count()):
                link = about_links.nth(i)

                if link.is_visible():
                    visible_link = link
                    break

            if visible_link is None:

                print("About Us not visible. Scrolling to footer...")

                self.page.evaluate(
                    "() => window.scrollTo(0, document.body.scrollHeight)"
                )

                self.page.wait_for_timeout(2000)

                for i in range(about_links.count()):
                    link = about_links.nth(i)

                    if link.is_visible():
                        visible_link = link
                        break

            # Print available About-related links for debugging
            print("\nAvailable About-related links:")

            all_links = self.page.locator("a")

            for i in range(all_links.count()):
                link = all_links.nth(i)

                try:
                    text = link.inner_text().strip()
                    href = link.get_attribute("href")

                    if "about" in text.lower() or (
                        href and "about" in href.lower()
                    ):
                        print(f"Text: {text} | URL: {href}")

                except Exception:
                    continue

            if visible_link is None:
                print("ERROR: No visible About Us link found.")
                return False

            print("\nAbout Us link found.")

            print("Link text:", visible_link.inner_text())
            print("Link URL:", visible_link.get_attribute("href"))

            visible_link.scroll_into_view_if_needed()

            visible_link.click(timeout=10000)

            self.page.wait_for_load_state(
                "domcontentloaded",
                timeout=15000
            )

            self.page.wait_for_timeout(2000)

            print("Current URL:", self.page.url)

            # Check whether About page content is displayed
            heading = self.page.locator(self.HEADINGS)

            if heading.count() > 0 and heading.first.is_visible():
                print("About page heading:", heading.first.inner_text())
                print("About page navigation successful.")
                return True

            # Some pages may not contain headings
            if "about" in self.page.url.lower():
                print("About page URL detected.")
                return True

            print("About page could not be verified.")
            return False

        except Exception as e:
            print(f"About click failed: {e}")
            return False

    def verify_about_page(self):

        try:
            self.page.wait_for_load_state(
                "domcontentloaded",
                timeout=10000
            )

            headings = self.page.locator(self.HEADINGS)

            if headings.count() == 0:
                print("No headings found.")
                return False

            print("Current URL:", self.page.url)
            print("Page heading:", headings.first.inner_text())

            return (
                "about" in self.page.url.lower()
                or headings.first.is_visible()
            )

        except Exception as e:
            print(f"About page verification failed: {e}")
            return False

    def scroll_about_page(self):

        print("Scrolling About page down...")

        for i in range(5):
            self.page.mouse.wheel(0, 1200)
            self.page.wait_for_timeout(500)

        print("Scrolling About page up...")

        for i in range(5):
            self.page.mouse.wheel(0, -1200)
            self.page.wait_for_timeout(500)

        print("Scrolling completed.")

    def get_all_sections(self):

        try:
            headings = self.page.locator(self.HEADINGS)

            sections = []

            for i in range(headings.count()):
                text = headings.nth(i).inner_text().strip()

                if text:
                    sections.append(text)

            print("Sections found:", sections)

            return sections

        except Exception as e:
            print(f"Unable to get sections: {e}")
            return []

    def read_content(self):

        try:
            paragraphs = self.page.locator(self.PARAGRAPHS)

            count = paragraphs.count()

            print(f"Total paragraphs: {count}")

            for i in range(min(count, 10)):

                text = paragraphs.nth(i).inner_text().strip()

                if text:
                    print(f"[{i + 1}] {text[:200]}")

            return count > 0

        except Exception as e:
            print(f"Unable to read content: {e}")
            return False

    def click_and_validate_tabs(self):

        results = []

        for tab in self.ALL_TABS:

            try:
                print(f"\nChecking tab: {tab}")

                tab_locator = self.page.get_by_role(
                    "button",
                    name=re.compile(
                        re.escape(tab),
                        re.I
                    )
                )

                if tab_locator.count() == 0:
                    print(f"Tab not found: {tab}")
                    results.append(False)
                    continue

                tab_locator.first.scroll_into_view_if_needed()
                tab_locator.first.click(timeout=5000)

                self.page.wait_for_timeout(1000)

                has_content = self.page.locator(
                    self.PARAGRAPHS
                ).count() > 0

                print(f"Content present: {has_content}")

                results.append(has_content)

            except Exception as e:
                print(f"Tab failed ({tab}): {e}")
                results.append(False)

        return all(results)
