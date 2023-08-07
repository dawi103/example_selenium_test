from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class OrderProducts:

    def __init__(self, driver):
        self.driver = driver
        self.username_input_id = 'user-name'
        self.password_input_id = 'password'
        self.add_product_to_cart1_id = 'add-to-cart-sauce-labs-backpack'
        self.add_product_to_cart2_id = 'add-to-cart-sauce-labs-bike-light'
        self.add_product_to_cart3_id = 'add-to-cart-sauce-labs-bolt-t-shirt'
        self.add_product_to_cart4_id = 'add-to-cart-sauce-labs-fleece-jacket'
        self.add_product_to_cart5_id = 'add-to-cart-sauce-labs-onesie'
        self.add_product_to_cart6_id = 'remove-test.allthethings()-t-shirt-(red)'
        self.cart_click_id = 'shopping_cart_container'
        self.checkout_id = 'checkout'
        self.first_name_id = 'first-name'
        self.second_name_id = 'last-name'
        self.postal_code_id = 'postal-code'


    def open_page(self):
        self.driver.get("https://www.saucedemo.com/")

    def log_in(self, username, password):
        self.driver.find_element(By.ID, self.username_input_id).send_keys(username)
        self.driver.find_element(By.ID, self.password_input_id).send_keys(password)
        self.driver.find_element(By.ID, self.password_input_id).send_keys(Keys.ENTER)

    def add_products(self):
        self.driver.find_element(By.ID,self.add_product_to_cart1_id).click()
        self.driver.find_element(By.ID,self.add_product_to_cart2_id).click()
        self.driver.find_element(By.ID,self.add_product_to_cart3_id).click()
        self.driver.find_element(By.ID,self.add_product_to_cart4_id).click()
        self.driver.find_element(By.ID,self.add_product_to_cart5_id).click()
        self.driver.find_element(By.ID,self.add_product_to_cart6_id).click()

    def cart_click(self):
        self.driver.find_element(By.ID, self.cart_click_id).click()


    def information_order(self, firstname, secondname, postalcode):
        self.driver.find_element(By.ID,self.first_name_id).send_keys(firstname)
        self.driver.find_element(By.ID,self.second_name_id).send_keys(secondname)
        self.driver.find_element(By.ID,self.postal_code_id).send_keys(postalcode)