import pytest
import time
from .pages.search_page import SearchPage

@pytest.mark.parametrize('link', ["https://yandex.ru"])
def test_guest_add_to_basket_product_page(browser, link):
    page = SearchPage(browser, link)
    page.open()
    page.should_be_search_field()
    page.search_da_text()
    page.should_be_search_suggest()
    page.press_enter()
    page.should_be_link()
    time.sleep(5)