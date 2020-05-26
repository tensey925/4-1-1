from pages.locators import ProductPageLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
import pytest


def test_guest_can_add_product_to_basket_no_promo(browser):
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
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Test expects that success message is not appeared, but if it appears - all is fine"


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be because nothing is added to basket"


@pytest.mark.xfail(reason="message disappearance functionality is not implemented")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_click()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but is not disappearing"


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page2 = LoginPage(browser, browser.current_url)
    page2.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_view_basket_page()
    page2 = BasketPage(browser, browser.current_url)
    page2.should_be_empty_basket()
    page2.should_be_empty_basket_message_shown()
