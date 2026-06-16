import pytest
from datetime import datetime
import uuid
from selenium.webdriver.common.by import By
# Import các trang từ folder Pages để phối hợp chạy kịch bản
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.recruitment_page import RecuitmentPage  
from utils.config_reader import ConfigReader  

def test_create_new_automation_tester_vacancy_flow(driver):
    
    # Khởi tạo dữ liệu tên Vacancy động kèm ngày hôm nay (Bước 5)
    current_date = datetime.now().strftime("%d/%m/%Y")
    random_suffix = uuid.uuid4().hex[:6]
    expected_vacancy_name = f"Automation Tester For1 {current_date} {random_suffix}"

    # Đăng nhập hệ thống 
    login_page = LoginPage(driver)
    login_page.login(ConfigReader.get_username(), ConfigReader.get_password())
    assert login_page.is_upgrade_button_displayed() == True, "Lỗi: Đăng nhập không thành công!"

    # Từ Dashboard điều hướng sang trang Recruitment 
    dashboard_page = DashboardPage(driver)
    dashboard_page.navigate_to_recruitment_page()
    
    # Khởi tạo trang Recruitment để tiếp tục các hành động tiếp theo
    recruitment_page = RecuitmentPage(driver)
    recruitment_page.navigate_to_vacancies_tab()
    
    # Chọn nút "Add"
    recruitment_page.click_add_vacancy()
    
    # Verify trang Add Vacancy hiển thị thành công 
    assert recruitment_page.is_add_vacancy_header_displayed()==True, "Lỗi: Không điều hướng được tới trang Add Vacancy!"
    
    # Xử lý lấy tên user động và nhập Form 
    # 1. Lấy text từ ô userdropdownname ngay tại file test
    user_locator = (By.XPATH, '//p[@class="oxd-userdropdown-name"]')
    manager_keyword_from_web = driver.find_element(*user_locator).text 

    

    # 2. Truyền biến này vào hàm điền form tổng
    recruitment_page.fill_entire_vacancy_form(
    name=expected_vacancy_name,
    job_title="Automaton Tester",
    desc="Automation Test Is Running",
    manager_keyword=manager_keyword_from_web,  
    positions=1,
    #active=False,
    #publish=True
    )
    
    # Bấm nút Save sau khi đã điền xong form
    recruitment_page.click_save()

    # Verify trang Edit Vacancy hiển thị (Xác nhận lưu thành công) ----
    assert recruitment_page.is_edit_vacancy_header_displayed() == True, "Lỗi: Lưu thất bại, URL không chuyển sang editVacancy!"
    
    # Bấm nút Cancel ----
    recruitment_page.click_cancel()
    
    # Verify quay lại trang danh sách Vacancies thành công ----
    assert recruitment_page.is_vacancies_list_displayed() == True, "Lỗi: Không quay lại được màn hình danh sách!"
    
    # Tìm kiếm thông tin vừa tạo ----
    # Ô manager_keyword để rỗng để hệ thống tự lọc theo tài khoản vừa tạo
    recruitment_page.search_created_vacancy(job_title="Automaton Tester", manager_keyword=manager_keyword_from_web)
    
    # Verify có ít nhất 1 dòng kết quả xuất hiện trong bảng ----
    assert recruitment_page.get_results_count() >= 1, "Lỗi: Không tìm thấy bản ghi nào sau khi Search!"
    
    # Verify dữ liệu hiển thị ở dòng đầu tiên trùng khớp dữ liệu đã nhập ----
    actual_name = recruitment_page.get_first_row_name()
    assert actual_name == expected_vacancy_name, f"Lỗi: Tên Vacancy bị lệch! Kỳ vọng: {expected_vacancy_name}, Thực tế: {actual_name}"
    
    # Đăng xuất (Logout) ----
    recruitment_page.perform_logout()
    assert "login" in driver.current_url, "Lỗi: Đăng xuất không thành công!"

