from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class RentLocators:
    date_field_locator = (By.XPATH, '*//input[@placeholder="* Когда привезти самокат"]')
    rental_period_locator = (By.XPATH, "*//div[@class='Dropdown-control']")
    rental_period_one_day_locator = (By.XPATH, "*//div[@class='Dropdown-menu']/div[@class='Dropdown-option'][1]")
    scooter_color_locator_black = (By.XPATH, "*//label[@class='Checkbox_Label__3wxSf'][1]")
    scooter_color_locator_gray = (By.XPATH, "*//label[@class='Checkbox_Label__3wxSf'][2]")
    comment_field_locator = (By.XPATH, '*//input[@placeholder="Комментарий для курьера"]')
    order_button_locator = (By.XPATH, '*//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    yes_button_locator = (By.XPATH, '*//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text() = "Да"]')
    no_button_locator = (By.XPATH, "*//button[@class='Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i' and text()='Нет']")
    order_status_button_locator = (By.XPATH, '*//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text() = "Посмотреть статус"]')
    back_button_locator = (By.XPATH, "*//button[@class='Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i' and text() = 'Назад']")
    Yandex_logo_locator = (By.XPATH, "*//a[@class='Header_LogoYandex__3TSOI']")
    scooter_logo_locator = (By.XPATH, "*//a[@class='Header_LogoScooter__3lsAR']")

class RentForm(BasePage):

    def enter_date(self, date):
        date_field = self.find_element(RentLocators.date_field_locator)
        date_field.click()
        date_field.send_keys(date)
        return date_field

    def rental_period_days_choice(self):
        rental_period_field = self.find_element(RentLocators.rental_period_locator)
        rental_period_field.click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(RentLocators.rental_period_one_day_locator))
        rental_period_one_day = self.find_element(RentLocators.rental_period_one_day_locator)
        rental_period_one_day.click()
        return rental_period_field

    def color_choice_black(self):
        color_field_black = self.find_element(RentLocators.scooter_color_locator_black)
        color_field_black.click()
        return color_field_black

    def color_choice_gray(self):
        color_field_gray = self.find_element(RentLocators.scooter_color_locator_gray)
        color_field_gray.click()
        return color_field_gray

    def comment_write(self, data):
        comment_field = self.find_element(RentLocators.comment_field_locator)
        comment_field.click()
        comment_field.send_keys(data)
        return comment_field

    def order_button_click(self):
        order_button = self.find_element(RentLocators.order_button_locator)
        return order_button.click()

    def yes_button_click(self):
        yes_button = self.find_element(RentLocators.yes_button_locator)
        return yes_button.click()

    def no_button_click(self):
        no_button = self.find_element(RentLocators.no_button_locator)
        return no_button.click()

    def status_check(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(RentLocators.order_status_button_locator))
        status_button = self.find_element(RentLocators.order_status_button_locator)
        return status_button.click()

    def yandex_logo_check(self):
        yandex_logo = self.find_element(RentLocators.Yandex_logo_locator)
        return yandex_logo.click()

    def scooter_logo_check(self):
        scooter_logo = self.find_element(RentLocators.scooter_logo_locator)
        return scooter_logo.click()
