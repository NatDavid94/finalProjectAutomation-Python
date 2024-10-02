from selenium.webdriver.common.by import By
import time
from FinalProjectAutomation.pageobjects.BasePage import BasePage


class CategoriesPage(BasePage):

    # list
    listCategories = (By.CSS_SELECTOR, "#ui-id-2 [role='presentation'] a")


    def __init__(self, driver):
        super().__init__(driver)
        self.listCategories = self.driver.find_elements(By.CSS_SELECTOR, "#ui-id-2 [role='presentation'] a")


    def chooseCategory(self,name):
        time.sleep(2)
        for el in self.listCategories:
            if el.text.strip().lower() == name.strip().lower():
                el.click()
                break


                