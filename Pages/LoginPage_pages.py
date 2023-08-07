from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_input = 'user-name'
        self.password_input = 'password'
        self.msg_passed_log_in = "//span[text()='Products']"
        self.error_msg = "//button[text()='Epic sadface: Username and password do not match any user in this service'"


    def open_page(self):
        self.driver.get("https://www.saucedemo.com/")
    def log_in(self, username, password):
        self.driver.find_element(By.ID, self.username_input).send_keys(username)
        self.driver.find_element(By.ID, self.password_input).send_keys(password)
        self.driver.find_element(By.ID, self.password_input).send_keys(Keys.ENTER)

