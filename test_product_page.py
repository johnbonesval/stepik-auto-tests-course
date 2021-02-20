import pytest
import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_add_to_basket_product_page(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_basket()
    page.should_not_be_successuful_message()
    #page.solve_quiz_and_get_code()
    #page.should_be_successuful_message()
    #page.should_be_product_names()
    time.sleep(3)

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_basket()
    page.should_not_be_successuful_message()
    time.sleep(3)

def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.should_not_be_successuful_message()
    time.sleep(3)

def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.add_to_basket()
    page.should_not_be_successuful_message()
    time.sleep(3)