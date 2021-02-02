import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart Chrome browser for test")
        browser = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name == "firefox":
        print("\nstart Firefox browser for test")
        browser = webdriver.Firefox(GeckoDriverManager().install())
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser")
    browser.quit()
