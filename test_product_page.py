from pages.product_page import ProductPage
import pytest
import time


# def test_guest_can_add_product_to_basket_no_promo(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = ProductPage(browser, link)
#     page.open()
#     product_page = ProductPage(browser, browser.current_url)
#     product_page.should_be_product_page_link()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.is_product_price_equals_to_the_basket_amount()
#     page.is_product_name_equals_to_the_basket_product()


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
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.is_product_price_equals_to_the_basket_amount()
    page.is_product_name_equals_to_the_basket_product()
