from page_locators import *
from selenium.webdriver.support.ui import WebDriverWait


class SearchPage(object):

    def __init__(self, driver):
        self.driver = driver

    def search_item(self, item):
        """
        :param item: item to search for, type is string
        :return:
        """
        search_box = WebDriverWait(self.driver, 10).until(
            lambda browser: self.driver.find_element(*SearchEngineMainPage.search_textbox))
        print dir(search_box)
        search_box.send_keys(item)

    def verify_search_results(self):
        """
        :return:
        """
        return WebDriverWait(self.driver, 10).until(
            lambda browser: self.driver.find_element(*SearchResultsPage.search_stats))


class EmailWebPage(object):

    def __init__(self, driver):
        self.driver = driver

    def enter_user_name(self, user_name):
        """
        :param user_name:
        :return:
        """
        login = WebDriverWait(self.driver, 10).until(
            lambda browser: self.driver.find_element(*GmailLoginPage.user_name_field))
        next_btn = WebDriverWait(self.driver, 10).until(
            lambda browser: self.driver.find_element(*GmailLoginPage.next_button))
        login.send_keys(user_name)
        next_btn.click()

    def enter_password(self, password):
        """
        :param password:
        :return:
        """
        passwd = WebDriverWait(self.driver, 10).until(
            lambda browser: self.driver.find_element(*GmailLoginPage.password_field))
        login_btn = WebDriverWait(self.driver, 10).until(
            lambda browser: self.driver.find_element(*GmailLoginPage.signin_button))
        passwd.send_keys(password)
        login_btn.click()

    def check_user_avatar(self):
        return WebDriverWait(self.driver, 10).until(
            lambda browser: self.driver.find_element(*GmailAccount.user_avatar))

    def logout_user(self):
        WebDriverWait(self.driver, 10).until(
            lambda browser: self.driver.find_element(*GmailAccount.user_avatar)).click()
        WebDriverWait(self.driver, 10).until(
            lambda browser: self.driver.find_element(*GmailAccount.logout_btn)).click()

    def check_gmail_header(self):
        return WebDriverWait(self.driver, 10).until(
            lambda browser: self.driver.find_element(*GmailLoginPage.gmail_header))
