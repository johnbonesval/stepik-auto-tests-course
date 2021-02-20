from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = "\login"
    LOGIN_FORM = (By.ID, "login-form")
    REGISTER_FORM = (By.ID, "register-form")

class ProductPageLocators():
    BOOK_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_TITLE_ADD_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) strong")
    BASKET_TOTAL_ADD_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages")