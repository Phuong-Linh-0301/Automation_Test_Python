import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class RecuitmentPage:
    def __init__(self, driver):
        # Khởi tạo driver để giúp tương tác với Chrome
        self.driver = driver
        # Danh sách các locator của các element trên trang Recuitment
        self.vacancies_tab = (By.XPATH, '//a[@class="oxd-topbar-body-nav-tab-item"]')

        #Danh sách các locator của các element trên tab Vacancies
        self.add_vacancy = (By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]')
        self.vacancy_name = (By.XPATH, '//div[@data-v-957b4417]/input[1]')
        self.job_title_dropdown = (By.XPATH, '//div[@class="oxd-select-text-input"]')
        self.description_field = (By.XPATH,'//textarea[@placeholder="Type description here"]')
        self.hiring_manager_field = (By.XPATH,'//input[@placeholder="Type for hints..."]')
        self.position_number = (By.XPATH, '//div[@data-v-957b4417]/input[2]')
        self.role = (By.XPATH, "//span[text()="Automaton Tester"]")

        self.save_btn = (By.XPATH, "//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]")
        self.cancel_btn = (By.XPATH, "//button[@class="oxd-button oxd-button--medium oxd-button--ghost"]")


        self.user_dropdown = (By.XPATH, "//span[@class="oxd-userdropdown-tab"]")

    def navigate_to_vacancies(self, username, password):
        self.driver.find_element(*self.vacancies_tab).click()

    def is_vacancies_tab_displayed(self):
    #Đợi tối đa 10 giây cho đến khi nút upgrade xuất hiện trên màn hình và trả về True/False
        return WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.vacancies_tab)).is_displayed()

    # def select_value(self,job_title_dropdown,add_vacancy,vacancy_name,description_field,hiring_manager_field,position_number):
    #     self.add_vacancy 
    def enter_vacancy_name(self):
        element = self.driver.find_element(*self.vacancy_name)
        element.send_keys("Automation Test")

    def enter_job_title(self):
        self.driver.find_element(*self.job_title_dropdown).click()
        self.driver.find_element(*self.role).click()

    def enter_description_field(self):
        element = self.driver.find_element(*self.self.description_field)
        element.send_keys("Automation Test is Running")

    def enter_hiring_manager(self):
        element = self.driver.find_element(*self.user_dropdown).click()
        element.send_keys(Keys.ARROW_DOWM)

    #//span[@class="oxd-userdropdown-tab"]