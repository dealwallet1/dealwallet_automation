import pytest
from pages.stores_page import StoresPage
from playwright.sync_api import Page


@pytest.mark.stores
class TestStoresPage:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.stores = StoresPage(page)
        self.stores.navigate()

    # ------------------------------
    # PAGE LOAD
    # ------------------------------
    def test_page_load(self):
        assert self.stores.verify_page_loaded()

    # ------------------------------
    # STORE CARDS
    # ------------------------------
    def test_store_cards_present(self):
        count = self.stores.get_store_count()
        assert count > 0, f"No stores found, count={count}"

    # ------------------------------
    # FULL FLOW (FILTER → SCROLL → STORE → LANDING → TABS)
    # ------------------------------
    def test_filters_functionality(self):

        # Step 1: Get filters
        filters, count = self.stores.get_all_filters()
        assert count > 0, "No filters found on Stores page"

        # Step 2: Loop filters
        for i in range(count):
            filter_text = filters.nth(i).inner_text().strip()
            print(f"Testing filter: {filter_text}")

            # Open filter
            assert self.stores.open_filter_by_index(i), \
                f"Failed to open filter {filter_text}"

            # Verify dropdown
            if "Sort" in filter_text:
                assert self.stores.verify_sort_dropdown_opened(), \
                    "Sort dropdown not visible"
            else:
                assert self.stores.verify_dropdown_opened(), \
                    f"Dropdown not visible for {filter_text}"

            print(f"Dropdown opened for: {filter_text}")

            # Close dropdown
            self.stores.close_dropdown()

        # Step 3: Scroll page
        self.stores.scroll_full_page()

        # Step 4: Click first store
        assert self.stores.click_first_store(), \
            "Store click failed"

        # Step 5: Wait for navigation (✅ improved)
        self.stores.page.wait_for_load_state("domcontentloaded")
        self.stores.page.wait_for_timeout(1500)

        # Step 6: Verify landing page
        assert self.stores.verify_store_landing_page(), \
            "Store landing page not opened"

        # Step 7: Validate store name
        store_name = self.stores.get_store_name()
        assert store_name is not None and store_name != "", \
            "Store name not loaded"

        # ✅ Step 8: Click and validate tabs (Deals / Coupons / About)
        assert self.stores.click_store_tabs(), \
            "Store tabs interaction failed"