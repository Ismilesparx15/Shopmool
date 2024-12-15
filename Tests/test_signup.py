import pytest
from Pages.login_page import LoginPage
from utils.config import URL, MOBILE_NUMBER, OTP
import random
import uuid

def generate_random_email():
    return f"user_{uuid.uuid4().hex[:6]}@yopmail.com"

def generate_random_mobile():
    return f"9{random.randint(100000000, 999999999)}"

def generate_random_name():
    first_names = ["John", "Jane", "Alex", "Emily", "Chris", "Laura", "Michael", "Sarah", "David", "Emma"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Taylor", "Anderson"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"


def test_signup(setup):
    """
    Test case to verify that a user can signup to the  website successfully.
    """

# Create an instance of the LoginPage POM
    page = setup
    login_page = LoginPage(page)

# Generate random credentials
    mobile_number = generate_random_mobile()
    email = generate_random_email()
    full_name = generate_random_name()
        # Step 1: Navigate to the login page
    login_page.navigate_to(URL)

     # Step 2: Click on the profile icon
    login_page.click_profile_icon()

        # Step 2: Enter the mobile number
    login_page.enter_mobile_number(mobile_number)

        # Step 3: Click the login button
    login_page.click_login()

        # Step 4: Enter OTP (simulated for the test; replace with actual OTP handling logic)
    login_page.enter_otp(OTP)

        # Step 5: Submit the OTP
    login_page.submit_otp()

    login_page.email_address_input(email)
    login_page.fullname_input_selector(full_name)
    login_page.birthdate_input_selector("15-12-2019")
    login_page.anniversarydate_input_selector("15-12-2019")
    login_page.profile_submit_button()
    login_page.click_profile_icon()   # Open profile dropdown again

        # Add assertions to verify successful login

    # Step 8: Verify the presence of the "Account" option in the dropdown
    assert login_page.is_profile_dropdown_visible(), "Login failed: Profile dropdown not visible after login."



