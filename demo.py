import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def pytest_addoption(parser):  # ✅ Corrected typo here
    parser.addoption(
        "--browser_name", action="store", default="firefox", help="browser selection"
    )


# Automated driver creation for all test cases
@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "firefox":
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
    elif browser_name == "chrome":
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)

    yield driver  # Before test function execution
    driver.close()  # After test function execution
