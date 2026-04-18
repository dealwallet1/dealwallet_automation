import pytest
from pages.deals_page import DealsPage
from playwright.sync_api import Page

@pytest.mark.deals
class TestDealsPage:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.deals = DealsPage(page)
        self.deals.navigate()

   
    def test_page_load(self):
        assert self.deals.verify_page_loaded()

   
    def test_deal_cards_present(self):
        count = self.deals.get_deals_count()
        assert count > 0, f"No deals found, count={count}"


    def test_filters_functionality(self):
        filters, count = self.deals.get_all_filters()

        assert count > 0, "No filters found on Deals page"

        for i in range(count):
            filter_text = filters.nth(i).inner_text().strip()

            print(f" Testing filter: {filter_text}")

            
            assert self.deals.open_filter_by_index(i), \
                f"Failed to open filter {filter_text}"

            
            if "Sort By" in filter_text:
                assert self.deals.verify_sort_dropdown_opened(), \
                    "Sort dropdown not visible"

                print(" Sort By dropdown opened")
                self.deals.close_dropdown()
                continue

            
            assert self.deals.verify_dropdown_opened(), \
                f"Dropdown not visible for {filter_text}"

            print(f" Dropdown opened for: {filter_text}")
            self.deals.close_dropdown()

        
        before = self.deals.get_deals_count()

        self.deals.scroll_page_full()

        after = self.deals.get_deals_count()

        print(f" Deals before scroll: {before}, after scroll: {after}")

        assert after >= before, "Deals did not load on scroll"

        
        self.deals.scroll_to_top()