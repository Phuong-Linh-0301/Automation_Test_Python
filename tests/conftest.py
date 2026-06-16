import pytest
from selenium import webdriver
from utils.config_reader import ConfigReader
import allure 
from allure_commons.types import AttachmentType

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(time_to_wait=ConfigReader.get_timeout())
    driver.get(ConfigReader.get_base_url())
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(), 
                name="Failure screenshot", 
                attachment_type=AttachmentType.PNG)