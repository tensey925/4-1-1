from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"          #передаем линк
    page = MainPage(browser, link)                          #создаем экземпляр класса МэйнПэйдж
    page.open()                                             #открываем получившуюся страницу
    page.go_to_login_page()                                 #вызываем метод чтобы перейти на страницу логина
    login_page = LoginPage(browser, browser.current_url)    #создаем экземпляр класса страницы на которой находимся
    login_page.should_be_login_page()                       #вызываем метод для проверки действительно ли мы на логин странице


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_on_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


