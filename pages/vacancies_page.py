import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class VacanciesPage:
    def __init__(self, driver):
        # Khởi tạo driver để giúp tương tác với Chrome
        self.driver = driver
        # Danh sách các locator của các element trên trang VacanciesPage
        self.add_btn = (By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]')

    def navigate_to_addJob(self, username, password):
        self.driver.find_element(*self.vacancies_tab).click()

    def is_vacancies_tab_displayed(self):
    #Đợi tối đa 10 giây cho đến khi nút upgrade xuất hiện trên màn hình và trả về True/False
        return WebDriverWait(self.driver, 10).until(
    lambda d: d.find_element(*self.vacancies_tab)
    ).is_displayed()
