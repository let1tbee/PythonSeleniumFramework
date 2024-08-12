from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    country_ID = (By.ID, "country")
    country_name = (By.XPATH, "//a[text()='Ukraine']")
    btn1 = (By.XPATH, "//label[@for='checkbox2']")
    btn2 = (By.XPATH, "//input[@class='btn btn-success btn-lg']")
    assert1 = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def countryID(self):
        return self.driver.find_element(*self.country_ID)

    def countryName(self):
        return self.country_name

    def countryBTN(self):
        return self.driver.find_element(*self.country_name)

    def pressConfBTN1(self):
        return self.driver.find_element(*self.btn1)

    def pressConfBTN2(self):
        return self.driver.find_element(*self.btn2)

    def assertGet(self):
        return self.assert1

    def assertionMes(self):
        return self.driver.find_element(*self.assert1)
