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
        assert count >= 1, f"No deals found, count={count}"

    def test_sorting(self):
        assert self.deals.sort_by("latest"), "Sorting failed"
