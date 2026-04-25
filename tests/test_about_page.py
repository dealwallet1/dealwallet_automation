import pytest
from pages.about_page import AboutPage
from playwright.sync_api import Page


@pytest.mark.about
class TestAboutPage:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.about = AboutPage(page)
        self.about.page.goto(self.about.base_url)

    def test_about_full_flow(self):

        assert self.about.click_about_us(), "Failed to click About Us"

        assert self.about.verify_about_page(), "About page not loaded"

        self.about.scroll_about_page()

        sections = self.about.get_all_sections()
        assert len(sections) > 0, "No sections found"

        assert self.about.read_content(), "No content found"

        assert self.about.click_and_validate_tabs(), "Tab validation failed"