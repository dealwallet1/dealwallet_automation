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
        """Setup for each test"""
        self.login_page = LoginPage(page)
        self.login_page.navigate()
    
    @pytest.mark.parametrize("test_data", load_test_data())
    def test_login_scenarios(self, test_data):
        """Test various login scenarios from users.json"""
        email = test_data['email']
        password = test_data['password']
        expected = test_data['expected']
        scenario = test_data['scenario']
        
        print(f"\n{'='*60}")
        print(f"Scenario: {scenario}")
        print(f"Email: {email}")
        print(f"Password: {password}")
        print(f"Expected Result: {expected}")
        print(f"{'='*60}")
        
    
        self.login_page.login(email, password)
        
        result = self.login_page.get_login_result()
        
        print(f"Actual Result: {'success' if result['success'] else 'error'}")
        print(f"Message: {result['message']}")
        
    
        if expected == 'success':
            assert result['success'], f"Login should succeed for scenario: {scenario}. Message: {result['message']}"
        else:
            assert not result['success'], f"Login should fail for scenario: {scenario}"
        
        print(f"Test Passed: {scenario}\n")