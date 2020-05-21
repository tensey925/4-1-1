from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    # LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    # LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")



