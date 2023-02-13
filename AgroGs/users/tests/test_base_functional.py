from utils.browser import make_chrome_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class UserBaseTest:
    def make_login(self):
        browser = make_chrome_browser()
        browser.maximize_window()
        browser.get("http://localhost:8000/accounts/login/")
        browser.find_element(By.NAME, "login").send_keys("teste")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("user12345")
        password.send_keys(Keys.RETURN)
        return browser

    def become_seller(self):
        browser = self.make_login()
        browser.find_element(By.XPATH, "/html/body/header/div/div[2]/div/div/div[2]/div/div[2]/nav/ul/li[4]/a").click()
        cnpj = browser.find_element(By.XPATH, '//*[@id="id_cnpj"]')
        cnpj.send_keys("06.740.070/0001-62")
        cnpj.send_keys(Keys.RETURN)
        return browser   