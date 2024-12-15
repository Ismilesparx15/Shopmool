from Pages.base_page import BasePage

class CategoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.final_category_selector = "//a[normalize-space()='DRESSES']"

    def click_final_category(self):
        self.page.click(self.final_category_selector)
