import pytest
from selenium import webdriver
@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.driver = driver
    yield
    driver.quit()
