import unittest
from selenium import webdriver

class TestWebsiteTitle(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.example.com")
    
    def test_title(self):
        expected_title = "Home Page"
        actual_title = self.driver.title
        self.assertEqual(expected_title, actual_title, "Title does not match expected value")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
