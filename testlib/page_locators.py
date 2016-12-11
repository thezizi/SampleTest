from selenium.webdriver.common.by import By


class SearchEngineMainPage(object):
    """
    """
    search_textbox = (By.XPATH, "//*[@id='gs_htif0']")
    search_button = (By.XPATH, "//*[@id='tsf']/div[2]/div[3]/center/input[1]")


class SearchResultsPage(object):
    """
    """
    google_symbol = (By.XPATH, "//*[@id='logo']/img")
    search_stats = (By.XPATH, "//*[@id='resultStats']")


class GmailLoginPage(object):
    """
    """
    gmail_header = (By.XPATH, "html/body/div[1]/div[2]/div[1]/h1")
    user_name_field = (By.XPATH, "//*[@id='Email']")
    password_field = (By.XPATH, "//*[@id='Passwd']")
    next_button = (By.XPATH, "//*[@id='next']")
    signin_button = (By.XPATH, "//*[@id='signIn']")


class GmailAccount(object):
    """
    """
    gmail_symbol = (By.XPATH, "//*[@id='gbq1']/div/a/span")
    user_avatar = (By.XPATH, "//*[@id='gb']/div[1]/div[1]/div[2]/div[4]/div[1]/a/span")
    logout_btn = (By.XPATH, "//*[@id='gb_71']")
