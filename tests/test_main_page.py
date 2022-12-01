import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.main_page import MainPage, MainLocators

class TestMainPage:
    @allure.title('Проверка вопроса "Сколько это стоит?"')
    @allure.description('Находим на странице вопрос "Сколько это стоит" и проверяем что открывается соответствующий ответ')
    def test_check_question_1(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((BasePage.cookies_button_locator)))
        cookies = driver.find_element(*BasePage.cookies_button_locator)
        cookies.click()
        question_1 = driver.find_element(*MainLocators.question_1_locator)
        driver.execute_script("arguments[0].scrollIntoView();", question_1)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((MainLocators.question_1_locator)))
        question_1.click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((MainLocators.answer_1_locator)))
        answer_1 = driver.find_element(*MainLocators.answer_1_locator)
        assert answer_1.text == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('Проверка вопроса "Хочу сразу несколько самокатов! Так можно?"')
    @allure.description('Находим на странице вопрос "Хочу сразу несколько самокатов! Так можно?" и проверяем что открывается соответствующий ответ')
    def test_check_question_2(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        question_2 = driver.find_element(*MainLocators.question_2_locator)
        driver.execute_script("arguments[0].scrollIntoView();", question_2)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((MainLocators.question_2_locator)))
        question_2.click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((MainLocators.answer_2_locator)))
        answer_2 = driver.find_element(*MainLocators.answer_2_locator)
        assert answer_2.text == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.title('Проверка вопроса "Как рассчитывается время аренды?"')
    @allure.description(
        'Находим на странице вопрос "Как рассчитывается время аренды?" и проверяем что открывается соответствующий ответ')
    def test_check_question_3(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        question_3 = driver.find_element(*MainLocators.question_3_locator)
        driver.execute_script("arguments[0].scrollIntoView();", question_3)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((MainLocators.question_3_locator)))
        question_3.click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((MainLocators.answer_3_locator)))
        answer_3 = driver.find_element(*MainLocators.answer_3_locator)
        assert answer_3.text == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.title('Проверка вопроса "Можно ли заказать самокат прямо на сегодня?"')
    @allure.description(
        'Находим на странице вопрос "Можно ли заказать самокат прямо на сегодня?" и проверяем что открывается соответствующий ответ')
    def test_check_question_4(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        question_4 = driver.find_element(*MainLocators.question_4_locator)
        driver.execute_script("arguments[0].scrollIntoView();", question_4)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((MainLocators.question_4_locator)))
        question_4.click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((MainLocators.answer_4_locator)))
        answer_4 = driver.find_element(*MainLocators.answer_4_locator)
        assert answer_4.text == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('Проверка вопроса "Можно ли продлить заказ или вернуть самокат раньше?"')
    @allure.description(
        'Находим на странице вопрос "Можно ли продлить заказ или вернуть самокат раньше?" и проверяем что открывается соответствующий ответ')
    def test_check_question_5(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        question_5 = driver.find_element(*MainLocators.question_5_locator)
        driver.execute_script("arguments[0].scrollIntoView();", question_5)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((MainLocators.question_5_locator)))
        question_5.click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((MainLocators.answer_5_locator)))
        answer_5 = driver.find_element(*MainLocators.answer_5_locator)
        assert answer_5.text == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.title('Проверка вопроса "Вы привозите зарядку вместе с самокатом?"')
    @allure.description(
        'Находим на странице вопрос "Вы привозите зарядку вместе с самокатом?" и проверяем что открывается соответствующий ответ')
    def test_check_question_6(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        question_6 = driver.find_element(*MainLocators.question_6_locator)
        driver.execute_script("arguments[0].scrollIntoView();", question_6)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((MainLocators.question_6_locator)))
        question_6.click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((MainLocators.answer_6_locator)))
        answer_6 = driver.find_element(*MainLocators.answer_6_locator)
        assert answer_6.text == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.title('Проверка вопроса "Можно ли отменить заказ?"')
    @allure.description(
        'Находим на странице вопрос "Можно ли отменить заказ?" и проверяем что открывается соответствующий ответ')
    def test_check_question_7(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        question_7 = driver.find_element(*MainLocators.question_7_locator)
        driver.execute_script("arguments[0].scrollIntoView();", question_7)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((MainLocators.question_7_locator)))
        question_7.click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((MainLocators.answer_7_locator)))
        answer_7 = driver.find_element(*MainLocators.answer_7_locator)
        assert answer_7.text == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.title('Проверка вопроса "Я жизу за МКАДом, привезёте?"')
    @allure.description(
        'Находим на странице вопрос "Я жизу за МКАДом, привезёте?" и проверяем что открывается соответствующий ответ')
    def test_check_question_8(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        question_8 = driver.find_element(*MainLocators.question_8_locator)
        driver.execute_script("arguments[0].scrollIntoView();", question_8)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((MainLocators.question_8_locator)))
        question_8.click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((MainLocators.answer_8_locator)))
        answer_8 = driver.find_element(*MainLocators.answer_8_locator)
        assert answer_8.text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'