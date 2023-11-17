import pytest
from Pages.HomePage import HomePage
from Tests.BaseTest import BaseTest
from Utilities import ExcelUtils


class TestLogin(BaseTest):

    @pytest.mark.parametrize("email,password",
                             ExcelUtils.get_data_from_excel("Excelfiles/Exceldata.xlsx", "LoginTest"))
    def test_login_with_valid_email_and_valid_password(self, email, password):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        account_page = login_page.login_to_application(email, password)
        assert account_page.display_status_of_account_creation()
        self.generate_screenshots("login_with_valid_credentials")

    def test_login_with_invalid_email_and_valid_password(self, email="apple1236@gmail.com", password="apple123456" ):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application(email, password)
        expected_warning = "Warning: No match for E-Mail Address and/or Password"
        assert login_page.retrieve_warning_message().__contains__(expected_warning)
        self.generate_screenshots("login_with_invalid_emailid")

    def test_login_with_valid_email_and_invalid_password(self, email="apple123@gmail.com", password="apple123456"):
        home_page = HomePage(self.driver)
        home_page.navigate_to_login_page()
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application(email, password)
        expected_warning = "Warning: No match for E-Mail Address and/or Password"
        assert login_page.retrieve_warning_message().__contains__(expected_warning)
        self.generate_screenshots("login_with_invalid_password")

    def test_login_with_invalid_email_and_invalid_password(self, email="apple1235635@gmail.com", password="apple7123456"):
        home_page = HomePage(self.driver)
        home_page.navigate_to_login_page()
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application(email, password)
        expected_warning = "Warning: No match for E-Mail Address and/or Password"
        assert login_page.retrieve_warning_message().__contains__(expected_warning)
        self.generate_screenshots("login_with_invalid_email-id_and_password")

    def test_login_with_blank_email_and_password(self, email="", password=""):
        home_page = HomePage(self.driver)
        home_page.navigate_to_login_page()
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application(email, password)
        expected_warning = "Warning: No match for E-Mail Address and/or Password"
        assert login_page.retrieve_warning_message().__contains__(expected_warning)
        self.generate_screenshots("login_without_credentials")

