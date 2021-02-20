import math
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .locators import SearchPageLocators
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class SearchPage(BasePage):
    def should_be_search_field(self):
        assert self.is_element_present(*SearchPageLocators.TEXT_LINE), "no search fields"

    def search_da_text(self):
        search = self.browser.find_element(*SearchPageLocators.TEXT_INPUT)
        search.send_keys("Тензор")

    def should_be_search_suggest(self):
        assert self.is_not_element_present(*SearchPageLocators.SUGGEST_TABLE), "Suggestion table did not appeared"

    def press_enter(self):
        search = self.browser.find_element(*SearchPageLocators.TEXT_INPUT)
        search.send_keys(Keys.ENTER)

    def should_be_link(self):
        expected_link="tensor.ru"
        assert self.is_element_present(*SearchPageLocators.RIGHT_LINK), "no right link"