from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def click(self, locator) -> None:
        self.driver.find_element(*locator).click()

    def fill_text(self, locator, txt: str) -> None:
        el = self.driver.find_element(*locator)
        el.clear()
        el.send_keys(txt)

    def get_text(self, locator) -> str:
        return self.driver.find_element(*locator).text


