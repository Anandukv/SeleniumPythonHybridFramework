from selenium.webdriver.common.by import By
from Pages.AccountSuccessPage import AccountSuccessPage
from Pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    firstname = "input-firstname"
    lastname = "input-lastname"
    email = "input-email"
    telephone = "input-telephone"
    password = "input-password"
    pass_confirm = "input-confirm"
    agree_policy = "agree"
    yes = "//input[@name='newsletter'][@value='1']"
    confirmation_msg_xpath = "//div[@id='content']/h1"
    continue_button_xpath = "//input[@value='Continue']"
    duplicate_email_warning = "//div[@id='account-register']/div[1]"
    policy_warning_message ="//div[@id='account-register']/div[1]"
    firstname_warning_message ="//input[@name='firstname']//following-sibling::div"
    lastname_warning_message ="//input[@name='lastname']//following-sibling::div"
    email_warning_message = "//input[@name='email']//following-sibling::div"
    telephone_warning_message = "//input[@name='telephone']//following-sibling::div"
    password_warning_message = "//input[@name='password']//following-sibling::div"

    expected_policy_warning_message = "Warning: You must agree to the Privacy Policy!"
    expected_firstname_warning_message = "First Name must be between 1 and 32 characters!"
    expected_lastname_warning_message = "Last Name must be between 1 and 32 characters!"
    expected_email_warning_message = "E-Mail Address does not appear to be valid!"
    expected_telephone_warning_message = "Telephone must be between 3 and 32 characters!"
    expected_password_warning_message = "Password must be between 4 and 20 characters!"

    def enter_firstname(self, firstname):
        self.driver.find_element(By.ID, self.firstname).click()
        self.driver.find_element(By.ID, self.firstname).clear()
        self.driver.find_element(By.ID, self.firstname).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(By.ID, self.lastname).click()
        self.driver.find_element(By.ID, self.lastname).clear()
        self.driver.find_element(By.ID, self.lastname).send_keys(lastname)

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email).click()
        self.driver.find_element(By.ID, self.email).clear()
        self.driver.find_element(By.ID, self.email).send_keys(email)

    def enter_telephone(self, telephone):
        self.driver.find_element(By.ID, self.telephone).click()
        self.driver.find_element(By.ID, self.telephone).clear()
        self.driver.find_element(By.ID, self.telephone).send_keys(telephone)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password).click()
        self.driver.find_element(By.ID, self.password).clear()
        self.driver.find_element(By.ID, self.password).send_keys(password)

    def enter_confirm_password(self, password):
        self.driver.find_element(By.ID, self.pass_confirm).click()
        self.driver.find_element(By.ID, self.pass_confirm).clear()
        self.driver.find_element(By.ID, self.pass_confirm).send_keys(password)

    def select_yes_radio_button(self):
        self.driver.find_element(By.XPATH, self.yes).click()

    def check_agree_policy(self):
        self.driver.find_element(By.NAME, self.agree_policy).click()

    def click_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()
        return AccountSuccessPage(self.driver)

    def retrieve_duplicate_email_warning(self):
        return self.driver.find_element(By.XPATH, self.duplicate_email_warning).text

    def retrieve_policy_warning_message(self):
        return self.driver.find_element(By.XPATH, self.policy_warning_message).text

    def retrieve_firstname_warning_message(self):
        return self.driver.find_element(By.XPATH, self.firstname_warning_message).text

    def retrieve_lastname_warning_message(self):
        return self.driver.find_element(By.XPATH, self.lastname_warning_message).text

    def retrieve_email_warning_message(self):
        return self.driver.find_element(By.XPATH, self.email_warning_message).text

    def retrieve_telephone_warning_message(self):
        return self.driver.find_element(By.XPATH, self.telephone_warning_message).text

    def retrieve_password_warning_message(self):
        return self.driver.find_element(By.XPATH, self.password_warning_message).text

    def register_an_account(self, firstname, lastname, email, telephone, password, yes_or_no, privacy_policy):
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_email(email)
        self.enter_telephone(telephone)
        self.enter_password(password)
        self.enter_confirm_password(password)
        if yes_or_no.__eq__("yes"):
            self.select_yes_radio_button()
        if privacy_policy.__eq__("select"):
            self.check_agree_policy()
        return self.click_continue_button()

    def verify_all_warnings(self):
        status = False
        if self.retrieve_policy_warning_message().__eq__(self.expected_policy_warning_message):
            if self.retrieve_firstname_warning_message().__eq__(self.expected_firstname_warning_message):
                if self.retrieve_email_warning_message().__eq__(self.expected_email_warning_message):
                    if self.retrieve_lastname_warning_message().__eq__(self.expected_lastname_warning_message):
                        if self.retrieve_telephone_warning_message().__eq__(self.expected_telephone_warning_message):
                            if self.retrieve_password_warning_message().__eq__(self.expected_password_warning_message):
                                status = True
        return status












