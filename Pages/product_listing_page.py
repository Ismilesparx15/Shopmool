from Pages.base_page import BasePage

class ProductListingPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.product_name_selector = "//a[contains(text(),'Embroidered Regular Chikankari Pure Cotton Kurta w')]"

    def click_product_name(self):
        self.page.click(self.product_name_selector)
