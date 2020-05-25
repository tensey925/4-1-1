from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_product_page_link()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.is_product_price_equals_to_the_basket_amount()
    page.is_product_name_equals_to_the_basket_product()
