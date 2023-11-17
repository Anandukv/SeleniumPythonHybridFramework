import datetime
from random import randint
import pytest
from Pages.HomePage import HomePage
from Tests.BaseTest import BaseTest
from Utilities import ExcelUtils


class TestRegister(BaseTest):

    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        confirmation_message = "Your Account Has Been Created!"
        account_success_page = register_page.register_an_account(ExcelUtils.readdata("Excelfiles/Exceldata.xlsx", "LoginTest", 2, 2), "lastname",
                                                                 self.generate_email_with_timestamp(),
                                                                 self.generate_telephone_number_with_random(), "123456",
                                                                 "no", "select")
        assert account_success_page.retrieve_status_of_account_creation().__eq__(confirmation_message)
        self.generate_screenshots("Registered_with_mandatory_fields")

    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        confirmation_message = "Your Account Has Been Created!"
        account_success_page = register_page.register_an_account("test", "lastname",
                                                                 self.generate_email_with_timestamp(),
                                                                 self.generate_telephone_number_with_random(),
                                                                 "123456", "yes", "select")
        assert account_success_page.retrieve_status_of_account_creation().__eq__(confirmation_message)
        self.generate_screenshots("Registered_with_all_fields")

    def test_register_with_duplicate_emailid(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("test", "lastname", "apple123@gmail.com",
                                          self.generate_telephone_number_with_random(), "123456",
                                          "yes", "select")
        warning_message = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_duplicate_email_warning().__eq__(warning_message)
        self.generate_screenshots("Register_with_duplicate_emailid")

    def test_register_without_entering_any_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("", "", "", "", "", "", "")
        assert register_page.verify_all_warnings()
        self.generate_screenshots("Register_with_no_details")














# assert register_page.retrieve_policy_warning_message().__eq__(expected_policy_warning_message)
# assert register_page.retrieve_firstname_warning_message().__eq__(expected_firstname_warning_message)
# assert register_page.retrieve_email_warning_message().__eq__(expected_email_warning_message)
# assert register_page.retrieve_lastname_warning_message().__eq__(expected_lastname_warning_message)
# assert register_page.retrieve_telephone_warning_message().__eq__(expected_telephone_warning_message)
# assert register_page.retrieve_password_warning_message().__eq__(expected_password_warning_message)
