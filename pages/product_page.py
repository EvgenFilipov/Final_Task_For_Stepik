from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_add_to_cart_button()


    def should_be_add_to_cart_button(self):  # проверяем что есть кнопка добавления в корзину
        assert self.is_element_present(*ProductPageLocators.CART_LINK), "А где-то кривой локатор!"


    def add_product_to_cart(self):
        cart_link = self.browser.find_element(*ProductPageLocators.CART_LINK)
        cart_link.click()
        self.solve_quiz_and_get_code()
        print("Метод страницы отработал")



    # page.should_be_success_message()  # проверяем что есть сообщение с нужным текстом