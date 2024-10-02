from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from FinalProjectAutomation.pageobjects.BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class NewTab(BasePage):

    showItemEl = (By.CSS_SELECTOR, ".fotorama__arr.fotorama__arr--next .fotorama__arr__arr")

    def __init__(self, driver):
        super().__init__(driver)
        self.listItemsNames = self.driver.find_elements(By.CSS_SELECTOR,".product-item-link")

    def clickItem(self,name):
        time.sleep(2)
        # finding the item's number
        i = 0
        for el in self.listItemsNames:
            i += 1
            if el.text.strip().lower() == name.strip().lower():
                break
        num = str(i)


        # create the string element of chosen item by --> child(num)
        elementStr = "#maincontent > div.columns > div.column.main > div.products.wrapper.grid.products-grid > ol > li:nth-child(" + num + ")"

        elBtn = self.driver.find_element(By.CSS_SELECTOR, elementStr)

        # Click elBtn and open the item in a new tab (for Windows/Linux)
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).click(elBtn).key_up(Keys.CONTROL).perform()

        # Switch to the newly opened tab
        all_window_handles = self.driver.window_handles
        original_window = self.driver.current_window_handle

        for window_handle in all_window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

        time.sleep(2)

        for j in range(3):
            time.sleep(2)  # Sleep for 2 seconds
            self.click(self.showItemEl)

        self.driver.close()

        # Switch back to the original tab
        self.driver.switch_to.window(original_window)
