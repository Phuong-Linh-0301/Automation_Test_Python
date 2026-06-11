import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class DashboardPage:
    def __init__(self, driver):
        # Khởi tạo driver để giúp tương tác với Chrome
        self.driver = driver
        # Danh sách các locator của các element trên trang login
        self.recruitment_menu= (By.XPATH, '//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]')
    


    def navigate_to_recuitment_page(self,recruitment_menu):
        self.driver.find_element(*self.recruitment_menu).click()
