from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import csv

class Browse(unittest.TestCase):
 def setUp(self):
    self.driver = webdriver.Firefox()
    self.driver.implicitly_wait(30)
    self.base_url = "http://google.com/"

    filename = 'test.csv'
    my_fieldnames = ['col' + str(i) for i in range(1,26)]
#line_number = 1
    with open(filename, 'rb') as f:
      mycsv = csv.reader(f,fieldnames=my_fieldnames,
                               delimiter=',', dialect=csv.excel,
                               quoting=csv.QUOTE_NONE)
      for self in mycsv:    
        mycsv = list(mycsv)
        self.cityname=mycsv[line_number][0]
        self.username=mycsv[line_number][1]
        self.password=mycsv[line_number][2]
        self.verificationErrors = []

def test_browse(self):
    driver = self.driver
    driver.get(self.base_url + "/")
    driver.find_element_by_id("gbqfq").send_keys(self.cityname)
    result = driver.find_elements_by_xpath("//ol[@id='rso']/li")[0] 
    result.find_element_by_xpath("./div/h3/a").click()
    #driver.find_elements_by_xpath(".//*[@id='rso']//div//h3/a")[:1].click()
    driver.find_elements_by_xpath("//div[@id='jjj']//a[.='jobs']").click()
    driver.find_elements_by_xpath("//div[@id='ef']//a[.='post']").click()
    driver.find_elements_by_xpath("//aside[@id='accountBlurb']//a[normalize-space(.)='log in to your account']").click()
    driver.find_elements_by_xpath("//section[@id='loginBox']/p[1]/input").send_keys(self.loginemail)
    driver.find_elements_by_xpath("//section[@id='loginBox']/p[2]/input").send_keys(self.loginpass)
    driver.find_elements_by_xpath("//section[@id='loginBox']//button[.='Log In']").click()
    driver.find_elements_by_xpath("//section[@class='body']/form/blockquote/label[1]/input").click()
    driver.find_elements_by_xpath("//div[@class='formnote']/form/button").click()
    driver.find_elements_by_xpath("//section[@class='body']/form/blockquote/label[2]/input").click()
    driver.find_elements_by_xpath("//section[@class='body']//button[.='continue']").click()
    driver.find_element_by_id("PostingTitle").send_keys(self.ptitle)
    driver.find_element_by_id("GeographicArea").send_keys(self.geolocation)
    driver.find_element_by_id("PostingBody").send_keys(self.pcontent)
    driver.find_element_by_id("FromEMail").send_keys(self.FromEMail)
    driver.find_elements_by_xpath("//form[@id='postingForm']/div/div[3]/div[1]/input[2]").send_keys(self.vFromEMail)
    driver.find_elements_by_xpath("//form[@id='postingForm']/div/div[4]/div/p/input").send_keys(self.compensation)
    driver.find_elements_by_xpath("//form[@id='postingForm']//button[.='continue']").click()
    driver.find_elements_by_xpath("//form[@id='postingForm']//button[.='continue']").click()
    driver.find_elements_by_xpath("//div[@class='addmore']/form/input[3]").send_keys(self.photo)
    driver.find_elements_by_xpath("//section[@class='body']//button[.='done with images']").click()
    driver.find_elements_by_xpath("//section[@id='previewButtons']//button[.='publish']").click()

def is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except NoSuchElementException, e: return False
    return True

def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)