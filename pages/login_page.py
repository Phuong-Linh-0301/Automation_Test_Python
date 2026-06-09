import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage:
    def __init__(self, driver):
        # Khởi tạo driver để giúp tương tác với Chrome
        self.driver = driver
        # Danh sách các locator của các element trên trang login
        self.username_field = (By.NAME, 'username')
        self.password_field = (By.NAME, 'password')
        self.click_btn = (By.XPATH, '//button[@type="submit"]')
        self.upgrade_btn = (By.XPATH, '//button[@class="oxd-glass-button orangehrm-upgrade-button"]')

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.click_btn).click()

    #def is_upgrade_button_displayed(self):
    #Đợi tối đa 10 giây cho đến khi nút upgrade xuất hiện trên màn hình và trả về True/False
        #return WebDriverWait(self.driver, 10).until(
    #lambda d: d.find_element(*self.upgrade_btn)
    #).is_displayed()