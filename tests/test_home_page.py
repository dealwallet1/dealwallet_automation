import pytest
from pages.home_page import HomePage
from playwright.sync_api import Page, TimeoutError


@pytest.mark.home
class TestHomePage:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.home = HomePage(page)
        self.home.navigate()
        self.home.handle_cookie_popup()
        self.home.wait_for_overlays_to_disappear()

  
    def test_homepage_loads_successfully(self):
        assert self.home.verify_home_loaded(), "Home page did not load"

    def test_logo_clickable(self):
        assert self.home.is_visible(self.home.LOGO, timeout=5000), "Logo not visible"
        self.home.safe_click(self.home.LOGO)
        assert "dealwallet" in self.home.page.url.lower(), "Logo click failed"

    def test_signin_button_functional(self):
        # If user logged in → skip
        if self.home.is_visible(self.home.PROFILE_AVATAR):
            pytest.skip("User already logged in — Sign In not shown")

        if not self.home.is_visible(self.home.SIGNIN_BUTTON):
            pytest.skip("Sign In button not visible")

        self.home.safe_click(self.home.SIGNIN_BUTTON)
        assert any(k in self.home.page.url.lower() for k in ["signin", "login"]), \
            "Sign-in did not navigate"

    def test_banner_section_visible(self):
        assert self.home.verify_banner_visible(), "Hero banner not visible"

    def test_feature_cards_present(self):
        count = self.home.get_feature_card_count()
        assert count >= 4, f"Expected at least 4 feature cards, found {count}"

   
    def test_search_field_present(self):
        visible = self.home.is_visible(self.home.SEARCH_INPUT, timeout=7000)
        assert visible, "Search bar not visible on homepage"

    def test_search_functionality(self):
        if not self.home.is_visible(self.home.SEARCH_INPUT, timeout=7000):
            pytest.skip("Search input not available")

        ok = self.home.perform_search("shoes")
        assert ok, "Search could not be performed"

        assert any(k in self.home.page.url.lower() for k in ["search", "product", "products"]), \
            "Search results page not detected after search"


    def test_footer_visible(self):
        self.home.scroll_to_bottom()
        assert self.home.verify_footer_visible(), "Footer is not visible"

    def test_social_media_links(self):
        self.home.scroll_to_bottom()
        links = self.home.verify_social_links()
        assert len(links) > 0, "Footer social icons missing"

    def test_performance_load_time(self):
        import time
        start = time.time()
        self.home.navigate()
        load_time = round(time.time() - start, 2)
        assert load_time < 12, f"Homepage load slow: {load_time}s"
