from pages.Cartpage import Cartpage
from pages.Countrypage import Countrypage
from pages.Homepage import Homepage
import time
import pytest
@pytest.mark.usefixtures("setup_and_teardown")
class Test_fruits:

    def test_add_brocoli(self):
        hp = Homepage(self.driver)
        hp.launch_homapage_url()
        hp.select_products()
        hp.click_cart_icon()
        hp.click_proceed_to_checkout()
        cp = Cartpage(self.driver)
        cp.click_place_order()
        cp.cart_quantity_text()
        country_page = Countrypage(self.driver)
        country_page.select_country_dropdown()
        country_page.click_agree_checkbox()
        country_page.click_proceed_button()
        time.sleep(6)