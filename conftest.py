import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    from utils.config import Config
    config = Config()

    with sync_playwright() as p:
      
        browser = p.chromium.launch(
            headless=config.HEADLESS,
            slow_mo=config.SLOW_MO
        )

     
        context = browser.new_context(ignore_https_errors=True)

        page = context.new_page()

        yield page

        page.close()
        context.close()
        browser.close()