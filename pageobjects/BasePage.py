from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def click(self, locator) -> None:
        self.highlight_element(locator, "Yellow")
        self.driver.find_element(*locator).click()

    def fill_text(self, locator, txt: str) -> None:
        self.highlight_element(locator, "Yellow")
        el = self.driver.find_element(*locator)
        el.clear()
        el.send_keys(txt)

    def get_text(self, locator) -> str:
        return self.driver.find_element(*locator).text


    # Function to highlight an element with a specified color
    def highlight_element(self, locator, color):
        element = self.driver.find_element(*locator)
        original_style = element.get_attribute("style")
        new_style = "background-color: " + color + ";" + original_style

        # Change the style temporarily
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, new_style)

        # Change the style back after a few milliseconds
        self.driver.execute_script("setTimeout(function () { arguments[0].setAttribute('style', arguments[1]); }, 400);"
                                   , element, original_style)
