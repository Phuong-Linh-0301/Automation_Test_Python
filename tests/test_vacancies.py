import pytest
from datetime import datetime
from selenium.webdriver.common.by import By
# Import các trang từ folder Pages để phối hợp chạy kịch bản
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.recruitment_page import RecuitmentPage  # Viết đúng theo tên class RecuitmentPage hiện tại của bạn

def test_create_new_automation_tester_vacancy_flow(driver):
    
    # Khởi tạo dữ liệu tên Vacancy động kèm ngày hôm nay (Bước 5)
    current_date = datetime.now().strftime("%d/%m/%Y")
    expected_vacancy_name = f"Automation Tester For {current_date}"

    # ---- BƯỚC 1: Đăng nhập hệ thống ----
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    
    # ---- BƯỚC 2: Từ Dashboard điều hướng sang trang Recruitment ----
    dashboard_page = DashboardPage(driver)
    dashboard_page.navigate_to_recruitment_page()
    
    # Khởi tạo trang Recruitment để tiếp tục các hành động tiếp theo
    recruitment_page = RecuitmentPage(driver)
    recruitment_page.navigate_to_vacancies_tab()
    
    # ---- BƯỚC 3: Chọn nút "+Add" ----
    recruitment_page.click_add_vacancy()
    
    # ---- BƯỚC 4: Verify trang Add Vacancy hiển thị thành công ----
    assert recruitment_page.is_add_vacancy_header_displayed()==True, "Lỗi: Không điều hướng được tới trang Add Vacancy!"
    
    # ---- BƯỚC 5: Xử lý lấy tên user động và nhập Form ----
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
    active=False,
    publish=True
    )
    
    # ---- BƯỚC 6: Bấm nút Save ----
    recruitment_page.click_save()
    
    # ---- BƯỚC 7: Verify trang Edit Vacancy hiển thị (Xác nhận lưu thành công) ----
    assert "editVacancy" in driver.current_url, "Lỗi: Lưu thất bại, URL không chuyển sang editVacancy!"
    
    # ---- BƯỚC 8: Bấm nút Cancel ----
    recruitment_page.click_cancel()
    
    # ---- BƯỚC 9: Verify quay lại trang danh sách Vacancies thành công ----
    assert "viewJobVacancies" in driver.current_url, "Lỗi: Không quay lại được màn hình danh sách!"
    
    # ---- BƯỚC 10: Tìm kiếm thông tin vừa tạo ----
    # Ô manager_keyword để rỗng để hệ thống tự lọc theo tài khoản vừa tạo
    recruitment_page.search_created_vacancy(job_title="Automation Tester", manager_keyword="")
    
    # ---- BƯỚC 11: Verify có ít nhất 1 dòng kết quả xuất hiện trong bảng ----
    assert recruitment_page.get_results_count() >= 1, "Lỗi: Không tìm thấy bản ghi nào sau khi Search!"
    
    # ---- BƯỚC 12: Verify dữ liệu hiển thị ở dòng đầu tiên trùng khớp dữ liệu đã nhập ----
    actual_name = recruitment_page.get_first_row_name()
    assert actual_name == expected_vacancy_name, f"Lỗi: Tên Vacancy bị lệch! Kỳ vọng: {expected_vacancy_name}, Thực tế: {actual_name}"
    
    # ---- BƯỚC 13: Đăng xuất (Logout) ----
    recruitment_page.perform_logout()
    assert "login" in driver.current_url, "Lỗi: Đăng xuất không thành công!"