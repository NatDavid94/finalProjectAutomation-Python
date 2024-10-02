import allure
import pytest
from FinalProjectAutomation.pageobjects.DeleteAddress import DeleteAddress
from FinalProjectAutomation.pageobjects.LoginPage import LoginPage
from FinalProjectAutomation.utils.config import ConfigReader


class TestDeleteAddress:

    @allure.title("logging in")
    def test_01_login(self):
        lp = LoginPage(self.driver)
        email = ConfigReader.read_config("email", "email")
        password = ConfigReader.read_config("email", "password")
        lp.login(email, password)

    @allure.title("Go Addresses Page")
    def test_02_goToAddresses(self):
        da = DeleteAddress(self.driver)
        da.goToAdrressPage()

    @allure.title("Deleting All Addresses")
    def test_03_delAddresses(self):
        da = DeleteAddress(self.driver)
        da.deleteAdress()