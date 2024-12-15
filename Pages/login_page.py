from Pages.base_page import BasePage

class LoginPage(BasePage):
     def __init__(self, page):
        """
        Constructor for the LoginPage class. It initializes the Playwright page object.

        :param page: Playwright page object
        """
        self.page = page
        self.url = "https://staging.shopmool.in/" # URL of the login page
        self.profile_icon = "//i[@class='icon-profile']"
        self.mobile_number_input_selector = "//input[@placeholder='Enter your mobile number']"  # Replace with the actual selector for the mobile input field
        self.login_button_selector = "//button[normalize-space()='Join / Sign In']"  # Replace with the actual selector for the login button
        self.otp_input_selector = "//input[@placeholder='Enter OTP']"  # Replace with the actual selector for the OTP field
        self.submit_otp_button_selector = "//button[normalize-space()='Verify OTP']"  # Replace with the actual selector for OTP submission
        self.profile_dropdown = "//a[@aria-label='Account'][normalize-space()='Account']"
        self.account_tab = "//h2[normalize-space()='Account details']"  # Highlighted account tab selector
        self.email_address_input_selector = "//input[@placeholder='Enter email address']"
        self.Full_name_input = "//input[@placeholder='Full Name']"
        self.birthdate_input = "//input[@placeholder='Birth date']"
        self.anniversarydate_input = "//input[@placeholder='Anniversary date']"
        self.complete_profile_submit_button = "//button[normalize-space()='Submit']"

     def click_profile_icon(self):
        """Click the profile icon on the header."""
        self.page.click(self.profile_icon)


     def enter_mobile_number(self, mobile_number):
        """
        Enter the mobile number in the mobile input field.

        :param mobile_number: The mobile number to enter
        """
        self.page.fill(self.mobile_number_input_selector, mobile_number)

     def click_login(self):
        """
        Click the login button.
        """
        self.page.click(self.login_button_selector)

     def enter_otp(self, otp):
        """
        Enter the OTP in the OTP input field.

        :param otp: The OTP to enter
        """
        self.page.fill(self.otp_input_selector, otp)

     def submit_otp(self):
        """
        Click the button to submit the OTP.
        """
        self.page.click(self.submit_otp_button_selector)

     def email_address_input(self, email):
        self.page.fill(self.email_address_input_selector, email)

     def fullname_input_selector(self, name):
        self.page.fill(self.Full_name_input, name)

     def birthdate_input_selector(self, birthdate):
        self.page.fill(self.birthdate_input, birthdate)

     def anniversarydate_input_selector(self, anniversarydate):
        self.page.fill(self.anniversarydate_input, anniversarydate)

     def profile_submit_button(self):
        self.page.click(self.complete_profile_submit_button)


     def is_profile_dropdown_visible(self):
        """Check if the profile dropdown is visible."""
        return self.page.is_visible(self.profile_dropdown)



