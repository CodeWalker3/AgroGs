from time import sleep
from django.test import TestCase
from AgroGs.users.tests.test_base_functional import UserBaseTest
from utils.browser import make_chrome_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class UsersTest(StaticLiveServerTestCase, TestCase, UserBaseTest):

    def test_registration(self):
        browser = make_chrome_browser()
        browser.get("http://localhost:8000/accounts/signup/")
        browser.find_element(By.NAME, "username").send_keys("teste")
        browser.find_element(By.NAME, "email").send_keys("teste@gmail.com")
        browser.find_element(By.NAME, "password1").send_keys("user12345")
        password = browser.find_element(By.NAME, "password2")
        password.send_keys("user12345")
        password.send_keys(Keys.RETURN)
        assert browser.current_url == "http://localhost:8000/"
        browser.quit()
 
    def test_login(self):
        browser = self.make_login()
        assert browser.current_url == "http://localhost:8000/"
        browser.quit()

    def test_become_seller(self):
        browser = self.become_seller()
        assert browser.current_url == "http://localhost:8000/"