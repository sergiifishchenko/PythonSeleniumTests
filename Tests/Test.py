import unittest

from Pages.MainPage import *
from Pages.SearchPage import *
from Tests.BaseTest import BaseTest


class PythonOrgSearch(BaseTest):

    def test_search_in_python_org(self):

        main_page = MainPage(self.driver)
        search_page = SearchResultsPage(self.driver)
        assert main_page.is_title_matches(), "python.org title doesn't match."
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        assert search_page.is_results_found(), "No results found."

    def requests_test(self):
        pass

if __name__ == "__main__":
    unittest.main()
