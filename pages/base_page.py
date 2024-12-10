class BasePage:
    def __init__(self,page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)
    
    def click_element(self, locator):
        self.page.click(locator)