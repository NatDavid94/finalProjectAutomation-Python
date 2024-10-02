import allure
import pytest

import time
from FinalProjectAutomation.pageobjects.CategoriesPage import CategoriesPage
from FinalProjectAutomation.pageobjects.CategoryPage import CategoryPage
from FinalProjectAutomation.pageobjects.CheckoutPage import CheckoutPage
from FinalProjectAutomation.pageobjects.ChooseItem import ChooseItem
from FinalProjectAutomation.pageobjects.ItemPage import ItemPage
from FinalProjectAutomation.pageobjects.LoginPage import LoginPage
from FinalProjectAutomation.utils.config import ConfigReader


class TestBuyProduct:

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
        cp.chooseShopCategory("Jackets")

    @allure.title("Choose Item")
    def test_04_chooseItem(self):
        ci = ChooseItem(self.driver)
        ci.chooseItem("Mars HeatTech™ Pullover")

    @allure.title("Choose Item Size")
    def test_05_chooseSizeItem(self):
        itp = ItemPage(self.driver)
        itp.chooseSize("L")


    @allure.title("Choose Item Color")
    def test_06_chooseColorItem(self):
        itp = ItemPage(self.driver)
        itp.chooseColor("Black")

    @allure.description("Adding the item to cart")
    @allure.title("Add To Cart")
    def test_07_addToCart(self):
        itp = ItemPage(self.driver)
        itp.addToCart()

    @allure.title("Go To Cart Page")
    def test_08_goToCartPag(self):
        itp = ItemPage(self.driver)
        itp.goToCartPage()

    @allure.title("Go To Checkout Page")
    def test_09_goToCheckoutPageg(self):
        itp = ItemPage(self.driver)
        itp.goToCheckoutPage()

    @allure.title("Click The New Address")
    def test_10_newAddress(self):
        chp = CheckoutPage(self.driver)
        chp.clickNewAddress()

    @allure.title("Filling The Credentials")
    def test_11_fillCredentials(self):
        chp = CheckoutPage(self.driver)
        chp.fillCredentails("Nat", "Dav", "Intel", "Ako", "Jer", "15", "ako", "North","17362","Israel", "0546709393")
        chp.clickshipHere()
        time.sleep(2)

    @allure.title("Clicking Next Button")
    def test_12_clickNext(self):
        chp = CheckoutPage(self.driver)
        chp.clickNext()
        time.sleep(4)

    @allure.title("Clicking Place Order Button")
    def test_13_clickPlaceOrder(self):
        chp = CheckoutPage(self.driver)
        chp.clickPlaceOrder()

    @allure.title("Clicking To Continue Shopping")
    def test_14_clickContinueShop(self):
        chp = CheckoutPage(self.driver)
        chp.clickContinueShop()
