import time

import allure
import pytest

from FinalProjectAutomation.pageobjects.CartPage import CartPage
from FinalProjectAutomation.pageobjects.CategoriesPage import CategoriesPage
from FinalProjectAutomation.pageobjects.CategoryPage import CategoryPage
from FinalProjectAutomation.pageobjects.ItemPage import ItemPage
from FinalProjectAutomation.pageobjects.ItemsPage import ItemsPage
from FinalProjectAutomation.pageobjects.LoginPage import LoginPage
from FinalProjectAutomation.pageobjects.SignOutPage import SignOutPage
from FinalProjectAutomation.utils.config import ConfigReader


class TestFillCart:

    allProducts = []

    @allure.title("logging in")
    def test_01_login(self):
        lp = LoginPage(self.driver)
        email = ConfigReader.read_config("email", "email")
        password = ConfigReader.read_config("email", "password")
        lp.login(email, password)

    @allure.title("Choose Category")
    def test_02_chooseCategory(self):
        cp = CategoriesPage(self.driver)
        cp.chooseCategory("Women")

    @allure.title("Choose Shop Category")
    def test_03_chooseShopCategory(self):
        cp = CategoryPage(self.driver)
        cp.chooseShopCategory("Hoodies & Sweatshirts")

    @allure.description("Choosing the item , size and color and adding the details to productInfo list ")
    @allure.title("Choose Item1")
    def test_04_chooseItem1(self):
        productInfo = []

        itp = ItemsPage(self.driver)
        itp.chooseItem("Ariel Roll Sleeve Sweatshirt", "M", "Green")

        productInfo.append("Product Name: Ariel Roll Sleeve Sweatshirt")
        productInfo.append("Size: M")
        productInfo.append("Color: Green")
        self.allProducts.append(productInfo)

    @allure.description("Choosing the item , size and color and adding the details to productInfo list ")
    @allure.title("Choose Item2")
    def test_05_chooseItem2(self):
        productInfo = []

        itp = ItemsPage(self.driver)
        itp.chooseItem("Phoebe Zipper Sweatshirt","XL", "Purple")

        productInfo.append("Product Name: Phoebe Zipper Sweatshirt")
        productInfo.append("Size: XL")
        productInfo.append("Color: Purple")
        self.allProducts.append(productInfo)

    @allure.description("Choosing the item , size and color and adding the details to productInfo list ")
    @allure.title("Choose Item3")
    def test_06_chooseItem3(self):
        productInfo = []

        itp = ItemsPage(self.driver)
        itp.chooseItem("Hera Pullover Hoodie","M", "Orange")

        productInfo.append("Product Name: Hera Pullover Hoodie")
        productInfo.append("Size: M")
        productInfo.append("Color: Orange")
        self.allProducts.append(productInfo)

    @allure.title("Choose Category")
    def test_07_chooseCategory(self):
        cp = CategoriesPage(self.driver)
        cp.chooseCategory("Men")

    @allure.title("Choose Shop Category")
    def test_08_chooseShopCategory(self):
        cp = CategoryPage(self.driver)
        cp.chooseShopCategory("Bottoms")

    @allure.description("Choosing the item , size and color and adding the details to productInfo list ")
    @allure.title("Choose Item4")
    def test_09_chooseItem4(self):
        productInfo = []

        itp = ItemsPage(self.driver)
        itp.chooseItem("Lono Yoga Short","33", "Red")

        productInfo.append("Product Name: Lono Yoga Short")
        productInfo.append("Size: 33")
        productInfo.append("Color: Red")
        self.allProducts.append(productInfo)

    @allure.title("Choose Category")
    def test_10_chooseCategory(self):
        cp = CategoriesPage(self.driver)
        cp.chooseCategory("Gear")

    @allure.title("Choose Shop Category")
    def test_11_chooseCategory(self):
        cp = CategoryPage(self.driver)
        cp.chooseShopCategory("Fitness Equipment")

    @allure.description("Choosing the item , and adding the details to productInfo list ")
    @allure.title("Choose Item5")
    def test_012_chooseItem5(self):
        productInfo = []

        itp = ItemsPage(self.driver)
        itp.chooseItemNoDress("Quest Lumaflex™ Band")

        productInfo.append("Product Name: Quest Lumaflex™ Band")
        self.allProducts.append(productInfo)

    @allure.title("Clicing signout")
    def test_013_signoutFromAcoount(self):

        sgo = SignOutPage(self.driver)
        sgo.clickSignOut()

    @allure.title("logging in")
    def test_14_login(self):
        lp = LoginPage(self.driver)
        email = ConfigReader.read_config("email", "email")
        password = ConfigReader.read_config("email", "password")
        lp.login(email, password)

    @allure.title("Go to cart page")
    def test_015_goToCartPage(self):
        itp = ItemPage(self.driver)
        itp.goToCartPage()

    @allure.description("Viewing the all the item on the cart and compare with the items that had added")
    @allure.title("View the cart page")
    def test_016_viewCartPage(self):
        crp = CartPage(self.driver)
        crp.clickViewCartPage()
        crp.compareItemsNames(self.allProducts)