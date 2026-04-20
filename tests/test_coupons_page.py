import pytest
from pages.coupons_page import CouponsPage
from playwright.sync_api import Page

@pytest.mark.coupons
class TestCouponsPage:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.coupons = CouponsPage(page)
        self.coupons.navigate()

    def test_page_load(self):
        assert self.coupons.verify_page_loaded()

    def test_coupon_cards_present(self):
        count = self.coupons.get_coupon_count()
        assert count > 0, f"No coupons found, count={count}"

    def test_filters_and_share(self):
        filters, valid_indexes = self.coupons.get_all_filters()

        assert len(valid_indexes) > 0, "No valid filters found"

       
        for i in valid_indexes:
            filter_text = filters.nth(i).inner_text().strip()

            print(f" Testing filter: {filter_text}")

            assert self.coupons.open_filter_by_index(i), \
                f"Failed to open filter {filter_text}"

            if "Sort By" in filter_text:
                assert self.coupons.verify_sort_dropdown_opened(), \
                    "Sort dropdown not visible"
            else:
                assert self.coupons.verify_dropdown_opened(), \
                    f"Dropdown not visible for {filter_text}"

            print(f" Dropdown opened: {filter_text}")

            self.coupons.close_dropdown()

        self.coupons.scroll_full_page()

        assert self.coupons.click_first_share_icon(), \
            "Failed to click share icon"

        assert self.coupons.verify_share_popup_opened(), \
            "Share popup not visible"