import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage  

class TestLogin:
    def test_login(self, driver):
        login_page = LoginPage(driver=driver)
        login_page.login("Admin", "admin123")
        assert login_page.is_upgrade_button_displayed() == True