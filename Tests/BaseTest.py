import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
