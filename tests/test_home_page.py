# import pytest
# from pages.home_page import HomePage
# from playwright.sync_api import Page

# @pytest.mark.home
# class TestHomePage:

#     @pytest.fixture(autouse=True)
#     def setup(self, page: Page):
#         self.home = HomePage(page)
#         self.home.navigate()

   
#     def test_homepage_loads_successfully(self):
       
#         assert "dealwallet.com" in self.home.page.url

   
#     def test_logo_clickable(self):
        
#         self.home.page.wait_for_selector(self.home.LOGO)

       
#         assert self.home.is_visible(self.home.LOGO)

#         self.home.safe_click(self.home.LOGO)

        
#         assert "dealwallet.com" in self.home.page.url

   
#     def test_signin_button_functional(self):
#         if not self.home.is_visible(self.home.SIGNIN_BUTTON):
#             pytest.skip("Sign In button not visible")

#         self.home.safe_click(self.home.SIGNIN_BUTTON)

#         assert "signin" in self.home.page.url.lower()


#     def test_banner_section_visible(self):
#         assert self.home.verify_banner_visible()

  
#     def test_feature_cards_present(self):
#         count = self.home.get_feature_card_count()

#         assert count > 0, f"No feature cards found, count={count}"

 
#     def test_search_field_present(self):
      
#         self.home.page.wait_for_selector(self.home.SEARCH_INPUT)

#         assert self.home.is_visible(self.home.SEARCH_INPUT)


#     def test_search_functionality(self):
#         ok = self.home.perform_search("shoes")
#         assert ok

       
#         self.home.page.wait_for_selector("a[href*='/deal']")

#         results = self.home.page.locator("a[href*='/deal']").count()
#         assert results > 0, "No search results displayed"

  
#     def test_footer_visible(self):
#         self.home.page.mouse.wheel(0, 5000)

       
#         self.home.page.wait_for_selector("footer")

#         assert self.home.verify_footer_visible()

 
#     def test_social_media_links(self):
#         self.home.page.mouse.wheel(0, 5000)

#         links = self.home.verify_social_links()
#         assert len(links) > 0



import pytest

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from pages.home_page import HomePage


class TestHomePage:

    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.home = HomePage(page)
        self.page = page

        self.home.navigate()

    # --------------------------------------------------
    # 1. Verify homepage loads successfully
    # --------------------------------------------------
    def test_homepage_load(self):

        assert self.page.url.startswith(
            self.home.base_url
        ), "Homepage did not load successfully"

        assert self.page.locator("body").count() > 0

        print("Homepage loaded successfully")

    # --------------------------------------------------
    # 2. Verify logo visibility
    # --------------------------------------------------
    def test_logo_visible(self):

        logo = self.page.locator(
            self.home.LOGO
        ).first

        assert logo.is_visible(), (
            "Homepage logo is not visible"
        )

        print("Homepage logo is visible")

    # --------------------------------------------------
    # 3. Verify logo click functionality
    # --------------------------------------------------
    def test_logo_click(self):

        result = self.home.click_logo()

        assert result, "Logo click failed"

        print("Logo click functionality verified")

    # --------------------------------------------------
    # 4. Verify Sign In button visibility
    # --------------------------------------------------
    def test_signin_visible(self):

        signin = self.page.locator(
            self.home.SIGNIN_BUTTON
        ).first

        assert signin.is_visible(), (
            "Sign In button is not visible"
        )

        print("Sign In button is visible")

    # --------------------------------------------------
    # 5. Verify Sign In functionality
    # --------------------------------------------------
    def test_signin_functionality(self):

        result = self.home.click_signin()

        assert result, "Sign In button click failed"

        print(
            "Sign In button clicked successfully"
        )

    # --------------------------------------------------
    # 6. Verify homepage banner
    # --------------------------------------------------
    def test_banner_visible(self):

        assert self.home.verify_banner_visible(), (
            "Homepage banner is not visible"
        )

        print("Homepage banner is visible")

    # --------------------------------------------------
    # 7. Verify feature cards
    # --------------------------------------------------
    def test_feature_cards_visible(self):

        count = self.home.get_feature_card_count()

        assert count > 0, (
            "No feature cards found on homepage"
        )

        print(
            f"Feature cards found: {count}"
        )

    # --------------------------------------------------
    # 8. Verify search field visibility
    # --------------------------------------------------
    def test_search_field_visible(self):

        search = self.page.locator(
            self.home.SEARCH_INPUT
        ).first

        assert search.is_visible(), (
            "Search field is not visible"
        )

        print("Search field is visible")

    # --------------------------------------------------
    # 9. Verify search functionality
    # --------------------------------------------------
    def test_search_functionality(self):

        result = self.home.perform_search(
            "mobile"
        )

        assert result, (
            "Search functionality failed"
        )

        print("Search query submitted successfully")

    # --------------------------------------------------
    # 10. Verify homepage scrolling
    # --------------------------------------------------
    def test_homepage_scroll(self):

        self.home.scroll_top_to_bottom()

        scroll_position = self.page.evaluate(
            "window.scrollY"
        )

        assert scroll_position > 0, (
            "Homepage scrolling failed"
        )

        print(
            "Homepage scrolling verified"
        )

    # --------------------------------------------------
    # 11. Verify footer visibility
    # --------------------------------------------------
    def test_footer_visible(self):

        self.home.scroll_top_to_bottom()

        assert self.home.verify_footer_visible(), (
            "Homepage footer is not visible"
        )

        print("Homepage footer is visible")

    # --------------------------------------------------
    # 12-17. Verify social media links and redirects
    # --------------------------------------------------
    @pytest.mark.parametrize(
        "social_name, expected_domain",
        [
            ("Facebook", "facebook.com"),
            ("Instagram", "instagram.com"),
            ("Threads", "threads.com"),
            ("Slack", "slack.com"),
            ("Telegram", "t.me"),
            ("YouTube", "youtube.com")
        ]
    )
    def test_social_media_redirect(
        self,
        social_name,
        expected_domain
    ):

        # Scroll to footer
        self.home.scroll_top_to_bottom()

        # Get social media links
        social_links = (
            self.home.get_social_media_links()
        )

        assert social_name in social_links, (
            f"{social_name} link was not found"
        )

        social = social_links[social_name]

        # Verify icon visibility
        assert social["visible"], (
            f"{social_name} icon is not visible"
        )

        # Verify URL availability
        assert social["href"], (
            f"{social_name} URL is missing"
        )

        # Verify expected domain
        assert expected_domain in social["href"].lower(), (
            f"Incorrect {social_name} URL: "
            f"{social['href']}"
        )

        original_page = self.page

        # Locate social media link
        locator = original_page.locator(
            f'footer a[href*="{expected_domain}"]'
        ).first

        if locator.count() == 0:

            locator = original_page.locator(
                f'a[href*="{expected_domain}"]'
            ).first

        assert locator.count() > 0, (
            f"{social_name} clickable link not found"
        )

        assert locator.is_visible(), (
            f"{social_name} link is not visible"
        )

        social_page = None

        try:

            # Handle popup or new tab
            with original_page.expect_popup(
                timeout=5000
            ) as popup_info:

                locator.click()

            social_page = popup_info.value

        except PlaywrightTimeoutError:

            # Handle same-tab navigation
            try:

                original_page.wait_for_url(
                    lambda url: expected_domain in str(url).lower(),
                    timeout=15000
                )

                social_page = original_page

            except PlaywrightTimeoutError:

                pytest.fail(
                    f"{social_name} click did not open "
                    "a new tab or navigate to destination"
                )

        try:

            # Wait for destination page
            try:

                social_page.wait_for_load_state(
                    "domcontentloaded",
                    timeout=30000
                )

            except PlaywrightTimeoutError:

                print(
                    f"{social_name} DOM loading timeout"
                )

            # Verify destination URL
            assert expected_domain in social_page.url.lower(), (
                f"{social_name} redirected incorrectly: "
                f"{social_page.url}"
            )

            print(
                f"\n{social_name} opened successfully: "
                f"{social_page.url}"
            )

            # Verify destination content
            content_visible = (
                self.home.verify_social_page_content(
                    social_page,
                    social_name
                )
            )

            assert content_visible, (
                f"{social_name} page content is not visible"
            )

            print(
                f"{social_name} redirect and content "
                "validation passed"
            )

        finally:

            # Close popup without closing original homepage
            if (
                social_page is not None
                and social_page != original_page
            ):

                try:
                    social_page.close()
                except Exception:
                    pass

            # Return to homepage after same-tab navigation
            elif social_page == original_page:

                self.home.navigate()

