import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def test_navigate(driver):
    print(driver.title)

    driver.get("https://google.com")
    print(driver.title)
    driver.back()
    print(driver.title)