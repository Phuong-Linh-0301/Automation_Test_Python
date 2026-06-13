import pytest
from selenium import webdriver
from utils.config_reader import ConfigReader

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(time_to_wait=ConfigReader.get_timeout())
    driver.get(ConfigReader.get_base_url())
    yield driver
    driver.quit()