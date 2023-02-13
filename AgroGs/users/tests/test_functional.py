from time import sleep
from AgroGs.users.tests.test_base_functional import UserBaseTest
from utils.browser import make_chrome_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class UsersTest(StaticLiveServerTestCase, UserBaseTest):

    def test_registration(self):
        browser = make_chrome_browser()
        browser.maximize_window()
        browser.get("http://localhost:8000/accounts/signup/")
        browser.find_element(By.NAME, "username").send_keys("teste")
        sleep(2)
        browser.find_element(By.NAME, "email").send_keys("teste@gmail.com")
        sleep(2)
        browser.find_element(By.NAME, "password1").send_keys("user12345")
        sleep(2)
        password = browser.find_element(By.NAME, "password2")
        password.send_keys("user12345")
        password.send_keys(Keys.RETURN)
        sleep(2)
        assert browser.current_url == "http://localhost:8000/"
        browser.quit()
 
    def test_login(self):
        browser = self.make_login()
        assert browser.current_url == "http://localhost:8000/"
        browser.quit()

    def test_become_seller(self):
        browser = self.become_seller()
        assert browser.current_url == "http://localhost:8000/"