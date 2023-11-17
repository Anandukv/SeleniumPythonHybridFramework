from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    product_HP_link_text = "HP LP3065"

    def display_status_of_product(self):
        return self.driver.find_element(By.LINK_TEXT, self.product_HP_link_text).is_displayed()

    def retrieve_no_product_message(self):
        return self.driver.find_element(By.XPATH, "//input[@id='button-search']//following-sibling::p").text

