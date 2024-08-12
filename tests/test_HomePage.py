import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage

from TestData.HomePageData import HomePageData


class TestHomePage(BaseClass):

    def test_formSubmition(self, getData):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        home_page.getEmail().send_keys(getData["Email"])
        home_page.getPass().send_keys(getData["Password"])
        home_page.getCheck().click()

        self.selectDrop(home_page.getDrop(), getData["Gender "])

        home_page.getName().send_keys(getData["Name"])
        log.info("All data has been filled in")
        home_page.getSub().click()

        text = home_page.getAssert().text  # text parcing
        print(text)

        assert "Success" in text  # check presence of specific word in the string
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase1"))
    def getData(self, request):
        return request.param
