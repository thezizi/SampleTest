"""
author: Konrad Michalczyk
"""

import pytest
from selenium import webdriver as wb
from testlib.page import EmailWebPage


class TestMailLoginLogout(object):

    @pytest.fixture(autouse=True)
    def open_browser(self, request):
        """
        fixture for browser object creation
        :param request:
        :return:
        """
        self.browser_fixt = wb.Firefox()
        self.browser_fixt.get('http://gmail.com')

        def fin():
            self.browser_fixt.quit()

        request.addfinalizer(fin)

    def test_mail_login(self, user_credentials):
        browser = EmailWebPage(self.browser_fixt)
        browser.enter_user_name(user_credentials['user'])
        browser.enter_password(user_credentials['password'])
        assert browser.check_user_avatar(), 'Login failed, user avatar not visible in page'
