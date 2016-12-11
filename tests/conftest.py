from ConfigParser import ConfigParser
import os


def pytest_generate_tests(metafunc):
    """
    hook function for test cases generation based on users list
    :param metafunc:
    :return:
    """
    for fixture in metafunc.fixturenames:
        if 'user_credentials' in fixture:
            user_dct = {}
            users_lst = []
            cf = ConfigParser()
            cf.read(os.path.join(os.getcwd(), 'user_credentials.ini'))
            for section in cf.sections():
                user_name = cf.get(section, 'user_name')
                password = cf.get(section, 'password')
                user_dct['user'] = user_name
                user_dct['password'] = password
                users_lst.append(user_dct)
            metafunc.parametrize('user_credentials', users_lst)
