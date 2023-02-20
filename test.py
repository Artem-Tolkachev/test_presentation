import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Reg(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def test(self):
        driver = self.driver
        driver.get("https://ya.ru/")
        driver.set_window_size(1920, 1024)

        submit_button = driver.find_element(By.CSS_SELECTOR, ".headline__personal-enter")
        submit_button.click()
        time.sleep(1)

        submit_button = driver.find_element(By.CSS_SELECTOR, ".Button2_size_l.Button2_view_clear")
        submit_button.click()
        time.sleep(1)

        textarea = driver.find_element(By.ID, "passp-field-phone")
        textarea.send_keys("9018004411")
        time.sleep(1)

        submit_button = driver.find_element(By.CSS_SELECTOR, ".Button2_size_l.Button2_view_action.Button2_width_max.Button2_type_submit")
        submit_button.click()
        time.sleep(2)

        driver.back()

    def test_bar(self):
        driver = self.driver
        driver.get("https://ya.ru/")
        driver.set_window_size(1920, 1024)

        submit_button = driver.find_element(By.CLASS_NAME, "services-pinned__item.services-pinned__add.services-pinned__close-focus")
        submit_button.click()
        time.sleep(1)

        textarea = driver.find_element(By.CLASS_NAME, "services-pinned__popup-search")
        textarea.send_keys("Почта")
        time.sleep(1)

        submit_button = driver.find_element(By.CLASS_NAME, "home-link2.headline__logo")
        submit_button.click()
        time.sleep(1)

        submit_button = driver.find_element(By.CLASS_NAME, "services-pinned__all")
        submit_button.click()
        time.sleep(1)

        submit_button = driver.find_element(By.CLASS_NAME, "services-more-popup__magnifier")
        submit_button.click()
        time.sleep(1)

        textarea = driver.find_element(By.CLASS_NAME, "services-more-popup__search")
        textarea.send_keys("Карты")
        time.sleep(1)

        submit_button = driver.find_element(By.LINK_TEXT, "Карты")
        submit_button.click()
        time.sleep(1)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":

    unittest.main()