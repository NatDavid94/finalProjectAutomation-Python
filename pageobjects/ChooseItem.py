from selenium.webdriver.common.by import By
import time
from FinalProjectAutomation.pageobjects.BasePage import BasePage


class ChooseItem(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.listItems = self.driver.find_elements(By.CSS_SELECTOR,".product-item-link")


    def chooseItem(self,name):
        time.sleep(2)
        for el in self.listItems:
            if el.text.strip().lower() == name.strip().lower():
                el.click()
                break