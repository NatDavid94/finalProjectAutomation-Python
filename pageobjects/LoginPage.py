from selenium.webdriver.common.by import By
import time
from FinalProjectAutomation.pageobjects.BasePage import BasePage


class LoginPage(BasePage):

    signInBtn1 = (By.CSS_SELECTOR,"a[href='https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/']")
    emailEl = (By.CSS_SELECTOR, "#email")
    passEl = (By.CSS_SELECTOR, "[name='login[password]']")
    signInBtn2 = (By.CSS_SELECTOR, ".action.login.primary")
    EMAIL_ERROR = (By.CSS_SELECTOR, "#email-error")
    EMAIL_NOT_EXIST = (By.CSS_SELECTOR, ".message-error.error.message")
    PASS_ERROR = (By.CSS_SELECTOR, "#pass-error")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, email, password):
        time.sleep(2)
        self.click(self.signInBtn1)
        self.fill_text(self.emailEl, email)
        self.fill_text(self.passEl, password)
        self.click(self.signInBtn2)

        time.sleep(2)

    def getEmailErrorMsg(self):
        return self.get_text(self.EMAIL_ERROR)

    def getNotExistEmailErrorMsg(self):
        return self.get_text(self.EMAIL_NOT_EXIST)

    def getPassErrorMsg(self):
        return self.get_text(self.PASS_ERROR)