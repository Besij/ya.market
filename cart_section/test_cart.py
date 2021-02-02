import time
import allure
from .YandexMarketPage import MainHelper, SearchHelper, CartHelper

PRODUCT_NAME = 'яндекс станция'


@allure.feature('Тест работы корзины сервиса Яндекс.Маркет')
@allure.story('Переход на страницу товара')
def test_guest_can_open_the_search_page(browser):
    yandex_main_page = MainHelper(browser)
    yandex_main_page.go_to_site()
    with allure.step('Скриншот экрана до ввода продукта'):
        allure.attach(browser.get_screenshot_as_png(),
                      name='screenshot_before', attachment_type=allure.attachment_type.PNG)
    with allure.step('Вводим текст в строку поиска'):
        yandex_main_page.enter_product(PRODUCT_NAME)
    with allure.step('Скриншот экрана после ввода'):
        allure.attach(browser.get_screenshot_as_png(),
                      name='screenshot_after', attachment_type=allure.attachment_type.PNG)
    with allure.step('Закрытие всплывающего окна'):
        yandex_main_page.find_element_notification()
    with allure.step('Нажатие на кнопку поиска'):
        yandex_main_page.click_on_search_button()
        time.sleep(5)
    with allure.step('Открывается страница результатов поиска'):
        allure.attach(browser.get_screenshot_as_png(),
                      name='screenshot_search_results', attachment_type=allure.attachment_type.PNG)
        assert browser.title == '«яндекс станция» — Умные колонки — купить на Яндекс.Маркете'
    yandex_search_page = SearchHelper(browser)
    with allure.step('Находим необходимый товар'):
        yandex_search_page.find_product()
        browser.close()
        time.sleep(3)
        browser.switch_to.window(browser.window_handles[0])
    with allure.step('Скриншот страницы продукта'):
        allure.attach(browser.get_screenshot_as_png(),
                      name='screenshot_of_product_page', attachment_type=allure.attachment_type.PNG)
    with allure.step('Проверка корректности открытой страницы'):
        assert browser.title == 'Умная колонка Яндекс.Станция — купить по выгодной цене на Яндекс.Маркете'
    with allure.step('Добавляем товар в корзину'):
        yandex_search_page.find_add_button()
        time.sleep(2)
    with allure.step('Переходим в корзину'):
        yandex_search_page.find_go_to_cart_button()
        time.sleep(2)
    yandex_cart_page = CartHelper(browser)
    with allure.step('Проверяем цену товара в корзине и делаем скриншот'):
        allure.attach(browser.get_screenshot_as_png(),
                      name='MyScreenshot', attachment_type=allure.attachment_type.PNG)
        assert yandex_cart_page.check_product_price() == '12 990 ₽'
    with allure.step('В Корзине должен быть один товар'):
        assert yandex_cart_page.get_text_from_cart() == "1 товар в корзине"
