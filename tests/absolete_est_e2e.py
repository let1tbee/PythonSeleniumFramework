import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass

from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage


#@pytest.mark.usefixtures("setup") # this one is removed to BaseClass to keep this code cleaner
class TestOne(BaseClass):

    def test_e2e(self):
        """

        #This is fixture (conftest: setup)
        driver = webdriver.Chrome()
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.implicitly_wait(5)

        """

        #divide code for 3 classes - each for separate page

        # ***Homepage
        """
        
        # XPATH //a[contains)@href,'shop')]   CSS a[href&='shop']
        self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click() #method in the HomePage class
        
        """
        home_page = HomePage(self.driver)
        checkout_page = home_page.shopItems()

        # ***Checkoutpage
        """
        list = self.driver.find_elements(By.CLASS_NAME, "h-100")

        for item in list:
            if item.find_element(By.CLASS_NAME, "card-title").text == "Blackberry":
                item.find_element(By.CLASS_NAME, "btn").click()
                break

        self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        
        """
        list = checkout_page.listOfItems()

        for item in list:
            if checkout_page.itemCard(item).text == "Blackberry":
                checkout_page.btnCard(item).click()
                break

        checkout_page.pressBTN1().click()
        confirm_page = checkout_page.pressBTN2()

        # ***Confirmpage
        """
        self.driver.find_element(By.ID, "country").send_keys("uk")
        wait = WebDriverWait(self.driver, 10)  # creates waiting timeout
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[text()='Ukraine']")))
        self.driver.find_element(By.XPATH, "//a[text()='Ukraine']").click()

        self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        self.driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-success alert-dismissible']")))

        text = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        """


        confirm_page.countryID().send_keys("uk")
        self.initWaiting()
        self.waiting(confirm_page.countryName())
        confirm_page.countryBTN().click()

        confirm_page.pressConfBTN1().click()
        confirm_page.pressConfBTN2().click()

        self.waiting(confirm_page.assertGet())
        text = confirm_page.assertionMes().text

        assert "Success! Thank you!" in text

        time.sleep(2)
