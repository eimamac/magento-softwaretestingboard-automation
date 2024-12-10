from pages.landing_page import LandingPage
from pages.top_nav import TopNav
from pages.pdp_page import PDPPage
from pages.catalogue_page import CataloguePage
import config
import time

def test_add_to_cart(page):
    landing_page = LandingPage(page)
    top_nav = TopNav(page)
    catalogue_page = CataloguePage(page)
    pdp_page = PDPPage(page)
    url = config.URL
    
    landing_page.goto(url)
    top_nav.navigate_to_bags()

    catalogue_page.select_product('Push It Messenger Bag')
    pdp_page.click_element(pdp_page.BUTTON_ADD_TO_CART)
    page.wait_for_load_state("networkidle")
    
    counter_text = page.inner_text(top_nav.COUNTER_NUMBER)
    assert counter_text == '1'