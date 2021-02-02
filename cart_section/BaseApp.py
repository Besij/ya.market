from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.base_url = 'https://market.yandex.ru'

    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def find_element_clickable(self, locator, time=5):
        return WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(locator),
                                                       message=f"Can't find element by locator {locator}")

    def go_to_site(self):
        page = requests.get(self.base_url)
        if page.status_code == 200:
            return self.browser.get(self.base_url)
        else:
            return 'Failed'
