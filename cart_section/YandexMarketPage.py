from .BaseApp import BasePage
from selenium.webdriver.common.by import By


class YandexMarketLocators:
    LOCATOR_YA_SEARCH_FIELD = (By.ID, 'header-search')
    LOCATOR_YA_SEARCH_BUTTON = (By.CLASS_NAME, '_1XiEJDPVpk')
    LOCATOR_YA_NOTIFICATION_BUTTON = (By.CLASS_NAME, '_1qOETCp-Ym')
    LOCATOR_YA_PRODUCT_LINK = (By.CLASS_NAME, '_2DyHt9sctH')
    LOCATOR_YA_ADD_TO_CART_BUTTON = (By.CLASS_NAME, "_1UPuXOJfD4")
    LOCATOR_YA_GO_TO_CART_BUTTON = (By.CSS_SELECTOR, ".zsSJkfeAPw._2sWJL7-h2E._16jABpOZ2-._36y1jOUHs5._2_x8rfeWTI"
                                                     "._1GRkjutzG9")
    LOCATOR_YA_PRICE_OF_PRODUCT = (By.XPATH, "//*[@class='b_15TlWlsQyX']")
    LOCATOR_YA_DELETE_FROM_CART = (By.XPATH, "//div[@data-tid = 'c17de28d']")
    LOCATOR_YA_CART_QUANTITY = (By.XPATH, "//div[@data-tid-prop = '4b145b4d']")


class MainHelper(BasePage):

    def enter_product(self, word):
        search_field = self.find_element(YandexMarketLocators.LOCATOR_YA_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def get_attrib_search_field(self):
        search_field = self.find_element(YandexMarketLocators.LOCATOR_YA_SEARCH_FIELD)
        return search_field.get_attribute('value')

    def click_on_search_button(self):
        return self.find_element(YandexMarketLocators.LOCATOR_YA_SEARCH_BUTTON, time=2).click()

    def find_element_notification(self):
        return self.find_element(YandexMarketLocators.LOCATOR_YA_NOTIFICATION_BUTTON, time=2).click()


class SearchHelper(BasePage):

    def find_product(self):
        return self.find_element(YandexMarketLocators.LOCATOR_YA_PRODUCT_LINK).click()

    def find_add_button(self):
        return self.find_element(YandexMarketLocators.LOCATOR_YA_ADD_TO_CART_BUTTON).click()

    def find_go_to_cart_button(self):
        return self.find_element(YandexMarketLocators.LOCATOR_YA_GO_TO_CART_BUTTON).click()


class CartHelper(BasePage):

    def check_product_price(self):
        return self.find_element(YandexMarketLocators.LOCATOR_YA_PRICE_OF_PRODUCT).text

    def delete_product_from_cart(self):
        return self.find_element_clickable(YandexMarketLocators.LOCATOR_YA_DELETE_FROM_CART).click()

    def get_text_from_cart(self):
        return self.find_element(YandexMarketLocators.LOCATOR_YA_CART_QUANTITY).text
