from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "span>a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_BUTTON = (By.NAME, "login_submit")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")
    REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")


class ProductPageLocators:
    ADD_BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    BASKET_AMOUNT = (By.XPATH, '//div[@class="alertinner "]//p//strong')
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, "div.product_main>h1")
    NAME_OF_PRODUCT_ADDED = (By.CSS_SELECTOR, "#messages>div>div>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div")


class BasketPageLocators:
    BASKET_HEADER = (By.XPATH, '//div[@class="page_inner"]//div//h1[contains(text(), "Basket")]')
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//a[text()='Proceed to checkout']")
    EMPTY_BASKET_MESSAGE = (By.XPATH, '//div[@id="content_inner"]//p[contains(text(), "Your basket is empty.")]')
    BASKET_FORM = (By.CSS_SELECTOR, "form#basket_formset")
