from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Pages.RegisterPage import RegisterPage
from Pages.SearchPage import SearchPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    search_box_field_name = "search"
    search_button_xpath = "//button[@class='btn btn-default btn-lg']"
    my_account_drop_down_menu = "//span[text()='My Account']"
    login = "Login"
    register = "Register"

    def select_register_optn(self):
        self.driver.find_element(By.LINK_TEXT, self.register).click()
        return RegisterPage(self.driver)

    def enter_product_into_search_box_field(self, product_name):
        self.driver.find_element(By.NAME, self.search_box_field_name).click()
        self.driver.find_element(By.NAME, self.search_box_field_name).clear()
        self.driver.find_element(By.NAME, self.search_box_field_name).send_keys(product_name)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        return SearchPage(self.driver)

    def click_on_my_account_dropdown_menu(self):
        self.driver.find_element(By.XPATH, self.my_account_drop_down_menu).click()

    def select_login_option(self):
        self.driver.find_element(By.LINK_TEXT, self.login).click()
        return LoginPage(self.driver)

    def search_for_a_product(self, product_name):
        self.enter_product_into_search_box_field(product_name)
        return self.click_on_search_button()

    def navigate_to_login_page(self):
        self.click_on_my_account_dropdown_menu()
        return self.select_login_option()

    def navigate_to_register_page(self):
        self.click_on_my_account_dropdown_menu()
        return self.select_register_optn()

