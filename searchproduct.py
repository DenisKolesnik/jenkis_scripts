__author__ = 'QA_PC'

import unittest, xlrd
from selenium import  webdriver
from ddt import ddt, data, unpack

#def get_data(file_name):
    #rows = []
    #book = xlrd.open_workbook(file_name)
    #sheet = book.sheet_by_index(0)
    #for row_idx in range(1, sheet.nrows):
        #rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
    #return rows
@ddt
class SearchDDT(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get('http://www.cobra.ua/')

    @data(("iphone", 12))
    @unpack

    def test_search_by_category(self, search_value, expected_count):


        self.search_field = self.driver.find_element_by_id('search-field')
        self.search_field.clear()
        self.search_field.send_keys(search_value)
        self.search_field.submit()

        products = self.driver.find_elements_by_xpath('//div[1]/div[1]/section/div[3]/div[2]/div[@class="product"]')
        self.assertEqual(expected_count, len(products))
        if len(products) == expected_count:
            print('Passed#1')
        else:
            print('Test #1 failed')

    @data(("1/60014", 1))
    @unpack
    def test_search_by_name(self, search_value, expected_count):

        self.search_field = self.driver.find_element_by_id('search-field')
        self.search_field.clear()
        self.search_field.send_keys(search_value)
        self.search_field.submit()

        product =self.driver.find_elements_by_xpath('html/body/div[1]/div[1]/section/div[3]/div[2]/div[2]')

        self.assertEqual(expected_count, len(product))
        if len(product) == expected_count:
            print('Passed#2')
        else:
            print('Test #1 failed')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)












'''
# get the search textbox
search_field = driver.find_element_by_name("q")
search_field.clear()

# enter search keyword and submit
search_field.send_keys("phones")
search_field.submit()

# get all the anchor elements which have product names displayed
# currently on result page using find_elements_by_xpath method
products = driver.find_elements_by_xpath("//h2[@class='productname']/a")

# get the number of anchor elements found
print ("Found " + str(len(products)) + " products:")

# iterate through each anchor element and print the text that is
# name of the product
for product in products:
    print (product.text)

# close the browser window
driver.quit()
'''