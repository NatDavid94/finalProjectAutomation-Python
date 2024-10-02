from selenium.webdriver.common.by import By
import time
from FinalProjectAutomation.pageobjects.BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class ItemsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.listItemsNames = self.driver.find_elements(By.CSS_SELECTOR,".product-item-link")


    def chooseItem(self,name,size,color):
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

        # create listSizesEl Element
        listSizesStr = elementStr + " .swatch-option.text"
        listSizesEl = self.driver.find_elements(By.CSS_SELECTOR,listSizesStr)

        # create listColorsEl Element
        listColorssStr = elementStr + " .swatch-option.color"
        listColorsEl = self.driver.find_elements(By.CSS_SELECTOR,listColorssStr)

        # create addToCartBtn Element
        addToCartStr = elementStr + " .action.tocart.primary"
        addToCartBtn = self.driver.find_element(By.CSS_SELECTOR,addToCartStr)

        # choose the required size
        for el in listSizesEl:
            if el.text.strip().lower() == size.strip().lower():
                el.click()
                break

        # choose the required color
        for el in listColorsEl:
            if el.get_attribute("option-label").strip().lower() == color.strip().lower():
                el.click()
                break

        # click addToCartBtn
        addToCartBtn.click()

    def chooseItemNoDress(self, name):
        time.sleep(2)

        actions = ActionChains(self.driver)

        # Finding the item's number
        i = 0
        for el in self.listItemsNames:
            i += 1
            if el.text.strip().lower() == name.strip().lower():
                # Move the mouse to the item for identifying the button
                actions.move_to_element(el).perform()
                break

        num = str(i)
        # create the string element of chosen item by --> child(num)
        elementStr = "#maincontent > div.columns > div.column.main > div.products.wrapper.grid.products-grid > ol > li:nth-child(" + num + ")"

        # create addToCartBtn Element
        addToCartStr = elementStr + " .action.tocart.primary"
        addToCartBtn = self.driver.find_element(By.CSS_SELECTOR,addToCartStr)

        # click addToCartBtn
        addToCartBtn.click()
