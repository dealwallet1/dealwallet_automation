# from pages.base_page import BasePage

# class HomePage(BasePage):
#     def __init__(self, page):
#         super().__init__(page)

#         self.url = f"{self.base_url}/"

        
#         self.LOGO = "header a"

#         self.SEARCH_INPUT = "input[type='search'], input[placeholder*='Search']"

#         self.BANNER = "h1, h2"

#         self.FEATURE_CARD = "a[href*='deal']"

#         self.FOOTER = "footer"

#         self.SOCIAL_LINKS = [
#             "a[href*='facebook']",
#             "a[href*='twitter']",
#             "a[href*='instagram']"
#         ]

#         self.SIGNIN_BUTTON = "a[href*='signin']"

#     def navigate(self):
        
#         self.page.goto(
#             self.url,
#             timeout=60000,
#             wait_until="domcontentloaded"
#         )
#         self.handle_cookie_popup()
#         self.wait_for_page_ready()

#     # ❗ FIX 5: Strong banner validation
#     def verify_banner_visible(self):
#         try:
#             self.page.wait_for_selector(self.BANNER, timeout=5000)
#             return self.page.locator(self.BANNER).count() > 0
#         except:
#             return False

#     def get_feature_card_count(self):
#         self.handle_cookie_popup()
#         return self.page.locator(self.FEATURE_CARD).count()

#     def verify_footer_visible(self):
#         return self.is_visible(self.FOOTER)

#     def verify_social_links(self):
#         found = []
#         for sel in self.SOCIAL_LINKS:
#             if self.is_visible(sel):
#                 found.append(sel)
#         return found

#     def click_logo(self):
#         self.page.wait_for_selector(self.LOGO)
#         self.safe_click(self.LOGO)

#     def click_signin(self):
#         self.safe_click(self.SIGNIN_BUTTON)

#     def perform_search(self, query):
#         self.handle_cookie_popup()

#         locator = self.page.locator(self.SEARCH_INPUT)

#         if locator.count() == 0:
#             print(" Search input not found")
#             return False

#         locator.first.fill(query)
#         self.page.keyboard.press("Enter")

#         self.page.wait_for_timeout(2000)

#         return True




from pages.base_page import BasePage
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError


class HomePage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.url = f"{self.base_url}/"

        # Homepage locators
        self.LOGO = "header a"

        self.SEARCH_INPUT = (
            "input[type='search'], input[placeholder*='Search']"
        )

        self.BANNER = "h1, h2"

        self.FEATURE_CARD = "a[href*='deal']"

        self.FOOTER = "footer"

        self.SIGNIN_BUTTON = "a[href*='signin']"

        # Social media domains
        self.SOCIAL_MEDIA = {
            "Facebook": "facebook.com",
            "Instagram": "instagram.com",
            "Threads": "threads.com",
            "Slack": "slack.com",
            "Telegram": "t.me",
            "YouTube": "youtube.com"
        }

        # Platform-specific content selectors
        self.SOCIAL_CONTENT_SELECTORS = {

            "Facebook": [
                '[role="main"]',
                'div[data-pagelet="ProfileTilesFeed"]',
                'div[data-pagelet="ProfileActions"]',
                'h1'
            ],

            "Instagram": [
                'main',
                'article',
                'header'
            ],

            "Threads": [
                'main',
                '[role="main"]',
                'article'
            ],

            "Slack": [
                '[role="main"]',
                'main',
                '[data-qa="workspace_name"]'
            ],

            "Telegram": [
                '.tgme_page',
                '.tgme_page_title',
                'main'
            ],

            "YouTube": [
                '#channel-header-container',
                'ytd-channel-name',
                'ytd-rich-grid-renderer',
                'ytd-video-renderer',
                '#primary'
            ]
        }

    # Navigate to homepage
    def navigate(self):

        self.page.goto(
            self.url,
            timeout=60000,
            wait_until="domcontentloaded"
        )

        self.handle_cookie_popup()
        self.wait_for_page_ready()

    # Homepage banner
    def verify_banner_visible(self):

        try:

            self.page.locator(
                self.BANNER
            ).first.wait_for(
                state="visible",
                timeout=10000
            )

            return True

        except PlaywrightTimeoutError:
            return False

    # Logo validation
    def click_logo(self):

        try:

            logo = self.page.locator(
                self.LOGO
            ).first

            logo.wait_for(
                state="visible",
                timeout=10000
            )

            logo.click(timeout=10000)

            return True

        except PlaywrightTimeoutError:
            return False

    # Sign In
    def click_signin(self):

        try:

            button = self.page.locator(
                self.SIGNIN_BUTTON
            ).first

            button.wait_for(
                state="visible",
                timeout=10000
            )

            button.click(timeout=10000)

            self.page.wait_for_timeout(2000)

            print("Sign In current URL:", self.page.url)

            return True

        except PlaywrightTimeoutError:
            return False

    # Feature cards
    def get_feature_card_count(self):

        self.handle_cookie_popup()

        return self.page.locator(
            self.FEATURE_CARD
        ).count()

    # Footer
    def verify_footer_visible(self):

        return self.is_visible(
            self.FOOTER
        )

    # Search
    def perform_search(self, query):

        self.handle_cookie_popup()

        locator = self.page.locator(
            self.SEARCH_INPUT
        ).first

        if locator.count() == 0:

            print("Search input not found")

            return False

        locator.fill(query)

        self.page.keyboard.press("Enter")

        self.page.wait_for_timeout(2000)

        return True

    # Scroll homepage
    def scroll_top_to_bottom(self):

        self.page.evaluate(
            """
            window.scrollTo({
                top: document.body.scrollHeight,
                behavior: 'instant'
            })
            """
        )

        self.page.wait_for_timeout(2000)

        print("Homepage scrolled from top to bottom")

    # Get all social media links
    def get_social_media_links(self):

        social_links = {}

        self.scroll_top_to_bottom()

        for name, domain in self.SOCIAL_MEDIA.items():

            locator = self.page.locator(
                f'footer a[href*="{domain}"]'
            ).first

            if locator.count() == 0:

                locator = self.page.locator(
                    f'a[href*="{domain}"]'
                ).first

            if locator.count() == 0:

                social_links[name] = {
                    "visible": False,
                    "href": None
                }

                continue

            social_links[name] = {
                "visible": locator.is_visible(),
                "href": locator.get_attribute("href")
            }

        return social_links

    # Verify destination page content
    def verify_social_page_content(
        self,
        social_page,
        social_name
    ):

        try:

            print(
                f"\nValidating {social_name} content..."
            )

            # Wait for initial page loading
            try:

                social_page.wait_for_load_state(
                    "domcontentloaded",
                    timeout=20000
                )

            except PlaywrightTimeoutError:

                print(
                    "DOM loading timeout. "
                    "Continuing content validation..."
                )

            print(
                "Social Media Page Title:",
                social_page.title()
            )

            print(
                "Social Media URL:",
                social_page.url
            )

            # Get platform-specific selectors
            selectors = self.SOCIAL_CONTENT_SELECTORS.get(
                social_name,
                []
            )

            # Check meaningful visible content
            for selector in selectors:

                try:

                    element = social_page.locator(
                        selector
                    ).first

                    element.wait_for(
                        state="visible",
                        timeout=5000
                    )

                    content = element.inner_text(
                        timeout=3000
                    ).strip()

                    if content:

                        print(
                            f"{social_name} content found "
                            f"using selector: {selector}"
                        )

                        print(
                            "Content preview:",
                            content[:200]
                        )

                        return True

                except Exception:
                    continue

            print(
                f"{social_name}: No meaningful "
                "visible content detected."
            )

            return False

        except Exception as error:

            print(
                f"{social_name} validation error:",
                error
            )

            return False
