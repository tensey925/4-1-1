from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        get_url = self.browser.current_url
        assert get_url == 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/', \
            "Wrong link is provided to get login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), "Registration button is not presented"

    def register_new_user(self, email, password):
        self.enter_registration_email(email)
        self.enter_registration_password(password)
        self.enter_registration_confirm_password(password)
        register_button = self.get_element_from_tuple(*LoginPageLocators.REGISTRATION_BUTTON)
        register_button.click()

    def enter_registration_email(self, email):
        email_field = self.get_element_from_tuple(*LoginPageLocators.REGISTRATION_EMAIL_FIELD)
        email_field.send_keys(email)

    def enter_registration_password(self, password):
        password_field = self.get_element_from_tuple(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD)
        password_field.send_keys(password)

    def enter_registration_confirm_password(self, password):
        confirm_password_field = self.get_element_from_tuple(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_FIELD)
        confirm_password_field.send_keys(password)
