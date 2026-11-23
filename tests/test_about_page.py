# import pytest
# from pages.about_page import AboutPage
# from playwright.sync_api import Page


# @pytest.mark.about
# class TestAboutPage:

#     @pytest.fixture(autouse=True)
#     def setup(self, page: Page):
#         self.about = AboutPage(page)
#         self.about.page.goto(self.about.base_url)

#     def test_about_full_flow(self):

#         assert self.about.click_about_us(), "Failed to click About Us"

#         assert self.about.verify_about_page(), "About page not loaded"

#         self.about.scroll_about_page()

#         sections = self.about.get_all_sections()
#         assert len(sections) > 0, "No sections found"

#         assert self.about.read_content(), "No content found"

#         assert self.about.click_and_validate_tabs(), "Tab validation failed"

















# import pytest
# from pages.about_page import AboutPage
# from playwright.sync_api import Page


# @pytest.mark.about
# class TestAboutPage:

#     @pytest.fixture(autouse=True)
#     def setup(self, page: Page):
#         self.about = AboutPage(page)

#         self.about.page.goto(
#             self.about.base_url,
#             wait_until="domcontentloaded"
#         )

#     def test_about_full_flow(self):

#         # Step 1: Navigate to About Us
#         assert self.about.click_about_us(), \
#             "Failed to click About Us"

#         # Step 2: Verify About Us page
#         assert self.about.verify_about_page(), \
#             "About page not loaded"

#         # Step 3: Scroll down and up
#         self.about.scroll_about_page()

#         # Step 4: Get page headings
#         sections = self.about.get_all_sections()

#         assert len(sections) > 0, \
#             "No sections found"

#         # Step 5: Read page content
#         assert self.about.read_content(), \
#             "No content found"

#         # Step 6: Validate tabs
#         assert self.about.click_and_validate_tabs(), \
#             "Tab validation failed"







import pytest
from playwright.sync_api import Page
from pages.about_page import AboutPage


@pytest.mark.about
class TestAboutPage:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):

        self.about = AboutPage(page)

        print("\nOpening DealWallet homepage...")

        self.about.page.goto(
            self.about.base_url,
            wait_until="domcontentloaded",
            timeout=30000
        )

        self.about.page.wait_for_timeout(2000)

    def test_about_full_flow(self):

        # Step 1: Navigate to About Us
        assert self.about.click_about_us(), (
            "Failed to navigate to About Us page"
        )

        # Step 2: Verify About page
        assert self.about.verify_about_page(), (
            "About page verification failed"
        )

        # Step 3: Scroll page
        self.about.scroll_about_page()

        # Step 4: Get headings
        sections = self.about.get_all_sections()

        assert len(sections) > 0, (
            "No headings found on About page"
        )

        # Step 5: Read content
        assert self.about.read_content(), (
            "No paragraph content found"
        )

        # Step 6: Validate tabs
        assert self.about.click_and_validate_tabs(), (
            "One or more About page tabs failed"
        )
