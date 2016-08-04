__author__ = 'QA_PC'
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from xmlrunner import xmlrunner

class SearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://asos.com")

    def test_search(self):
        driver = self.driver
        search_field = driver.find_element_by_id("txtSearch")
        search_field.send_keys("text")

        go_button = driver.find_element_by_class_name("go")
        go_button.click()

        products = driver.find_elements_by_css_selector("#productlist-results > div > div.results.three-grid > ul > li:nth-child(1)")
        assert len(products) > 0

        if len(products) > 0:
            print("More than null")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)


