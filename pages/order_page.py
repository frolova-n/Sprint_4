from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class OrderLocators:
    for_whom_scooter_header = (By.XPATH, "*//div[@class='Order_Header__BZXOb']")
    name_field_locator = (By.XPATH, "(*//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN'])[1]")
    surname_field_locator = (By.XPATH, '*//input[@placeholder="* Фамилия"]')
    adress_field_locator = (By.XPATH, '*//input[@placeholder="* Адрес: куда привезти заказ"]')
    metro_field_locator = (By.XPATH, '*//input[@placeholder="* Станция метро"]')
    teatralnaya_locator =(By.XPATH, "*//li[@class='select-search__row'][32]//div[@class='Order_Text__2broi']")
    phone_field_locator = (By.XPATH, '*//input[@placeholder="* Телефон: на него позвонит курьер"]')
    next_button = (By.XPATH, "*//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    about_rent_header_locator = (By.XPATH, "*//div[@class='Order_Header__BZXOb']")


class OrderForm(BasePage):

    def enter_name(self, data):
        name_field = self.find_element(OrderLocators.name_field_locator)
        name_field.click()
        name_field.send_keys(data)
        return name_field

    def enter_surname(self, data):
        surname_field = self.find_element(OrderLocators.surname_field_locator)
        surname_field.click()
        surname_field.send_keys(data)
        return surname_field

    def enter_adress(self, data):
        adress_field = self.find_element(OrderLocators.adress_field_locator)
        adress_field.click()
        adress_field.send_keys(data)
        return adress_field

    def enter_metro(self):
        metro_field = self.find_element(OrderLocators.metro_field_locator)
        metro_field.click()
        teatralnaya_station = self.find_element(OrderLocators.teatralnaya_locator)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((OrderLocators.teatralnaya_locator)))
        teatralnaya_station.click()
        return metro_field

    def enter_phone(self, data):
        phone_field = self.find_element(OrderLocators.phone_field_locator)
        phone_field.click()
        phone_field.send_keys(data)
        return phone_field

    def click_on_next_button(self):
        return self.find_element(OrderLocators.next_button, time = 2).click()

    def cookies_click(self, driver):
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((BasePage.cookies_button_locator)))
        cookies = driver.find_element(*BasePage.cookies_button_locator)
        return cookies.click()

    def order_page_enter(self, name, surname, adress, phone):
        self.enter_name(name)
        self.enter_surname(surname)
        self.enter_adress(adress)
        self.enter_metro()
        self.enter_phone(phone)
        self.click_on_next_button()
