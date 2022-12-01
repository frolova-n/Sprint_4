from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.order_page import OrderForm, OrderLocators
import allure

class TestOrderPage:
    @allure.title('Проверка страницы "Для кого самокат" с первым набором данных')
    def test_order_page(self, driver):
        base_page = BasePage(driver)
        order_page = OrderForm(driver)
        base_page.go_to_site()
        order_page.cookies_click(driver)
        order_page.order_page_enter('Михаил', 'Петров', 'Театральная, 1','89123456789')
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((OrderLocators.about_rent_header_locator)))
        assert driver.find_element(*OrderLocators.about_rent_header_locator).text == 'Про аренду'

    @allure.title('Проверка страницы "Для кого самокат" со вторым набором данных')
    def test_order_page2(self, driver):
        base_page = BasePage(driver)
        order_page = OrderForm(driver)
        base_page.go_to_site()
        order_page.order_page_enter('Мария', 'Иванова', 'Тверская, 1', '+79123456777')
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((OrderLocators.about_rent_header_locator)))
        assert driver.find_element(*OrderLocators.about_rent_header_locator).text == 'Про аренду'