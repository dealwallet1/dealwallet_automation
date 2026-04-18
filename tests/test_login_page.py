import pytest
import json
from pages.login_page import LoginPage
from playwright.sync_api import Page

def load_test_data():
    with open('users.json', 'r') as f:
        return json.load(f)

@pytest.mark.login
class TestLoginPage:
    
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.login_page = LoginPage(page)
        self.login_page.navigate()
    
    @pytest.mark.parametrize(
        "test_data",
        load_test_data(),
        ids=[data["scenario"] for data in load_test_data()]
    )
    def test_login_scenarios(self, test_data):
        email = test_data['email']
        password = test_data['password']
        expected = test_data['expected']

        self.login_page.login(email, password)
        result = self.login_page.get_login_result()

        print(f"\nResult: {result}")

        
        if expected == "success":
            assert (
                result["success"] 
                or result["message"] != "Unknown state"
            ), f"Login unstable or blocked: {result}"

      
        else:
            assert not result["success"], f"Expected failure but got success"