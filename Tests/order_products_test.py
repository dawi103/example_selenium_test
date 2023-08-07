from Pages.Order_products_pages import OrderProducts
import pytest


@pytest.mark.usefixture("setup")
class OrderTest:

    def test_order_products(self):
        order_products = OrderProducts(self.driver)
        order_products.open_page()
        order_products.log_in("standard_user", "secret_sauce")
        order_products.add_product_to_cart1_id()
        order_products.add_product_to_cart2_id()
        order_products.add_product_to_cart3_id()
        order_products.add_product_to_cart4_id()
        order_products.add_product_to_cart5_id()
        order_products.add_product_to_cart6_id()
        order_products.cart_click_id()
        order_products.information_order("Test", "Testowski", "00-00")