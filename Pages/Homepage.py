from Pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.route_category_selector = "//div[contains(text(),'WOMEN')]"

    def click_route_category(self):
        self.page.click(self.route_category_selector)
