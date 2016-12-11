"""
author: Konrad Michalczyk
"""

import pytest
from selenium import webdriver as wb
from testlib.page import SearchPage


class TestSampleTest(object):

    @pytest.fixture(autouse=True)
    def open_browser(self, request):
        """
        fixture for browser object creation
        :param request:
        :return:
        """
        self.browser_fixt = wb.Firefox()
        self.browser_fixt.get('http://www.google.pl')

        def fin():
            self.browser_fixt.quit()

        request.addfinalizer(fin)

    @pytest.mark.usefixtures('open_browser')
    def test_search_item(self):
        """
        :return:
        """
        browser_test = SearchPage(self.browser_fixt)
        browser_test.search_item('S3 group Wroclaw')
        assert browser_test.verify_search_results()
