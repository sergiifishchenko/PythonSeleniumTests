from Pages.BasePage import *


class SearchResultsPage(BasePage):

    def is_results_found(self):
        return "No results found." not in self.driver.page_source
