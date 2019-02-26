from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import string
import random
from selenium.webdriver.support.select import Select


def random_string():
    # string will be chosen from letters, digits, len=3
    symbols = string.ascii_lowercase + string.digits
    return ''.join([random.choice(symbols) for i in range(10)])

test_data = random_string() + ('@') +random_string() +('.com')

print(test_data)