import allure
import pytest
from FinalProjectAutomation.pageobjects.DeleteAddress import DeleteAddress
from FinalProjectAutomation.pageobjects.LoginPage import LoginPage
from FinalProjectAutomation.pageobjects.NewAddress import NewAddress
from FinalProjectAutomation.utils.config import ConfigReader


class TestNewAddress:

    @allure.title("logging in")
    def test_01_login(self):
        lp = LoginPage(self.driver)
        email = ConfigReader.read_config("email", "email")
        password = ConfigReader.read_config("email", "password")
        lp.login(email, password)

    @allure.title("Go to address page")
    def test_02_goToAddresse(self):
        da = DeleteAddress(self.driver)
        da.goToAdrressPage()

    @allure.title("Clicking new address button")
    def test_03_clickNewAddress(self):
        na = NewAddress(self.driver)
        na.clickAddNewAddress()

    @allure.title("Filling the credentials")
    def test_04_fillCredentials(self):
        na = NewAddress(self.driver)
        na.fillCredentials("Nat","Dav","Philips","050-62648324","Burla","Haifa","North","753264","Israel")

    @allure.title("Clicking save address button")
    def test_05_clickSaveAddress(self):
        na = NewAddress(self.driver)
        na.clickSaveAddress()