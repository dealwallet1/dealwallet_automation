import pytest
from pages.home_page import HomePage
from playwright.sync_api import Page

@pytest.mark.home
class TestHomePage:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.home = HomePage(page)
        self.home.navigate()

   
    def test_homepage_loads_successfully(self):
       
        assert "dealwallet.com" in self.home.page.url

   
    def test_logo_clickable(self):
        
        self.home.page.wait_for_selector(self.home.LOGO)

       
        assert self.home.is_visible(self.home.LOGO)

        self.home.safe_click(self.home.LOGO)

        
        assert "dealwallet.com" in self.home.page.url

   
    def test_signin_button_functional(self):
        if not self.home.is_visible(self.home.SIGNIN_BUTTON):
            pytest.skip("Sign In button not visible")

        self.home.safe_click(self.home.SIGNIN_BUTTON)

        assert "signin" in self.home.page.url.lower()


    def test_banner_section_visible(self):
        assert self.home.verify_banner_visible()

  
    def test_feature_cards_present(self):
        count = self.home.get_feature_card_count()

        assert count > 0, f"No feature cards found, count={count}"

 
    def test_search_field_present(self):
      
        self.home.page.wait_for_selector(self.home.SEARCH_INPUT)

        assert self.home.is_visible(self.home.SEARCH_INPUT)


    def test_search_functionality(self):
        ok = self.home.perform_search("shoes")
        assert ok

       
        self.home.page.wait_for_selector("a[href*='/deal']")

        results = self.home.page.locator("a[href*='/deal']").count()
        assert results > 0, "No search results displayed"

  
    def test_footer_visible(self):
        self.home.page.mouse.wheel(0, 5000)

       
        self.home.page.wait_for_selector("footer")

        assert self.home.verify_footer_visible()

 
    def test_social_media_links(self):
        self.home.page.mouse.wheel(0, 5000)

        links = self.home.verify_social_links()
        assert len(links) > 0