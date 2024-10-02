from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from FinalProjectAutomation.pageobjects.BasePage import BasePage


class DeleteAddress(BasePage):

    settingsBtn = (By.CSS_SELECTOR, ".panel.header .action.switch")
    myAccount = (By.CSS_SELECTOR, "a[href='https://magento.softwaretestingboard.com/customer/account/']")
    addressBook = (By.CSS_SELECTOR, "a[href='https://magento.softwaretestingboard.com/customer/address/']")
    DeleteBtn = (By.CSS_SELECTOR, "[role='delete-address']")
    okBtn = (By.CSS_SELECTOR, ".action-primary.action-accept")

    def __init__(self, driver):
        super().__init__(driver)
        self.listDeleteBtn = self.driver.find_elements(By.CSS_SELECTOR, "[role='delete-address']")

    def goToAdrressPage(self):
        time.sleep(2)
        self.click(self.settingsBtn)  # Use the click method from BasePage
        time.sleep(2)
        self.click(self.myAccount)  # Use the click method from BasePage
        time.sleep(2)
        self.click(self.addressBook)  # Use the click method from BasePage

    def deleteAdress(self):
        size_of_list = len(self.listDeleteBtn)
        for i in range(size_of_list):
            time.sleep(2)
            self.click(self.DeleteBtn)
            time.sleep(2)
            self.click(self.okBtn)
            time.sleep(2)
