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
