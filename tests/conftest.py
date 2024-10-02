import os
import allure
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


def pytest_exception_interact(report):
    if report.failed:
        allure.attach(body=driver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=allure.attachment_type.PNG)


def pytest_sessionfinish() -> None:
    environment_properties = {
     'browser': driver.name,
     'driver_version': driver.capabilities['browserVersion']
    }
    allure_env_path = os.path.join("allure-results", 'environment.properties')
    with open(allure_env_path, 'w') as f:
        data = '\n'.join([f'{variable}={value}' for variable, value in environment_properties.items()])
        f.write(data)


@pytest.fixture(scope="class", autouse=True)
def driver_init(request):
    global driver
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    driver.maximize_window()
    driver.get("https://magento.softwaretestingboard.com/")
    yield
    driver.quit()