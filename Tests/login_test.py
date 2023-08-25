import pytest
from Pages.LoginPage_pages import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_log_in_passed(self):
        login_page = LoginPage(self.driver)
        login_page.open_page()
        login_page.log_in("standard_user", "secret_sauce")
        assert "Products" in login_page.msg_passed_log_in

    def test_log_in_failed(self):
        login_page = LoginPage(self.driver)
        login_page.open_page()
        login_page.log_in("standard_user1", "secret_sauce1")
        assert "Epic sadface: Username and password do not match any user in this service" in login_page.error_msg

