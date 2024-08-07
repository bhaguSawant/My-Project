from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class KatalonRecorederDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_katalon_recoreder_demo(self):
        driver = self.driver
        driver.get(self.base_url + "chrome://newtab/")
        driver.get(
            "https://www.google.com/search?q=javatpoint&rlz=1C1YTUH_en&oq=javatpo&gs_lcrp=EgZjaHJvbWUqDggAEEUYJxg7GIAEGIoFMg4IABBFGCcYOxiABBiKBTIGCAEQRRg5MgYIAhBFGEAyCggDEAAYsQMYgAQyDwgEEAAYFBiHAhixAxiABDIHCAUQABiABDIMCAYQABgUGIcCGIAEMgYIBxBFGDyoAgiwAgE&sourceid=chrome&ie=UTF-8")
        driver.find_element_by_xpath("//div[@id='rso']/div/div/div/div/div/div/div/div/div/span/a/h3").click()
        driver.get("https://www.javatpoint.com/")
        driver.find_element_by_id("gsc-i-id1").click()
        driver.find_element_by_id("gsc-i-id1").clear()
        driver.find_element_by_id("gsc-i-id1").send_keys("python")
        driver.find_element_by_css_selector(".gsc-search-box").submit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()