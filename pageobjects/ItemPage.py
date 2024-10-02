from selenium.webdriver.common.by import By
import time
from FinalProjectAutomation.pageobjects.BasePage import BasePage


class ItemPage(BasePage):

    addToCartBtn = (By.CSS_SELECTOR, "#product-addtocart-button")
    cartPageBtn = (By.CSS_SELECTOR, ".action.showcart .counter.qty")
    procToCheckout = (By.CSS_SELECTOR, "#top-cart-btn-checkout")


    def __init__(self, driver):
        super().__init__(driver)
        self.listSizes = self.driver.find_elements(By.CSS_SELECTOR,".swatch-option.text")
        self.listColors = self.driver.find_elements(By.CSS_SELECTOR,".swatch-option.color")


    def chooseSize(self,size):
        time.sleep(2)
        for el in self.listSizes:
            if el.text.strip().lower() == size.strip().lower():
                el.click()
                break

    def chooseColor(self,color):
        time.sleep(2)
        for el in self.listColors:
            if el.get_attribute("option-label").strip().lower() == color.strip().lower():
                el.click()
                break


    def addToCart(self):
        self.click(self.addToCartBtn)
        time.sleep(3)

    def goToCartPage(self):
        time.sleep(2)
        self.click(self.cartPageBtn)

    def goToCheckoutPage(self):
        self.click(self.procToCheckout)
        time.sleep(5)
