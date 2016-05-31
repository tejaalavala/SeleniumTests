# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re

class ALinks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://deanza.edu/"
        self.verificationErrors = []
    
    def test_a_links(self):
        link_title = {
            "Assessment Center (Placement Tests)" : "De Anza College :: Admissions and Records :: Assessment & Placement :: Home", 
            "Computer Access Lab" : "De Anza College :: Assistive Computer Technology :: Home",
            "Associate Degrees" : "De Anza College :: Counseling and Advising Center :: AA/AS Degree & Certificate Programs",
            "Associate Degree for Transfer (AA-T and AS-T)" : "De Anza College :: Transfer Planning :: SB1440 :: Home",
            "Astronomy Department" : "De Anza College :: Astronomy :: Home",
            "Athletics" : "De Anza College :: Athletics :: Welcome to Athletics",
            "Automotive Technology" : "De Anza College :: Automotive Technology Department :: What We Offer",
            "Awards and Achievements" : "De Anza College :: Awards and Achievements :: Home",
            }
        
        driver = self.driver
        driver.get(self.base_url + "directory/dir-az.html")

        for link in link_title:
            title = link_title[link]
            driver.find_element_by_link_text(link).click()
            try: self.assertEqual(title, driver.title)
            except AssertionError as e: self.verificationErrors.append(str(e))
            driver.back()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
