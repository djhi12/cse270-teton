# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


class TestSmokeside():
    # def setup_method(self, method):
    #   self.driver = webdriver.Chrome()
    #   self.vars = {}
    def setup_method(self, method):
        options = Options()
        options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=options)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_smokeside(self):
        self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
        self.driver.set_window_size(1408, 785)
        elements = self.driver.find_elements(
            By.CSS_SELECTOR, ".header-logo img")
        assert len(elements) > 0
        self.driver.find_element(By.ID, "nopad").click()
        elements = self.driver.find_elements(
            By.CSS_SELECTOR, ".header-title > h1")
        assert len(elements) > 0
        self.driver.find_element(By.CSS_SELECTOR, ".header-title > h2").click()
        elements = self.driver.find_elements(
            By.CSS_SELECTOR, ".header-title > h2")
        assert len(elements) > 0
        self.driver.find_element(By.CSS_SELECTOR, ".header-top").click()
        self.driver.find_element(By.CSS_SELECTOR, ".header-logo img").click()
        elements = self.driver.find_elements(By.LINK_TEXT, "Join Us")
        assert len(elements) > 0
        self.driver.find_element(By.ID, "nopad").click()
        self.driver.find_element(By.LINK_TEXT, "Directory").click()
        self.driver.find_element(By.ID, "directory-grid").click()
        elements = self.driver.find_elements(
            By.CSS_SELECTOR, ".gold-member:nth-child(9) > img")
        assert len(elements) > 0
        self.driver.find_element(By.ID, "directory-list").click()
        elements = self.driver.find_elements(
            By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)")
        assert len(elements) > 0
        self.driver.find_element(By.LINK_TEXT, "Join").click()
        elements = self.driver.find_elements(By.NAME, "fname")
        assert len(elements) > 0
        self.driver.find_element(By.NAME, "fname").send_keys("Daniel")
        self.driver.find_element(By.NAME, "lname").send_keys("Idorot")
        self.driver.find_element(By.NAME, "bizname").send_keys("BrightChamps")
        self.driver.find_element(By.NAME, "bizname").click()
        self.driver.find_element(By.NAME, "bizname").send_keys("ITS Hawaii")
        self.driver.find_element(By.NAME, "biztitle").click()
        self.driver.find_element(
            By.NAME, "biztitle").send_keys("SEO Specialist")
        self.driver.find_element(By.NAME, "submit").click()
        elements = self.driver.find_elements(By.NAME, "email")
        assert len(elements) > 0
        self.driver.find_element(By.NAME, "email").send_keys("sdsdsd")
        self.driver.find_element(By.NAME, "cellphone").click()
        self.driver.find_element(
            By.NAME, "cellphone").send_keys("202-303-2222")
        self.driver.find_element(By.NAME, "submit").click()
        self.driver.find_element(
            By.NAME, "email").send_keys("sdsdsd@yahoo.com")
        self.driver.find_element(By.NAME, "email").send_keys(Keys.ENTER)
        self.driver.find_element(By.LINK_TEXT, "Admin").click()
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").send_keys("djidorot")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("asdasdsadsa")
        self.driver.find_element(
            By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".errorMessage")
        assert len(elements) > 0
