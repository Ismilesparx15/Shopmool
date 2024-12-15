import pytest
from Pages.login_page import LoginPage
from utils.config import URL, MOBILE_NUMBER, OTP


def test_login(setup):
    """
    Test case to verify that a user can log in to the e-commerce website successfully.
    """

# Create an instance of the LoginPage POM
    page = setup
    login_page = LoginPage(page)

        # Step 1: Navigate to the login page
    login_page.navigate_to(URL)

     # Step 2: Click on the profile icon
    login_page.click_profile_icon()

        # Step 2: Enter the mobile number
    login_page.enter_mobile_number(MOBILE_NUMBER)

        # Step 3: Click the login button
    login_page.click_login()

        # Step 4: Enter OTP (simulated for the test; replace with actual OTP handling logic)
    login_page.enter_otp(OTP)

        # Step 5: Submit the OTP
    login_page.submit_otp()

    login_page.click_profile_icon()   # Open profile dropdown again

        # Add assertions to verify successful login

    # Step 8: Verify the presence of the "Account" option in the dropdown
    assert login_page.is_profile_dropdown_visible(), "Login failed: Profile dropdown not visible after login."



