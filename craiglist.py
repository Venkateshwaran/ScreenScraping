#Python 2.6
from selenium import selenium
import unittest, time, re, csv, logging

class Untitled(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*firefox", "http://www.google.com")
        self.selenium.start()

    def test_untitled(self):
        sel = self.selenium
        spamReader = csv.reader(open('your_file.csv'))
        for row in spamReader:
            sel.open(row[0])
            sel.wait_for_page_to_load("30000")
            print sel.get_html_source()

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()