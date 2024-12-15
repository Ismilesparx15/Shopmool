from Pages.base_page import BasePage

class ProductDetailPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.color_radio_selector_template = "//input[@type='radio' and @value='Green']"
        # self.size_selector = "//select[@name='size']"
        self.add_to_cart_button_selector = "//button[@aria-label='add cart']"
        self.cart_confirmation_selector = "//div[contains(text(),'Product added to cart')]"  # Update this selector as needed


    def select_color(self, color):
        # Use the color value to construct the selector for the radio button
        color_radio_selector = self.color_radio_selector_template.format(color=color)
        self.page.click(color_radio_selector)

    # def select_size(self, size):
    #     self.page.select_option(self.size_selector, size)

    def click_add_to_cart(self):
        self.page.click(self.add_to_cart_button_selector)

    def is_product_added_to_cart(self):
        """Check if the product added to cart confirmation is visible."""
        return self.page.is_visible(self.cart_confirmation_selector)
    def wait_for_cart_confirmation(self):
        """Wait for the product added to cart confirmation message to appear."""
        self.page.wait_for_selector(self.cart_confirmation_selector, timeout=10000)  # Wait up to 10 seconds
