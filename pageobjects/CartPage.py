from selenium.webdriver.common.by import By
import time
from FinalProjectAutomation.pageobjects.BasePage import BasePage


class CartPage(BasePage):

    viewCartBtn = (By.CSS_SELECTOR, ".action.viewcart")
    deleteItemBtn = (By.CSS_SELECTOR, ".action.action-delete")

    def __init__(self, driver):
        super().__init__(driver)
        self.all_products = []

    def clickViewCartPage(self):
        self.click(self.viewCartBtn)
        time.sleep(2)

    def compareItemsNames(self, allProductsAdded):
        itemNamesList = self.driver.find_elements(By.CSS_SELECTOR, ".item-info .product-item-name")

        time.sleep(2)
        countInt = 3  # count of element start with '3'

        # adding the item's product list to list - allProducts
        for item in itemNamesList:
            countStr = str(countInt)
            print(countStr)
            itemEl = "#shopping-cart-table > tbody:nth-child(" + countStr + ") > tr.item-info > td.col.item > div"
            valueEl = itemEl + " dl.item-options dd"  # list of values

            productInfo = ["Product Name: " + item.text]  # create list of product

            #  create list of values for example : M(size) , Red(Color)
            valuesList = self.driver.find_elements(By.CSS_SELECTOR,valueEl)

            # There are items that don't have size and color
            if valuesList:
                productInfo.append("Size: " + valuesList[0].text)
                productInfo.append("Color: " + valuesList[1].text)


            # add the product to products list
            self.all_products.append(productInfo)

            countInt += 1  # increasing counter

        # print allProducts list
        #print(self.all_products)

        #print(allProductsAdded)

        print("--------self.all_products-----------")
        for product in self.all_products:
            for info in product:
                print(info)
            print("----------------------")

        print("\n\n----------allProductsAdded-----------")
        for product in allProductsAdded:
            for info in product:
                print(info)
            print("----------------------")



        # sort the allProductsAdded that we got as a parameter
        allProductsAdded.sort(key=lambda product: product[0])

        # sort the allProducts that we create now
        self.all_products.sort(key=lambda product: product[0])

        # *** testing ***
        # comparing between the lists
        assert allProductsAdded == self.all_products, "The lists do not match"

    def deleteItems(self):
        deleteItemList = self.driver.find_elements(By.CSS_SELECTOR, ".action.action-delete")
        size_of_list = len(deleteItemList)

        for i in range(size_of_list):
            self.click(self.deleteItemBtn)
            time.sleep(5)




