from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_BUTTON = (By.NAME, "login_submit")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    ADD_BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    BASKET_AMOUNT = (By.XPATH, '//div[@class="alertinner "]//p//strong')
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, "div.product_main>h1")
    NAME_OF_PRODUCT_ADDED = (By.CSS_SELECTOR, "#messages>div>div>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div")
