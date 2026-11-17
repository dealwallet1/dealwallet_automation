# from pages.base_page import BasePage

# class LoginPage(BasePage):
#     def __init__(self, page):
#         super().__init__(page)

        
#         self.url = f"{self.base_url}/signin"

#         self.EMAIL = "input[type='email']"
#         self.PASSWORD = "input[type='password']"

        
#         self.SUBMIT = "button:has-text('Sign'), button[type='submit']"

#     def navigate(self):
       
#         self.page.goto(
#             self.url,
#             timeout=60000,
#             wait_until="domcontentloaded"
#         )
#         self.handle_cookie_popup()
#         self.wait_for_page_ready()

#     def login(self, email, password):
#         self.navigate()

        
#         self.safe_fill(self.EMAIL, email)
#         self.safe_fill(self.PASSWORD, password)
#         self.safe_click(self.SUBMIT)

        
#         self.page.wait_for_timeout(3000)

#     def get_login_result(self):
#         self.handle_cookie_popup()

#         current_url = self.page.url.lower()

        
#         if any(k in current_url for k in ["account", "profile", "dashboard"]):
#             return {"success": True, "message": "Login successful"}

        
#         error_selectors = [
#             "text=invalid",
#             "text=incorrect",
#             "text=failed",
#             "text=error"
#         ]

#         for err in error_selectors:
#             if self.page.locator(err).count() > 0:
#                 return {"success": False, "message": "Login failed"}

        
#         if "signin" in current_url or "login" in current_url:
#             return {"success": False, "message": "Still on login page"}

       
#         return {"success": False, "message": "Unknown state"}





# from pages.base_page import BasePage


# class LoginPage(BasePage):

#     def __init__(self, page):
#         super().__init__(page)

#         self.url = f"{self.base_url}/signin"

#         # Login form locator
#         self.LOGIN_FORM = "form"

#         # Login form fields
#         self.EMAIL = "input[type='email']"
#         self.PASSWORD = "input[type='password']"
#         self.SUBMIT = "button[type='submit']"

#         self.login_form = None
#         self.login_page_url = None

#     # --------------------------------------------------
#     # Navigate to Login Page
#     # --------------------------------------------------

#     def navigate(self):

#         print("\nOpening DealWallet login page...")

#         self.page.goto(
#             self.url,
#             timeout=60000,
#             wait_until="domcontentloaded"
#         )

#         # Handle cookie popup
#         self.handle_cookie_popup()

#         # Identify the actual login form
#         self.login_form = (
#             self.page.locator(self.LOGIN_FORM)
#             .filter(has_text="Forgot Password?")
#             .first
#         )

#         self.login_form.wait_for(
#             state="visible",
#             timeout=15000
#         )

#         print("Login form loaded successfully.")

#         # Verify email field
#         email_field = self.login_form.locator(self.EMAIL)

#         email_field.wait_for(
#             state="visible",
#             timeout=10000
#         )

#         # Verify password field
#         password_field = self.login_form.locator(self.PASSWORD)

#         password_field.wait_for(
#             state="visible",
#             timeout=10000
#         )

#         self.login_page_url = self.page.url

#         print("Login page ready:", self.page.url)

#     # --------------------------------------------------
#     # Login Function
#     # --------------------------------------------------

#     def login(self, email, password):

#         # Navigate to login page
#         self.navigate()

#         print("\nEntering email...")

#         email_field = self.login_form.locator(self.EMAIL)
#         email_field.fill(email)

#         print("Email entered successfully.")

#         print("Entering password...")

#         password_field = self.login_form.locator(self.PASSWORD)
#         password_field.fill(password)

#         print("Password entered successfully.")

#         print("Clicking Login button...")

#         submit_button = self.login_form.locator(
#             self.SUBMIT
#         ).first

#         submit_button.wait_for(
#             state="visible",
#             timeout=10000
#         )

#         submit_button.click()

#         print("Login form submitted.")

#         # Wait for navigation or application response
#         self.page.wait_for_timeout(4000)

#         print("Current URL after login:", self.page.url)

#     # --------------------------------------------------
#     # Get Login Result
#     # --------------------------------------------------

#     def get_login_result(self):

#         current_url = self.page.url
#         current_url_lower = current_url.lower()

#         print("\nChecking login result...")
#         print("Current URL:", current_url)

#         # 1. Check successful login welcome message
#         welcome_message = self.page.get_by_text(
#             "Welcome back to DealWallet",
#             exact=False
#         )

#         if (
#             welcome_message.count() > 0
#             and welcome_message.first.is_visible()
#         ):

#             message = welcome_message.first.inner_text().strip()

#             return {
#                 "success": True,
#                 "message": message,
#                 "url": current_url
#             }

#         # 2. Check authenticated user indicators
#         auth_indicators = [
#             "text=Sign out",
#             "text=Logout",
#             "a[href*='logout']"
#         ]

#         for selector in auth_indicators:

#             elements = self.page.locator(selector)

#             for i in range(elements.count()):

#                 if elements.nth(i).is_visible():

#                     return {
#                         "success": True,
#                         "message": "Authenticated user indicator found",
#                         "url": current_url
#                     }

#         # 3. Check actual login error messages
#         error_selectors = [
#             "[role='alert']",
#             "text=Invalid credentials",
#             "text=Incorrect password",
#             "text=Invalid email or password"
#         ]

#         for selector in error_selectors:

#             errors = self.page.locator(selector)

#             for i in range(errors.count()):

#                 error = errors.nth(i)

#                 if error.is_visible():

#                     message = error.inner_text().strip()

#                     if message:

#                         return {
#                             "success": False,
#                             "message": message,
#                             "url": current_url
#                         }

#         # 4. Check whether user is still on login page
#         if any(
#             word in current_url_lower
#             for word in ["signin", "sign-in", "login"]
#         ):

#             return {
#                 "success": False,
#                 "message": "Still on login page",
#                 "url": current_url
#             }

#         # 5. Do not assume every homepage redirect is successful
#         return {
#             "success": False,
#             "message": "Redirected, but authentication not confirmed",
#             "url": current_url
#         }

















import time

from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.url = f"{self.base_url}/signin"

        # Login form
        self.LOGIN_FORM = "form"
        self.EMAIL = "input[type='email']"
        self.PASSWORD = "input[type='password']"
        self.SUBMIT = "button[type='submit']"

        self.login_form = None
        self.login_page_url = None

        # Network diagnostics
        self.network_errors = []
        self.failed_requests = []

    # --------------------------------------------------
    # Navigate to Login Page
    # --------------------------------------------------

    def navigate(self):

        print("\nOpening DealWallet login page...")

        self.page.goto(
            self.url,
            timeout=60000,
            wait_until="domcontentloaded"
        )

        self.handle_cookie_popup()

        # Select the actual login form
        self.login_form = (
            self.page.locator(self.LOGIN_FORM)
            .filter(has_text="Forgot Password?")
            .first
        )

        self.login_form.wait_for(
            state="visible",
            timeout=15000
        )

        # Wait for login fields
        self.login_form.locator(self.EMAIL).wait_for(
            state="visible",
            timeout=10000
        )

        self.login_form.locator(self.PASSWORD).wait_for(
            state="visible",
            timeout=10000
        )

        self.login_page_url = self.page.url

        print("Login form loaded successfully.")
        print("Login page ready:", self.page.url)

    # --------------------------------------------------
    # Capture Network Errors
    # --------------------------------------------------

    def capture_network_errors(self):

        self.network_errors = []
        self.failed_requests = []

        def handle_response(response):

            request = response.request

            # Capture API/network responses, not images or stylesheets
            if request.resource_type in ["xhr", "fetch"]:
                if response.status >= 400:

                    self.network_errors.append({
                        "url": response.url,
                        "status": response.status
                    })

        def handle_request_failed(request):

            if request.resource_type in ["xhr", "fetch"]:

                self.failed_requests.append({
                    "url": request.url,
                    "failure": request.failure
                })

        self.page.on("response", handle_response)
        self.page.on("requestfailed", handle_request_failed)

        return handle_response, handle_request_failed

    # --------------------------------------------------
    # Login Function
    # --------------------------------------------------

    def login(self, email, password):

        self.navigate()

        # Start capturing network activity before submitting
        response_handler, request_handler = (
            self.capture_network_errors()
        )

        try:

            print("\nEntering email...")

            self.login_form.locator(self.EMAIL).fill(email)

            print("Email entered successfully.")

            print("Entering password...")

            self.login_form.locator(self.PASSWORD).fill(password)

            print("Password entered successfully.")

            print("Clicking Login button...")

            submit_button = self.login_form.locator(
                self.SUBMIT
            ).first

            submit_button.wait_for(
                state="visible",
                timeout=10000
            )

            submit_button.click()

            print("Login form submitted.")

            # Wait for a real result instead of using a fixed 4-second wait
            start_time = time.monotonic()
            timeout_seconds = 15

            while time.monotonic() - start_time < timeout_seconds:

                result = self.get_login_result()

                if result["success"]:
                    break

                if result["message"] not in [
                    "Still on login page",
                    "Login result not available yet"
                ]:
                    break

                self.page.wait_for_timeout(500)

            print("\nCurrent URL after login:", self.page.url)

        finally:

            self.page.remove_listener(
                "response",
                response_handler
            )

            self.page.remove_listener(
                "requestfailed",
                request_handler
            )

        # Print network diagnostics
        if self.network_errors:

            print("\nFailed API Responses:")

            for error in self.network_errors:
                print(error)

        if self.failed_requests:

            print("\nFailed Network Requests:")

            for request in self.failed_requests:
                print(request)

    # --------------------------------------------------
    # Get Login Result
    # --------------------------------------------------

    def get_login_result(self):

        current_url = self.page.url
        current_url_lower = current_url.lower()

        # 1. Check the actual successful login message first
        welcome_message = self.page.get_by_text(
            "Welcome back to DealWallet",
            exact=False
        )

        if (
            welcome_message.count() > 0
            and welcome_message.first.is_visible()
        ):

            message = welcome_message.first.inner_text().strip()

            return {
                "success": True,
                "message": message,
                "url": current_url
            }

        # 2. Check known authentication error messages
        error_messages = [
            "Something went wrong.",
            "Invalid credentials",
            "Invalid email or password",
            "Incorrect password",
            "Please enter a valid email"
        ]

        for message in error_messages:

            error_locator = self.page.get_by_text(
                message,
                exact=False
            )

            for index in range(error_locator.count()):

                element = error_locator.nth(index)

                if element.is_visible():

                    actual_message = element.inner_text().strip()

                    return {
                        "success": False,
                        "message": actual_message,
                        "url": current_url
                    }

        # 3. Check authenticated user indicators
        auth_indicators = [
            "text=Sign out",
            "text=Logout",
            "a[href*='logout']"
        ]

        for selector in auth_indicators:

            elements = self.page.locator(selector)

            for index in range(elements.count()):

                if elements.nth(index).is_visible():

                    return {
                        "success": True,
                        "message": "Authenticated user indicator found",
                        "url": current_url
                    }

        # 4. Still on login page
        if any(
            word in current_url_lower
            for word in ["signin", "sign-in", "login"]
        ):

            return {
                "success": False,
                "message": "Still on login page",
                "url": current_url
            }

        # 5. Redirect without confirmed authentication
        return {
            "success": False,
            "message": "Login result not available yet",
            "url": current_url
        }
