from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']") #creating taple to hot reach to selectors
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    check = (By.ID, "exampleCheck1")
    dropdown = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    assertionMes = (By.CLASS_NAME, "alert-success")
    def shopItems(self):
        #self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        self.driver.find_element(*self.shop).click() # put * to open the taple (otherwise it will come with gaps)
        checkout_page = CheckoutPage(self.driver)
        return checkout_page #return class object

    def getEmail(self):
        return self.driver.find_element(*self.email)

    def getPass(self):
        return self.driver.find_element(*self.password)

    def getCheck(self):
        return self.driver.find_element(*self.check)

    def getDrop(self):

        return self.driver.find_element(*self.dropdown)

    def getName(self):
        return self.driver.find_element(*self.name)

    def getSub(self):
        return self.driver.find_element(*self.submit)

    def getAssert(self):
        return self.driver.find_element(*self.assertionMes)