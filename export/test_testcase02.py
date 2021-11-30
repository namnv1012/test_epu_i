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

class TestTestcase02():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testcase02(self):
    self.driver.get("https://amisapp.misa.vn/login")
    self.driver.set_window_size(798, 824)
    self.driver.find_element(By.CSS_SELECTOR, ".wrap-login").click()
    self.driver.find_element(By.NAME, "pass").click()
    self.driver.find_element(By.CSS_SELECTOR, ".container-login").click()
    self.driver.find_element(By.NAME, "username").click()
    self.driver.find_element(By.NAME, "pass").click()
    self.driver.find_element(By.NAME, "pass").click()
    self.driver.find_element(By.NAME, "pass").send_keys("Nam101220000")
    self.driver.find_element(By.CSS_SELECTOR, ".login-form-btn").click()
  