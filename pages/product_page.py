from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket_click(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        link.click()

    def should_be_product_page_link(self, compare_url):
        self.should_be_product_page_url(compare_url)
        self.should_be_product_page_form()
        self.should_be_product_page_button()

    def should_be_product_page_url(self, compare_url):
        get_url = self.browser.current_url
        assert get_url == compare_url, "Wrong link is provided to get product page"

    def should_be_product_page_form(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET_FORM), "Basket form is not presented"

    def should_be_product_page_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET_BUTTON), "Add basket button is not presented"

    def is_product_name_equals_to_the_basket_product(self):
        name_of_product = self.get_text_from_element(
            self.get_element_from_tuple(*ProductPageLocators.NAME_OF_PRODUCT))
        name_of_product_added = self.get_text_from_element(self.get_element_from_tuple(
            *ProductPageLocators.NAME_OF_PRODUCT_ADDED))
        assert name_of_product_added == name_of_product, "Product name is not equal to the product name in the basket"

    def is_product_price_equals_to_the_basket_amount(self):
        product_price = self.get_text_from_element(self.get_element_from_tuple(*ProductPageLocators.PRODUCT_PRICE))
        basket_amount = self.get_text_from_element(self.get_element_from_tuple(*ProductPageLocators.BASKET_AMOUNT))
        assert product_price == basket_amount, "The price is not equal to the amount in the basket"
