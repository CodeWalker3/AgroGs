from time import sleep
from django.test import TestCase
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from AgroGs.users.tests.test_base_functional import UserBaseTest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsTest(StaticLiveServerTestCase, TestCase, UserBaseTest):
    
    def test_create_product(self):
        browser = self.make_login()
        browser.find_element(By.CLASS_NAME, "block-userlink").click()
        sleep(2)
        browser.find_element(By.XPATH, "/html/body/header/div/div[1]/div/div/div[3]/div/div[2]/div[2]/ul/li[1]/a").click()
        browser.find_element(By.CLASS_NAME, "tp-in-btn").click()
        browser.find_element(By.NAME, "name").send_keys("tomate")
        browser.find_element(By.NAME, "price").send_keys(12)
        browser.find_element(By.NAME, "quantity").send_keys(5)
        browser.find_element(By.CLASS_NAME, "nice-select").click()
        sleep(2)
        browser.find_element(By.XPATH, "/html/body/main/div/div/div/div/form/div[2]/div[3]/div[2]/ul/li[2]").click()
        descr = browser.find_element(By.XPATH, '//*[@id="id_description"]')
        descr.send_keys("tomate colhidos no campo")
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div/div/form/button"))
        )
        button.click()
        assert browser.current_url == "http://localhost:8000/products/list/"
        browser.quit()

    def test_edit_product(self):
        browser = self.make_login()
        browser.find_element(By.CLASS_NAME, "block-userlink").click()
        sleep(2)
        browser.find_element(By.XPATH, "/html/body/header/div/div[1]/div/div/div[3]/div/div[2]/div[2]/ul/li[1]/a").click()
        browser.find_element(By.XPATH, "/html/body/main/section/div[1]/div/table/tbody[1]/tr/td[4]/a[2]/i").click()
        browser.find_element(By.NAME, "name").send_keys("teste1")
        sleep(2)
        browser.execute_script("window.scrollTo(0, 780);")
        
        button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div/div/form/button"))
        )
        button.click()
        assert browser.current_url == "http://localhost:8000/products/list/"
        browser.quit()