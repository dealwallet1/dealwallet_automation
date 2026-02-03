import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    """Fixture to provide a fresh browser page for each test"""
    from utils.config import Config
    config = Config()
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=config.HEADLESS)
        context = browser.new_context(
        
        )
        page = context.new_page()
        
        yield page
        
        page.close()
        context.close()
        browser.close()

def pytest_html_report_title(report):
    # Default title if no specific marker used
    title = "DealWallet Automation Test Report"

    try:
        config = report.config
        markexpr = getattr(config.option, "markexpr", None)
        if markexpr:
            if "login" in markexpr:
                title = "DealWallet Login Page Test Report"
            elif "home" in markexpr:
                title = "DealWallet Home Page Test Report"
    except Exception:
        pass

    report.title = title



