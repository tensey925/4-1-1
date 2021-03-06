from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
import pytest
import time


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_product_page_link(
        "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019")
    page.add_to_basket_click()
    page.solve_quiz_and_get_code()
    page.is_product_price_equals_to_the_basket_amount()
    page.is_product_name_equals_to_the_basket_product()


@pytest.mark.parametrize('promo',
                         [
                             "0", "1", "2", "3", "4", "5", "6",
                             pytest.param(7, marks=pytest.mark.xfail),
                             "8", "9"
                         ])
def test_guest_can_add_product_to_basket_with_promo(browser, promo):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}".format(promo)
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page_link(
        "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer{}".format(promo))
    page.add_to_basket_click()
    page.solve_quiz_and_get_code()
    page.is_product_price_equals_to_the_basket_amount()
    page.is_product_name_equals_to_the_basket_product()


@pytest.mark.xfail(reason="message appears - all is fine")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_click()
    page.should_not_be_success_message_after_adding_product_to_basket()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message_if_nothing_in_the_basket()


@pytest.mark.xfail(reason="message disappearance functionality is not implemented")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_click()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page2 = LoginPage(browser, browser.current_url)
    page2.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_view_basket_page()
    page2 = BasketPage(browser, browser.current_url)
    page2.should_be_empty_basket()
    page2.should_be_empty_basket_message_shown()


@pytest.mark.login_test_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = '1*23$56789'
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message_if_nothing_in_the_basket()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_be_product_page_link(
            "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019")
        page.add_to_basket_click()
        page.solve_quiz_and_get_code()
        page.is_product_price_equals_to_the_basket_amount()
        page.is_product_name_equals_to_the_basket_product()
