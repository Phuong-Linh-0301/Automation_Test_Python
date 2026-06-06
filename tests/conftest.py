import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(time_to_wait=10)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    yield driver
    driver.quit()