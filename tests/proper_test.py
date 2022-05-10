from selenium import webdriver
import unittest
from page_objects import main_page, register_page
from page_objects import support_functions


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.url = 'https://fabrykatestow.pl'
        self.driver.get(self.url)
        self.driver.set_window_size(1920,1080)

    def tearDown(self):
        self.driver.quit()

    def test1_almost_join_newsletter(self):
        main_page.click_newsletter_button(self.driver)
        support_functions.save_window_after(self.driver)
        # self.assertTrue(support_functions.check_current_url(self.driver, register_page.url))
        self.assertTrue(register_page.submit_register_to_newsletter_button_visible(self.driver))
