from time import sleep
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from AgroGs.users.tests.test_base_functional import UserBaseTest


class ProductsTest(StaticLiveServerTestCase, UserBaseTest):
    
    def test_create_product(self):
        browser = self.become_seller()
        browser.find_element(By.CLASS_NAME, "block-userlink").click()
        sleep(2)
        browser.find_element(By.XPATH, "/html/body/header/div/div[1]/div/div/div[3]/div/div[2]/div[2]/ul/li[1]/a").click()
        browser.find_element(By.CLASS_NAME, "tp-in-btn").click()
        browser.find_element(By.NAME, "name").send_keys("tomate")
        browser.find_element(By.NAME, "price").send_keys(12)
        browser.find_element(By.NAME, "image").send_keys("C:/Projeto Integrador/Integador 3 2023/AgroGs/AgroGs/static/assets/img/tomate.jpg")
        browser.find_element(By.NAME, "quantity").send_keys(5)
        browser.find_element(By.CLASS_NAME, "nice-select").click()
        sleep(2)
        browser.find_element(By.XPATH, "/html/body/main/div/div/div/div/form/div[2]/div[3]/div[2]/ul/li[2]").click()
        descr = browser.find_element(By.XPATH, '//*[@id="id_description"]')
        descr.send_keys("tomate colhidos no campo")
        button = browser.find_element(By.XPATH, "/html/body/main/div/div/div/div/form/button")
        browser.execute_script("arguments[0].scrollIntoView();", button)
        sleep(3)
        button.click()
        assert browser.current_url == "http://localhost:8000/products/list/"
        browser.quit()

    def test_edit_product(self):
        browser = self.become_seller()
        browser.find_element(By.CLASS_NAME, "block-userlink").click()
        sleep(2)
        browser.find_element(By.XPATH, "/html/body/header/div/div[1]/div/div/div[3]/div/div[2]/div[2]/ul/li[1]/a").click()
        browser.find_element(By.XPATH, "/html/body/main/section/div[1]/div/table/tbody[1]/tr/td[4]/a[2]/i").click()
        browser.find_element(By.NAME, "name").send_keys("teste1")
        sleep(2)
        button = browser.find_element(By.XPATH, "/html/body/main/div/div/div/div/form/button")
        browser.execute_script("arguments[0].scrollIntoView();", button)
        sleep(3)
        button.click()
        assert browser.current_url == "http://localhost:8000/products/list/"
        browser.quit()