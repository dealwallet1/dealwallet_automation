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
        assert count >= 1, f"No categories found, count={count}"

    def test_search_category(self):
        ok = self.categories.search_category("Electronics")
        assert ok
