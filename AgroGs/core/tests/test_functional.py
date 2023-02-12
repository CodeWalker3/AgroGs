from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from AgroGs.core.tests.test_base_functional import CartBaseTest


class CartTest(StaticLiveServerTestCase, CartBaseTest):
    
    def test_add_to_cart(self):
        browser = self.add_to_cart()
        assert browser.current_url == "http://localhost:8000/cart/"
        browser.quit()

    def test_remove_from_cart(self):
        browser = self.add_to_cart()
        browser.find_element(By.XPATH, "/html/body/main/section/div/div/div/form/div[1]/table/tbody/tr/td[6]/a").click()
        assert browser.current_url == "http://localhost:8000/cart/"
        browser.quit()