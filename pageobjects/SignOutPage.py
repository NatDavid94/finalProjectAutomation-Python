from selenium.webdriver.common.by import By
import time
from FinalProjectAutomation.pageobjects.BasePage import BasePage


class SignOutPage(BasePage):

    arrowBtn = (By.CSS_SELECTOR, ".panel.header .action.switch")
    signoutBtn = (By.CSS_SELECTOR, "[href='https://magento.softwaretestingboard.com/customer/account/logout/']")


    def __init__(self, driver):
        super().__init__(driver)


    def clickSignOut(self):
        time.sleep(2)
        self.click(self.arrowBtn)
        time.sleep(2)
        self.click(self.signoutBtn)
        time.sleep(7)
