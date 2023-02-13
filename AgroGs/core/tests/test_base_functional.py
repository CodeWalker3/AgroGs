from time import sleep
from AgroGs.users.tests.test_base_functional import UserBaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CartBaseTest(UserBaseTest):
    def add_to_cart(self):
        browser = self.make_login()
        sleep(3)
        browser.find_element(By.XPATH, "/html/body/header/div/div[2]/div/div/div[2]/div/div[2]/nav/ul/li[2]/a").click()
        sleep(3)
        browser.find_element(By.XPATH, "/html/body/main/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div[3]/a").click()
        sleep(3)
        return browser
