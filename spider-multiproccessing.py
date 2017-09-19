from multiprocessing import Pool
import bs4 as bs
import random
import requests
import string
# a spider is used to quickly access and process many websites at once
# beautiful soup library is used for parsing HTML pages

def random_starting_url():
    starting = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for i in range(3))
    url = ''.join(['http://', starting, '.com'])
    return url
