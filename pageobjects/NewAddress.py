from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

from FinalProjectAutomation.pageobjects.BasePage import BasePage


class NewAddress(BasePage):

    addNewAddress = (By.CSS_SELECTOR, "[role='add-address']")
    fName = (By.CSS_SELECTOR, "#firstname")
    lName = (By.CSS_SELECTOR, "#lastname")
    companyName = (By.CSS_SELECTOR, "#company")
    telNumber = (By.CSS_SELECTOR, "#telephone")
    streetEl = (By.CSS_SELECTOR, "#street_1")
    cityEl = (By.CSS_SELECTOR, "#city")
    regionEl = (By.CSS_SELECTOR, "#region")
    zipEl = (By.CSS_SELECTOR, "#zip")
    countryDropdown = (By.CSS_SELECTOR, "#country")
    saveAddressBtn = (By.CSS_SELECTOR, ".action.save.primary")

    def __init__(self, driver):
        super().__init__(driver)

    def clickAddNewAddress(self):
        time.sleep(3)
        self.click(self.addNewAddress)
        time.sleep(4)

    def fillCredentials(self, firstName, lastName, company, tel, street, city, region, zip, country):
        self.fill_text(self.fName,firstName)
        self.fill_text(self.lName,lastName)
        self.fill_text(self.companyName,company)
        self.fill_text(self.telNumber,tel)

        country_dropdown_element = self.driver.find_element(*self.countryDropdown)
        self.selectCountry = Select(country_dropdown_element)
        self.selectCountry.select_by_visible_text(country)

        self.fill_text(self.streetEl, street)
        self.fill_text(self.cityEl, city)
        self.fill_text(self.regionEl, region)
        self.fill_text(self.zipEl, zip)

    def clickSaveAddress(self):
        self.click(self.saveAddressBtn)
        time.sleep(2)