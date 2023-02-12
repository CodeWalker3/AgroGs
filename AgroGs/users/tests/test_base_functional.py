from utils.browser import make_chrome_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class UserBaseTest:
    def make_login(self):
        browser = make_chrome_browser()
        browser.maximize_window()
        browser.get("http://localhost:8000/accounts/login/")
        browser.find_element(By.NAME, "login").send_keys("admin")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("admin")
        password.send_keys(Keys.RETURN)
        return browser