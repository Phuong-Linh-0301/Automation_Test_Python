import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def test_navigate(driver):
    print(f'Tiêu đề trang 1 là: {driver.title}')

    driver.get("https://google.com")
    print(f'Tiêu đề trang 2 là: {driver.title}')
    driver.back()
    print(f'Tiêu đề trước là: {driver.title}')