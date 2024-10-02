import allure
import pytest
from FinalProjectAutomation.pageobjects.CategoriesPage import CategoriesPage
from FinalProjectAutomation.pageobjects.CategoryPage import CategoryPage
from FinalProjectAutomation.pageobjects.LoginPage import LoginPage
from FinalProjectAutomation.pageobjects.NewTab import NewTab
from FinalProjectAutomation.utils.config import ConfigReader


class TestNewTab:

    @allure.title("logging in")
    def test_01_login(self):
        lp = LoginPage(self.driver)
        email = ConfigReader.read_config("email", "email")
        password = ConfigReader.read_config("email", "password")
        lp.login(email, password)

    @allure.title("Choose Category")
    def test_02_chooseCategory(self):
        cp = CategoriesPage(self.driver)
        cp.chooseCategory("Men")

    @allure.title("Choose Shop Category")
    def test_03_chooseShopCategory(self):
        cp = CategoryPage(self.driver)
        cp.chooseShopCategory("Hoodies & Sweatshirts")

    @allure.description("opening it on new tab")
    @allure.title("Choosing item1")
    def test_04_clickForNewTab(self):
        nt = NewTab(self.driver)
        nt.clickItem("Grayson Crewneck Sweatshirt")

    @allure.description("opening it on new tab")
    @allure.title("Choosing item2")
    def test_05_clickForNewTab(self):
        nt = NewTab(self.driver)
        nt.clickItem("Hero Hoodie")