from Pages.Order_products_pages import OrderProducts
import pytest


@pytest.mark.usefixtures("setup")
class TestOrder:

    def test_order_products(self):
        order_products = OrderProducts(self.driver)
        order_products.open_page()
        order_products.log_in("standard_user", "secret_sauce")
        order_products.add_products()
        order_products.cart_click()
        order_products.information_order("Test", "Testerski", "00-00")
        assert "Thank you for your order" in  order_products.succes_comunicate


