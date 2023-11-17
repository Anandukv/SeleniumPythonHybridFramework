from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class AccountSuccessPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    confirmation_message = "//div[@id='content']/h1"

    def retrieve_status_of_account_creation(self):
        return self.driver.find_element(By.XPATH, self.confirmation_message).text



