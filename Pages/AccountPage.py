from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    edit_your_account_information_option = "Edit your account information"

    def display_status_of_account_creation(self):
        return self.driver.find_element(By.LINK_TEXT, self.edit_your_account_information_option).is_displayed()