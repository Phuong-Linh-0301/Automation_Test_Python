import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
class TestDragDropGuru99:

    def test_drag_drop_guru99(self, driver):
        """Test kéo thả 4 ô (Account, Amount) từ Debit và Credit side"""

        # Truy cập website
        driver.get("https://demo.guru99.com/test/drag_drop.html")
        driver.maximize_window()
        
        # Khởi tạo ActionChains
        actions = ActionChains(driver)
        
        bank_account = driver.find_element(By.XPATH, "//a[contains(text(), 'BANK')]")
        debit_account_box = driver.find_element(By.ID, "bank")
        
        amount_5000 = driver.find_element(By.XPATH, "//li[@data-id='2'][1]")
        debit_amount_box = driver.find_element(By.ID, "amt7")
        

        sales_account = driver.find_element(By.XPATH, "//a[contains(text(), 'SALES')]")
        credit_account_box = driver.find_element(By.ID, "loan")
        
        amount_5000_credit = driver.find_element(By.XPATH, "//li[@data-id='2'][2]")
        credit_amount_box = driver.find_element(By.ID, "amt8")
        
        
        # Thực hiện kéo thả từng ô một từ Debit và Credit side vào đúng vị trí
        actions.drag_and_drop(bank_account, debit_account_box).perform()
        actions.drag_and_drop(amount_5000, debit_amount_box).perform()
        actions.drag_and_drop(sales_account, credit_account_box).perform()
        actions.drag_and_drop(amount_5000_credit, credit_amount_box).perform()
        sleep(2)  # Thêm thời gian chờ để xem kết quả kéo thả

    # Kiểm tra xem Perfect! có xuất hiện không
        try:
            wait = WebDriverWait(driver, 5)
            perfect_text = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Perfect!']")))
            print("Drag and drop thành công! Perfect xuất hiện.")
            assert perfect_text.is_displayed(), "Perfect message không hiển thị"
        except:
            print("Drag and drop thất bại hoặc Perfect message không xuất hiện")
            raise