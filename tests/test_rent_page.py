from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.order_page import OrderForm
import allure
import time
from pages.rent_page import RentForm, RentLocators

class TestRentPage:
    @allure.title('Проверка страницы "Про аренду" c подтверждением заказа')
    def test_rent_yes(self, driver):
        base_page = BasePage(driver)
        order_page = OrderForm(driver)
        base_page.go_to_site()
        order_page.cookies_click(driver)
        order_page.order_page_enter('Михаил', 'Петров', 'Театральная, 1', '89123456789')
        rent_page = RentForm(driver)
        rent_page.enter_date('12.12.2022')
        rent_page.color_choice_black()
        rent_page.rental_period_days_choice()
        rent_page.comment_write('привет')
        rent_page.order_button_click()
        rent_page.yes_button_click()
        assert driver.find_element(*RentLocators.order_status_button_locator).text == 'Посмотреть статус'

    @allure.title('Проверка страницы "Про аренду" с нажатием на кнопку "нет" в форме подтверждения заказа')
    def test_rent_no(self, driver):
        base_page = BasePage(driver)
        order_page = OrderForm(driver)
        base_page.go_to_site()
        order_page.order_page_enter('Мария', 'Иванова', 'Тверская, 1', '+79123456777')
        rent_page = RentForm(driver)
        rent_page.enter_date('13.12.2022')
        rent_page.color_choice_gray()
        rent_page.rental_period_days_choice()
        rent_page.order_button_click()
        rent_page.no_button_click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((RentLocators.back_button_locator)))
        assert driver.find_element(*RentLocators.back_button_locator).text == 'Назад'

    @allure.title('Проверка логотипа "Яндекс"')
    def test_rent_logo_Yandex(self, driver):
        base_page = BasePage(driver)
        order_page = OrderForm(driver)
        base_page.go_to_site()
        order_page.order_page_enter('Михаил', 'Петров', 'Театральная, 1', '89123456789')
        rent_page = RentForm(driver)
        rent_page.enter_date('12.12.2022')
        rent_page.color_choice_black()
        rent_page.rental_period_days_choice()
        rent_page.comment_write('привет')
        rent_page.order_button_click()
        rent_page.yes_button_click()
        rent_page.status_check()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((RentLocators.Yandex_logo_locator)))
        rent_page.yandex_logo_check()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[0])
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'

    @allure.title('Проверка логотипа "Самокат"')
    def test_rent_logo_scooter(self, driver):
        base_page = BasePage(driver)
        order_page = OrderForm(driver)
        base_page.go_to_site()
        order_page.order_page_enter('Михаил', 'Петров', 'Театральная, 1', '89123456789')
        rent_page = RentForm(driver)
        rent_page.enter_date('12.12.2022')
        rent_page.color_choice_black()
        rent_page.rental_period_days_choice()
        rent_page.comment_write('привет')
        rent_page.order_button_click()
        rent_page.yes_button_click()
        rent_page.status_check()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((RentLocators.Yandex_logo_locator)))
        rent_page.scooter_logo_check()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'