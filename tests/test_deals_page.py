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

    def test_filters_and_scroll(self):
        
        self.deals.page.wait_for_load_state("networkidle")

        filters, count = self.deals.get_all_filters()
        assert count > 0, "No filters found"

        for i in range(count):
            text = filters.nth(i).inner_text().strip()
            print(f"Testing filter: {text}")

            assert self.deals.open_filter_by_index(i)

            if "Sort By" in text:
                assert self.deals.verify_sort_dropdown_opened()
            else:
                assert self.deals.verify_dropdown_opened()

            self.deals.close_dropdown()

        before = self.deals.get_deals_count()
        self.deals.scroll_page_full()
        after = self.deals.get_deals_count()

        print(f"Before: {before}, After: {after}")
        assert after >= before

        self.deals.scroll_to_top()

    def test_buy_now_navigation(self):
        assert self.deals.click_first_buy_now(), \
            "Buy Now click failed"

        self.deals.page.wait_for_load_state("domcontentloaded")

        assert self.deals.verify_redirect_to_deal_page(), \
            "Redirection failed"

    def test_share_popup(self):
        # Step 1: Go to deal page
        assert self.deals.click_first_buy_now(), \
            "Buy Now click failed"

        self.deals.page.wait_for_load_state("domcontentloaded")

        assert self.deals.verify_redirect_to_deal_page(), \
            "Redirection failed"

        assert self.deals.click_share_icon(), \
            "Share icon click failed"

        assert self.deals.verify_share_popup_opened(), \
            "Share popup not visible"

    