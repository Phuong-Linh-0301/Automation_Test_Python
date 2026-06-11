import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.recruitment_menu import RecuitmentPage

class TestAddVacancies:
    def add_vacancies(self, driver):
        vacancies_page = TestNavigate(driver=driver)
        assert login_page.is_upgrade_button_displayed() == True