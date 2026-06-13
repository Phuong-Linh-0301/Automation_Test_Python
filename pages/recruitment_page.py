import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.page_base import BasePage
from utils.config_reader import ConfigReader


class RecuitmentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Khởi tạo driver để giúp tương tác với Chrome
        self.driver = driver
        
        # Đặt thời gian chờ ngầm định cho driver (10 giây)
        self.driver.implicitly_wait(10)
        
        # Danh sách các locator của các element trên trang Recuitment
        self.vacancies_tab = (By.XPATH, '//a[text()="Vacancies"]')

        #Danh sách các locator của các element trên tab Vacancies
        self.add_vacancy_btn = (By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]')
        
        self.add_vacancy_header = (By.XPATH, '//h6[text()="Add Vacancy"]')
        self.edit_vacancy_header = (By.XPATH, '//h6 [text()="Edit Vacancy"]')
        

        self.vacancy_name = (By.XPATH, '(//div[@data-v-957b4417]/input)[1]')
        self.job_title_dropdown = (By.XPATH, '//div[@class="oxd-select-text-input"]')
        self.description_field = (By.XPATH,'//textarea[@placeholder="Type description here"]')
        self.hiring_manager_field = (By.XPATH,'//input[@placeholder="Type for hints..."]')
        
        self.user_dropdown_name = (By.CLASS_NAME, "oxd-userdropdown-name")
        
        self.position_number = (By.XPATH, '(//div[@data-v-957b4417]/input)[2]')
        self.role = (By.XPATH, '//span[text()="Automaton Tester"]')


        self.active_switch = (By.XPATH, '(//span[@class="oxd-switch-input oxd-switch-input--active --label-right"])[1]')
        self.publish_switch = (By.XPATH, '(//span[@class="oxd-switch-input oxd-switch-input--active --label-right"])[2]')

        self.save_btn = (By.XPATH, '//button[@type="submit"]')
        self.cancel_btn = (By.XPATH, '//button[@type="button" and @class="oxd-button oxd-button--medium oxd-button--ghost"]')

        self.vacancies_list = (By.XPATH, '//div[@class="oxd-table orangehrm-vacancy-list"]')
        self.search_job_title_dropdown = (By.XPATH, '(//div[@class="oxd-select-text-input"])[1]')

    def navigate_to_vacancies_tab(self):
        self.driver.find_element(*self.vacancies_tab).click()

    def is_vacancies_tab_displayed(self):
    #Đợi tối đa 10 giây cho đến khi nút upgrade xuất hiện trên màn hình và trả về True/False
        return WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.vacancies_tab)).is_displayed()

    def click_add_vacancy(self):
        self.driver.find_element(*self.add_vacancy_btn).click()

    def is_add_vacancy_header_displayed(self):
    #Đợi tối đa 10 giây cho đến khi header Add Vacancy xuất hiện trên màn hình
        return WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.add_vacancy_header)).is_displayed()

    # def select_value(self,job_title_dropdown,add_vacancy,vacancy_name,description_field,hiring_manager_field,position_number):
    #     self.add_vacancy 
    def enter_vacancy_name(self, name):
        element = self.driver.find_element(*self.vacancy_name)
        element.clear()
        element.send_keys(name)

    def select_job_title(self, job_title):
        self.driver.find_element(*self.job_title_dropdown).click()
        # Wait for dropdown options to appear
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@role="option"]'))
        )
        # Tìm thẻ span chứa chính xác tên Job Title được truyền vào để click
        role_option = (By.XPATH, f'//div[@role="option"]//span[text()="{job_title}"]')
        self.driver.find_element(*role_option).click()

    def enter_description(self, desc):
        """Đã sửa: Nhận dữ liệu text desc động"""
        element = self.driver.find_element(*self.description_field)
        element.clear()
        element.send_keys(desc)

    def select_hiring_manager(self, manager_keyword):
        # 1. Tìm ô nhập liệu Hiring Manager và dán text vào
        manager_input = self.driver.find_element(*self.hiring_manager_field)
        manager_input.click()
        manager_input.send_keys(manager_keyword)
    
        # 2. Đợi hộp thoại gợi ý (Dropdown danh sách kết quả) xuất hiện trong DOM
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//span[@data-v-08362132=""]'))
        )
    
        # 3. Di chuyển con trỏ xuống dòng gợi ý đầu tiên và bấm chọn
        manager_input.send_keys(Keys.ARROW_DOWN)
        manager_input.send_keys(Keys.ENTER)
    
        
    def enter_position_number(self, positions):
        element = self.driver.find_element(*self.position_number)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(str(positions))


    def configure_status_switches(self, active, publish):
        """Configure the Active and Publish switches with explicit waits.

        Uses element_to_be_clickable and raises a clear TimeoutException if
        the expected toggle cannot be found within the timeout.
        """
        wait = WebDriverWait(self.driver, 10)

        if not active:
            try:
                el = wait.until(EC.element_to_be_clickable(self.active_switch))
                if el.is_displayed() and el.is_enabled():
                    el.click()
            except TimeoutException:
                raise TimeoutException(f"Active switch not found/clickable: {self.active_switch}")

        if publish:
            try:
                el = wait.until(EC.element_to_be_clickable(self.publish_switch))
                if el.is_displayed() and el.is_enabled():
                    el.click()
            except TimeoutException:
                raise TimeoutException(f"Publish switch not found/clickable: {self.publish_switch}")


    def fill_entire_vacancy_form(self, name, job_title, desc, manager_keyword, positions):
        self.enter_vacancy_name(name)
        self.select_job_title(job_title)
        self.enter_description(desc)
        self.select_hiring_manager(manager_keyword)
        self.enter_position_number(positions)
        #self.configure_status_switches(active, publish)


    def click_save(self):
        self.driver.find_element(*self.save_btn).click()

    def is_edit_vacancy_header_displayed(self):
        return WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.edit_vacancy_header)).is_displayed()
  
    def click_cancel(self):
        self.driver.find_element(*self.cancel_btn).click()

    def is_vacancies_list_displayed(self):
        return WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.vacancies_list)).is_displayed()

    #Hàm phục vụ cho Bước 10: Tìm kiếm lại bản ghi vừa tạo
    def search_created_vacancy(self, job_title, manager_keyword):
        self.driver.find_element(*self.search_job_title_dropdown).click()
        self.driver.find_element(By.XPATH, f'//div[@role="option"]//span[text()="{job_title}"]').click()
        
        # Nếu muốn search theo manager
        if manager_keyword:
            m_input = self.driver.find_element(*self.search_hiring_manager_field)
            m_input.send_keys(manager_keyword)
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@role="listbox"]')))
            m_input.send_keys(Keys.ARROW_DOWN)
            m_input.send_keys(Keys.ENTER)
            
        self.driver.find_element(*self.search_btn).click()

    def get_results_count(self):
        return len(self.driver.find_elements(*self.table_records))

    def get_first_row_name(self):
        return self.driver.find_element(*self.first_row_vacancy_name).text

    def perform_logout(self):
        self.driver.find_element(*self.user_dropdown).click()
        self.driver.find_element(*self.logout_link).click()
        
