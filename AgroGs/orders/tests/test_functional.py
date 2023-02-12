from time import sleep
from AgroGs.core.tests.test_base_functional import CartBaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from AgroGs.users.models import Address, User


class OrdersTest(StaticLiveServerTestCase, CartBaseTest):

    def test_create_order(self):
        browser = self.add_to_cart()
        button = browser.find_element(By.XPATH, "/html/body/main/section/div/div/div/form/div[3]/div/div/a")
        browser.execute_script("arguments[0].scrollIntoView();", button)
        sleep(3)
        button.click()
        sleep(2)
        user = User.objects.filter(username="teste").first()
        if Address.objects.filter(user=user).exists() == True:
            browser.find_element(By.NAME, "street").send_keys("rua teste")
            browser.find_element(By.NAME, "compliment").send_keys("apartamento")
            browser.find_element(By.NAME, "number").send_keys(109)
            browser.find_element(By.NAME, "city").send_keys("Test Town")
            browser.find_element(By.NAME, "state").send_keys("RN")
            browser.find_element(By.NAME, "phone").send_keys("8895758855")
            button = browser.find_element(By.XPATH, "/html/body/main/section/div/form/div/div[2]/div/div[2]/div[2]/button")
            browser.execute_script("arguments[0].scrollIntoView();", button)
            sleep(3)
            button.click()
            assert browser.current_url == "http://localhost:8000/orders/list/"
            browser.quit()
            
        else:
            button = browser.find_element(By.XPATH, "/html/body/main/section/div/form/div/div[2]/div/div[2]/div[2]/button")
            browser.execute_script("arguments[0].scrollIntoView();", button)
            sleep(3)
            button.click()
            assert browser.current_url == "http://localhost:8000/orders/list/"
            browser.quit()


