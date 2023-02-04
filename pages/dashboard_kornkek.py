
import time
from lib2to3.pgen2 import driver

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

class Dashboard(BasePage):
    dashboard_url = ('https://scouts-test.futbolkolektyw.pl/en')
    expected_title = "Scouts panel"
    futbol_kol_button_xpath = '//*[@title ="Logo Scouts Panel"]'
    wait = WebDriverWait(driver, 10)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.futbol_kol_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

