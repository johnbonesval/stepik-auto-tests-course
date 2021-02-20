import math
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):
    def add_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        login_link.click()
        #current_name = str(self.browser.current_url)
        #expected_name = LoginPageLocators.LOGIN_URL
        #assert expected_url in current_url, "wrong url"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_successuful_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "message is not presented"

    def should_not_be_successuful_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def is_not_element_present(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def is_disappeared(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_product_names(self):
        current_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_ADD_MESSAGE).text
        expected_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        current_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE_ADD_MESSAGE).text
        expected_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        assert current_price in expected_price, "wrong price"
        assert current_title in expected_title, "wrong title"