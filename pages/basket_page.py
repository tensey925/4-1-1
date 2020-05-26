from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_product_page_link(self, compare_url):
        self.should_be_basket_page_url(compare_url)
        self.should_be_basket_page_header()
        self.should_be_proceed_to_checkout_button()

    def should_be_basket_page_url(self, compare_url):
        get_url = self.browser.current_url
        assert get_url == compare_url, "Wrong link is provided to get basket page"

    def should_be_basket_page_header(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_HEADER), \
            "There is no Basket header element on the page"

    def should_be_proceed_to_checkout_button(self):
        assert self.is_element_present(*BasketPageLocators.PROCEED_TO_CHECKOUT_BUTTON), \
            "PROCEED TO CHECKOUT button is not presented"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORM), "Basket is not empty, but it should be"

    def should_be_empty_basket_message_shown(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Basket is empty message should be shown, but it is not"
