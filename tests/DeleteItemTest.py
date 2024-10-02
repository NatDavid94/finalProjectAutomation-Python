import allure
import pytest
from FinalProjectAutomation.pageobjects.CartPage import CartPage
from FinalProjectAutomation.pageobjects.ItemPage import ItemPage
from FinalProjectAutomation.pageobjects.LoginPage import LoginPage
from FinalProjectAutomation.utils.config import ConfigReader


class TestDeleteItem:

    @allure.title("logging in")
    def test_01_login(self):
        lp = LoginPage(self.driver)
        email = ConfigReader.read_config("email", "email")
        password = ConfigReader.read_config("email", "password")
        lp.login(email, password)

    @allure.title("Going To Cart Page")
    def test_02_goToCartPage(self):
        itp = ItemPage(self.driver)
        itp.goToCartPage()

    @allure.title("Going To Cart Page")
    def test_03_viewCartPage(self):
        crp = CartPage(self.driver)
        crp.clickViewCartPage()

    @allure.title("Deleting the items")
    def test_04_deleteItems(self):
        crp = CartPage(self.driver)
        crp.deleteItems()

