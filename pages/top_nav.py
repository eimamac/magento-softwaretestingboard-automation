from .base_page import BasePage

class TopNav(BasePage):
    GEAR_MENU = '#ui-id-6'
    BAGS_LINK = '#ui-id-25'
    COUNTER_NUMBER = '.counter-number'

    def navigate_to_bags(self):
        self.page.hover(self.GEAR_MENU)
        self.click_element(self.BAGS_LINK)

    pass