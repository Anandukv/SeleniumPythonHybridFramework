from selenium.webdriver.common.by import By
from Pages.AccountPage import AccountPage
from Pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    email_address_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    warning_message = "//div[@class='alert alert-danger alert-dismissible']"

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_field_id).click()
        self.driver.find_element(By.ID, self.password_field_id).clear()
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password)

    def enter_email_address(self, email):
        self.driver.find_element(By.ID, self.email_address_field_id).click()
        self.driver.find_element(By.ID, self.email_address_field_id).clear()
        self.driver.find_element(By.ID, self.email_address_field_id).send_keys(email)

    def click_on_login_buton(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
        return AccountPage(self.driver)

    def retrieve_warning_message(self):
        return self.driver.find_element(By.XPATH, self.warning_message).text

    def login_to_application(self, email, password):
        self.enter_email_address(email)
        self.enter_password(password)
        return self.click_on_login_buton()

