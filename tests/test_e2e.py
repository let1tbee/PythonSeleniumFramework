import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass

from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        checkout_page = home_page.shopItems()
        log.info("Getting card titles")
        list = checkout_page.listOfItems()

        for item in list:
            if checkout_page.itemCard(item).text == "Blackberry":
                checkout_page.btnCard(item).click()
                break

        checkout_page.pressBTN1().click()
        confirm_page = checkout_page.pressBTN2()


        confirm_page.countryID().send_keys("uk")
        self.initWaiting()
        self.waiting(confirm_page.countryName())
        confirm_page.countryBTN().click()
        log.info("Entering country name")
        confirm_page.pressConfBTN1().click()
        confirm_page.pressConfBTN2().click()
        log.info("Waiting for page to process")
        self.waiting(confirm_page.assertGet())
        text = confirm_page.assertionMes().text
        log.info("Text copied")
        assert "Success! Thank you!" in text

        time.sleep(2)
