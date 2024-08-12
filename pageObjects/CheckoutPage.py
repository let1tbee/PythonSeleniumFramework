from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    list = (By.CLASS_NAME, "h-100") #creating taple to hot reach to selectors
    card_title = (By.CLASS_NAME, "card-title")
    btn_card = (By.CLASS_NAME, "btn")
    btn1 = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    btn2 = (By.XPATH, "//button[@class='btn btn-success']")

    def listOfItems(self):
        #self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        return self.driver.find_elements(*CheckoutPage.list) # put * to open the taple (otherwise it will come with gaps)

    def itemCard(self, item):
        return item.find_element(*CheckoutPage.card_title)

    def btnCard(self, item):
        return item.find_element(*CheckoutPage.btn_card)

    def pressBTN1(self):
        return self.driver.find_element(*CheckoutPage.btn1)

    def pressBTN2(self):
        self.driver.find_element(*CheckoutPage.btn2).click()
        confirm_page =ConfirmPage(self.driver)
        return confirm_page