from .base_page import BasePage

class CataloguePage(BasePage):

    def select_product(self,product_name):
        locator = f'text={product_name}'
        self.click_element(locator) 
