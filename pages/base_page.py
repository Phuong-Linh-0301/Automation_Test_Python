import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*locator))
    

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    def is_displayed(self, locator):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except:
            return False
    
    def select_option_from_dropdown(self, dropdown_locator, option_text):
        dropdown = self.find_element(dropdown_locator)
        try:
            select = Select(dropdown)
            select.select_by_visible_text(option_text)
            return
        except Exception:
            return None
        
    def get_text(self, locator):
        return self.wait_for_visible(locator).text.strip()    
        
    def wait_for_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
    
    def wait_for_invisible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.invisibility_of_element_located(locator))
    
    def wait_for_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self.wait_for_clickable(locator).click()
    
    def wait_for_presence(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
    
     