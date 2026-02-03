import pytest
from pages.stores_page import StoresPage
from playwright.sync_api import Page

@pytest.mark.stores
class TestStoresPage:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.stores = StoresPage(page)
        self.stores.navigate()

    def test_page_load(self):
        assert self.stores.verify_page_loaded()

    def test_store_cards_present(self):
        count = self.stores.get_store_count()
        assert count >= 1, f"No stores found, count={count}"

    def test_store_search(self):
        ok = self.stores.search_store("Amazon")
        assert ok
