# import pytest
# import json
# from pages.login_page import LoginPage
# from playwright.sync_api import Page

# def load_test_data():
#     with open('users.json', 'r') as f:
#         return json.load(f)

# @pytest.mark.login
# class TestLoginPage:
    
#     @pytest.fixture(autouse=True)
#     def setup(self, page: Page):
#         self.login_page = LoginPage(page)
#         self.login_page.navigate()
    
#     @pytest.mark.parametrize(
#         "test_data",
#         load_test_data(),
#         ids=[data["scenario"] for data in load_test_data()]
#     )
#     def test_login_scenarios(self, test_data):
#         email = test_data['email']
#         password = test_data['password']
#         expected = test_data['expected']

#         self.login_page.login(email, password)
#         result = self.login_page.get_login_result()

#         print(f"\nResult: {result}")

        
#         if expected == "success":
#             assert (
#                 result["success"] 
#                 or result["message"] != "Unknown state"
#             ), f"Login unstable or blocked: {result}"

      
#         else:
#             assert not result["success"], f"Expected failure but got success"






# import pytest
# import json

# from pages.login_page import LoginPage
# from playwright.sync_api import Page


# # --------------------------------------------------
# # Load Login Test Data
# # --------------------------------------------------

# def load_test_data():

#     with open("users.json", "r") as file:
#         return json.load(file)


# TEST_DATA = load_test_data()


# # --------------------------------------------------
# # Login Test Cases
# # --------------------------------------------------

# @pytest.mark.login
# class TestLoginPage:

#     @pytest.fixture(autouse=True)
#     def setup(self, page: Page):

#         self.login_page = LoginPage(page)

#     @pytest.mark.parametrize(
#         "test_data",
#         TEST_DATA,
#         ids=[data["scenario"] for data in TEST_DATA]
#     )

#     def test_login_scenarios(self, test_data):

#         email = test_data["email"]
#         password = test_data["password"]
#         expected = test_data["expected"]

#         scenario = test_data["scenario"]

#         print("\n====================================")
#         print(f"Test Scenario: {scenario}")
#         print(f"Expected Result: {expected}")
#         print("====================================")

#         # Execute login
#         self.login_page.login(email, password)

#         # Get login result
#         result = self.login_page.get_login_result()

#         print("\nLogin Test Result:")
#         print(result)

#         # Validate successful login
#         if expected == "success":

#             assert result["success"] is True, (
#                 f"Valid login failed: {result}"
#             )

#             print("\nPASS: Valid login successful.")

#         # Validate unsuccessful login
#         else:

#             assert result["success"] is False, (
#                 f"Expected login failure but got success: {result}"
#             )

#             print("\nPASS: Invalid login correctly rejected.")

#         print("\n====================================")


























import json
import pytest

from pages.login_page import LoginPage
from playwright.sync_api import Page


# --------------------------------------------------
# Load Test Data
# --------------------------------------------------

def load_test_data():

    with open("users.json", "r", encoding="utf-8") as file:
        return json.load(file)


TEST_DATA = load_test_data()


# --------------------------------------------------
# Login Test Cases
# --------------------------------------------------

@pytest.mark.login
class TestLoginPage:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):

        self.login_page = LoginPage(page)

    @pytest.mark.parametrize(
        "test_data",
        TEST_DATA,
        ids=[data["scenario"] for data in TEST_DATA]
    )
    def test_login_scenarios(self, test_data):

        email = test_data["email"]
        password = test_data["password"]
        expected = test_data["expected"]
        scenario = test_data["scenario"]

        print("\n====================================")
        print(f"Test Scenario: {scenario}")
        print(f"Expected Result: {expected}")
        print("====================================")

        # Execute login
        self.login_page.login(email, password)

        # Get final login result
        result = self.login_page.get_login_result()

        print("\nLogin Test Result:")
        print(result)

        # Print diagnostics if valid login fails
        if expected == "success" and not result["success"]:

            print("\nVALID LOGIN FAILED")

            print("\nCurrent Page URL:")
            print(self.login_page.page.url)

            print("\nCurrent Page Content:")
            print(
                self.login_page.page.locator("body").inner_text()[:2000]
            )

            print("\nFailed API Responses:")
            print(self.login_page.network_errors)

            print("\nFailed Network Requests:")
            print(self.login_page.failed_requests)

        # Validate successful login
        if expected == "success":

            assert result["success"] is True, (
                f"Valid login failed: {result}"
            )

            print("\nPASS: Valid login successful.")

        # Validate negative scenarios
        else:

            assert result["success"] is False, (
                f"Expected login failure but got success: {result}"
            )

            print("\nPASS: Invalid login correctly rejected.")

        print("\n====================================")
