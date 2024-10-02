from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

from FinalProjectAutomation.pageobjects.BasePage import BasePage


class CheckoutPage(BasePage):

    firstName = (By.CSS_SELECTOR, "[name='firstname']")
    lastName = (By.CSS_SELECTOR, "[name='lastname']")
    company = (By.CSS_SELECTOR, "[name='company']")
    street0 = (By.CSS_SELECTOR, "[name='street[0]']")
    street1 = (By.CSS_SELECTOR, "[name='street[1]']")
    street2 = (By.CSS_SELECTOR, "[name='street[2]']")
    city = (By.CSS_SELECTOR, "[name='city']")
    postcode = (By.CSS_SELECTOR, "[name='postcode']")
    telephone = (By.CSS_SELECTOR, "[name='telephone']")
    nextBtn = (By.CSS_SELECTOR, "[data-bind=\"i18n: 'Next'\"]")
    newAddress = (By.CSS_SELECTOR, ".action.action-show-popup")
    shipHere = (By.CSS_SELECTOR, ".action.primary.action-save-address")
    stateEl = (By.CSS_SELECTOR, "[name='region']")
    placeOrder = (By.CSS_SELECTOR, ".action.primary.checkout")
    continueShop = (By.CSS_SELECTOR, ".action.primary.continue")
    countryDropdown = (By.CSS_SELECTOR, "[name='country_id']")

    def __init__(self, driver):
        super().__init__(driver)


    def clickNewAddress(self):
        time.sleep(2)
        self.click(self.newAddress)

    def fillCredentails(self,fname,lname,cmpy,st0,st1 ,st2,cty,stateProvince,pstcd,country,tlph):
        time.sleep(2)
        self.fill_text(self.firstName,fname)
        self.fill_text(self.lastName,lname)
        self.fill_text(self.company,cmpy)
        self.fill_text(self.street0,st0)
        self.fill_text(self.street1,st1)
        self.fill_text(self.street2,st2)
        self.fill_text(self.city,cty)

        country_dropdown_element = self.driver.find_element(*self.countryDropdown)
        self.selectCountry = Select(country_dropdown_element)
        self.selectCountry.select_by_visible_text(country)

        self.fill_text(self.stateEl,stateProvince)
        self.fill_text(self.postcode,pstcd)
        self.fill_text(self.telephone, tlph)

    def clickshipHere(self):
        self.click(self.shipHere)

    def clickNext(self):
        self.click(self.nextBtn)

    def clickPlaceOrder(self):
        time.sleep(5)
        self.click(self.placeOrder)
        time.sleep(10)

    def clickContinueShop(self):
        self.click(self.continueShop)