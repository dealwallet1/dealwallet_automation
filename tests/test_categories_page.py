import pytest
from pages.categories_page import CategoriesPage
from playwright.sync_api import Page


@pytest.mark.categories
class TestCategoriesPage:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.categories = CategoriesPage(page)
        self.categories.navigate()

    def test_page_load(self):
        assert self.categories.verify_page_loaded()

    def test_category_cards_present(self):
        count = self.categories.get_category_count()
        assert count > 0, f"No categories found, count={count}"

    def test_category_full_flow(self):
       
        self.categories.scroll_to_footer()

      
        assert self.categories.click_first_category(), \
            "Category click failed"

      
        self.categories.page.wait_for_load_state("domcontentloaded")

      
        assert self.categories.verify_category_landing_page(), \
            "Category landing page not opened"

        
        category_name = self.categories.get_category_name()
        assert category_name is not None and category_name != "", \
            "Category name not loaded"

        # Step 6: Tabs interaction
        assert self.categories.click_all_tabs(), \
            "Tabs interaction failed"   