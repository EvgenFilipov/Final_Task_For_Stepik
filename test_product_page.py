from .pages.product_page import ProductPage


def test_guest_can_add_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)  # инициализируем объект Page Object
    page.open()  # открываем страницу в браузере
    product_page = ProductPage(browser, browser.current_url)
    page.should_be_add_to_cart_button()  # проверяем что есть кнопка добавления в корзину
    page.add_product_to_cart() # жмем кнопку добавить в корзину



