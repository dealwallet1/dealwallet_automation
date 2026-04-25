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
        assert count > 0, f"No stores found, count={count}"


    def test_filters_functionality(self):

        filters, count = self.stores.get_all_filters()
        assert count > 0, "No filters found on Stores page"

        for i in range(count):
            filter_text = filters.nth(i).inner_text().strip()
            print(f"Testing filter: {filter_text}")

            assert self.stores.open_filter_by_index(i), \
                f"Failed to open filter {filter_text}"

            if "Sort" in filter_text:
                assert self.stores.verify_sort_dropdown_opened(), \
                    "Sort dropdown not visible"
            else:
                assert self.stores.verify_dropdown_opened(), \
                    f"Dropdown not visible for {filter_text}"

            print(f"Dropdown opened for: {filter_text}")

        
            self.stores.close_dropdown()

        
        self.stores.scroll_full_page()

    
        assert self.stores.click_first_store(), \
            "Store click failed"

        
        self.stores.page.wait_for_load_state("domcontentloaded")
        self.stores.page.wait_for_timeout(1500)

        assert self.stores.verify_store_landing_page(), \
            "Store landing page not opened"

        store_name = self.stores.get_store_name()
        assert store_name is not None and store_name != "", \
            "Store name not loaded"

        assert self.stores.click_store_tabs(), \
            "Store tabs interaction failed"