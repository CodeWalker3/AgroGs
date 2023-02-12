from time import sleep
from AgroGs.users.tests.test_base_functional import UserBaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CartBaseTest(UserBaseTest):
    def add_to_cart(self):
        browser = self.make_login()
        browser.execute_script("window.scrollTo(0, 850);")
        sleep(2)
        browser.find_element(By.XPATH, "/html/body/main/section[2]/div/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/a").click()
        browser.find_element(By.XPATH, "/html/body/main/div/div/div/div[2]/div/div[5]/a").click()
        return browser
