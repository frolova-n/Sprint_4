from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainLocators:
    question_1_locator = (By.XPATH, "*//div[@id='accordion__heading-0']")
    answer_1_locator = (By.XPATH, "*//div[@id='accordion__panel-0']/p")
    question_2_locator = (By.XPATH, "*//div[@id='accordion__heading-1']")
    answer_2_locator = (By.XPATH, "*//div[@id='accordion__panel-1']/p")
    question_3_locator = (By.XPATH, "*//div[@id='accordion__heading-2']")
    answer_3_locator = (By.XPATH, "*//div[@id='accordion__panel-2']/p")
    question_4_locator = (By.XPATH, "*//div[@id='accordion__heading-3']")
    answer_4_locator = (By.XPATH, "*//div[@id='accordion__panel-3']/p")
    question_5_locator = (By.XPATH, "*//div[@id='accordion__heading-4']")
    answer_5_locator = (By.XPATH, "*//div[@id='accordion__panel-4']/p")
    question_6_locator = (By.XPATH, "*//div[@id='accordion__heading-5']")
    answer_6_locator = (By.XPATH, "*//div[@id='accordion__panel-5']/p")
    question_7_locator = (By.XPATH, "*//div[@id='accordion__heading-6']")
    answer_7_locator = (By.XPATH, "*//div[@id='accordion__panel-6']/p")
    question_8_locator = (By.XPATH, "*//div[@id='accordion__heading-7']")
    answer_8_locator = (By.XPATH, "*//div[@id='accordion__panel-7']/p")

class MainPage():

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://qa-scooter.praktikum-services.ru'

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not found locator {locator}')

    def question_find(self, question_locator):
        question = self.find_element(question_locator)
        return question

    def answer_find(self, answer_locator):
        answer = self.find_element(answer_locator)
        return answer.click()