from selenium.webdriver.common.by import By
import time
from FinalProjectAutomation.pageobjects.BasePage import BasePage


class CategoryPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.ShopByCategory = self.driver.find_elements(By.CSS_SELECTOR,".sidebar.sidebar-main .item a")


    def chooseShopCategory(self,name):
        time.sleep(2)
        for el in self.ShopByCategory:
            if el.text.strip().lower() == name.strip().lower():
                el.click()
                break