from pages.landing_page import LandingPage
from pages.top_nav import TopNav
from pages.pdp_page import PDPPage
from pages.catalogue_page import CataloguePage
import config
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_add_to_cart(page):
    try:
        landing_page = LandingPage(page)
        top_nav = TopNav(page)
        catalogue_page = CataloguePage(page)
        pdp_page = PDPPage(page)
        url = config.URL

        logging.info("Navigating to URL: %s", url)
        try:
            landing_page.goto(url)
        except Exception as e:
            logging.error("Failed to navigate to URL: %s", e)
            raise

        logging.info("Navigating to bags section.")
        try:
            top_nav.navigate_to_bags()
        except Exception as e:
            logging.error("Failed to navigate to bags: %s", e)
            raise

        logging.info("Selecting product: 'Push It Messenger Bag'")
        try:
            catalogue_page.select_product('Push It Messenger Bag')
        except Exception as e:
            logging.error("Failed to select product: %s", e)
            raise

        logging.info("Adding product to cart.")
        try:
            pdp_page.click_element(pdp_page.BUTTON_ADD_TO_CART)
            page.wait_for_load_state("networkidle")
        except Exception as e:
            logging.error("Failed to add product to cart or wait for network idle: %s", e)
            raise

        logging.info("Validating cart counter.")
        try:
            counter_text = page.inner_text(top_nav.COUNTER_NUMBER)
            assert counter_text == '1', f"Expected counter to be '1', but got '{counter_text}'"
        except AssertionError as ae:
            logging.error("Assertion failed: %s", ae)
            raise
        except Exception as e:
            logging.error("Failed to validate cart counter: %s", e)
            raise

        logging.info("Test 'add to cart' passed successfully.")

    except Exception as e:
        logging.critical("Test 'add to cart' encountered an unexpected error: %s", e)
        raise
