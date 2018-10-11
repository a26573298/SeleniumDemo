#!/usr/bin/python
# -*- coding: UTF-8 -*-
# python 中文編碼

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


def login(self):
    self.driver.get("https://play.kkbox.com/")
    self.driver.find_element_by_id("uid").clear()
    self.driver.find_element_by_id("pwd").clear()
    self.driver.find_element_by_id("uid").send_keys("mandyyang@kkbox.com")
    time.sleep(2)
    self.driver.find_element_by_id("pwd").send_keys("P299kkbox")
    time.sleep(2)
    self.driver.find_element_by_id("login-btn").send_keys(Keys.ENTER)
    time.sleep(2)
    # self.driver.quit()


class KkboxSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_artist(self):
        login(self)
        self.driver.find_element_by_id("lst-ib").send_keys("韋禮安")
        # 取得網頁所有程式碼(測試方法有錯，除了輸入框可能其他地方也會有韋禮安的字)
        """src = self.driver.page_source
        # 確認有無輸入韋禮安
        text_found = re.search(r"韋禮安", src)
        self.assertNotEqual(text_found, None)"""
        self.driver.find_element_by_id("lst-ib").send_keys(Keys.ENTER)
        #assert "No results found." not in driver.page_source
        self.driver.find_element_by_class_name("cards artists")
        assert "有所畏" not in self.driver.page_source
        

    def tearDown(self):
        self.driver.quit()

    """def IsElementDisplayed(self, element):
    	if (self.driver.FindElements(element).Count > 0):
            if (self.driver.FindElement(element).Displayed):
                return true
            else
                return false
        else
            return false"""

if __name__ == "__main__":
    unittest.main()