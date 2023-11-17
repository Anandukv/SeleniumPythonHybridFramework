
from Pages.HomePage import HomePage
from Tests.BaseTest import BaseTest


class TestSearch(BaseTest):

    def test_search_for_valid_product(self, product_name="HP"):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product(product_name)
        self.generate_screenshots("searched-product-found")
        assert search_page.display_status_of_product()

    def test_search_for_invalid_product(self, product_name="Nissan"):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product(product_name)
        expected_text = "There is no product that matches the search criteria."
        self.generate_screenshots("noproductfound")
        assert search_page.retrieve_no_product_message().__eq__(expected_text)

    def test_search_without_entering_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product("")
        expected_text = "There is no product that matches the search criteria."
        self.generate_screenshots("noitemsearched")
        assert search_page.retrieve_no_product_message().__eq__(expected_text)

    def test_search_product_negative_scenario(self, product_name="HP"):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product(product_name)
        expected_text = "There is no product that matches the search criteria."
        self.generate_screenshots("negative_scenario_itemsearched")
        assert search_page.retrieve_no_product_message().__eq__(expected_text)


# "pytest --alluredir="./Reports" -rA"