import allure
import pytest
import time
from FinalProjectAutomation.pageobjects.CategoriesPage import CategoriesPage
from FinalProjectAutomation.pageobjects.CategoryPage import CategoryPage
from FinalProjectAutomation.pageobjects.CheckoutPage import CheckoutPage
from FinalProjectAutomation.pageobjects.ItemPage import ItemPage
from FinalProjectAutomation.pageobjects.ItemsPage import ItemsPage
from FinalProjectAutomation.pageobjects.LoginPage import LoginPage
from FinalProjectAutomation.utils.config import ConfigReader


class TestBuyProducts:

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

    @allure.description("Choosing the item , size and color")
    @allure.title("Choose Item1")
    def test_04_chooseItem1(self):
        itp = ItemsPage(self.driver)
        itp.chooseItem("Ariel Roll Sleeve Sweatshirt", "M", "Green")

    @allure.description("Choosing the item , size and color")
    @allure.title("Choose Item2")
    def test_05_chooseItem2(self):
        itp = ItemsPage(self.driver)
        itp.chooseItem("Phoebe Zipper Sweatshirt","XL", "Purple")

    @allure.description("Choosing the item , size and color")
    @allure.title("Choose Item3")
    def test_06_chooseItem3(self):
        itp = ItemsPage(self.driver)
        itp.chooseItem("Hera Pullover Hoodie","M", "Orange")

    @allure.title("Choose Category")
    def test_07_chooseCategory(self):
        cp = CategoriesPage(self.driver)
        cp.chooseCategory("Men")

    @allure.title("Choose Shop Category")
    def test_08_chooseShopCategory(self):
        cp = CategoryPage(self.driver)
        cp.chooseShopCategory("Bottoms")

    @allure.description("Choosing the item , size and color")
    @allure.title("Choose Item4")
    def test_09_chooseItem4(self):
        itp = ItemsPage(self.driver)
        itp.chooseItem("Lono Yoga Short","33", "Red")

    @allure.title("Choose Category")
    def test_10_chooseCategory(self):
        cp = CategoriesPage(self.driver)
        cp.chooseCategory("Gear")

    @allure.title("Choose Shop Category")
    def test_11_chooseCategory(self):
        cp = CategoryPage(self.driver)
        cp.chooseShopCategory("Fitness Equipment")

    @allure.title("Choose Item5")
    def test_012_chooseItem5(self):
        itp = ItemsPage(self.driver)
        itp.chooseItemNoDress("Quest Lumaflex™ Band")

    @allure.title("Go To Cart Page")
    def test_013_goToCartPage(self):
        itp = ItemPage(self.driver)
        itp.goToCartPage()

    @allure.title("Go To Checkout Page")
    def test_014_goToCheckoutPage(self):
        itp = ItemPage(self.driver)
        itp.goToCheckoutPage()

    @allure.title("Click The New Address")
    def test_015_newAddress(self):
        chp = CheckoutPage(self.driver)
        chp.clickNewAddress()

    @allure.title("Filling The Credentials")
    def test_16_fillCreChecklou(self):
        chp = CheckoutPage(self.driver)
        chp.fillCredentails("Nat", "Dav", "Intel", "Ako", "Jer", "15", "ako", "North","17362","Israel", "0546709393")
        chp.clickshipHere()
        time.sleep(2)

    @allure.title("Clicking Next Button")
    def test_017_clickNext(self):
        chp = CheckoutPage(self.driver)
        chp.clickNext()
        time.sleep(4)

    @allure.title("Clicking Place Order Button")
    def test_18_clickPlaceOrder(self):
        chp = CheckoutPage(self.driver)
        chp.clickPlaceOrder()

    @allure.title("Clicking To Continue Shopping")
    def test_18_clickContinueShop(self):
        chp = CheckoutPage(self.driver)
        chp.clickContinueShop()
        time.sleep(3600)