__author__ = 'nispc'

import requests
from bs4 import BeautifulSoup as bs

res = requests.get('https://www.youtube.com/all_comments?v=wTVN6If-f2M')
soup = bs(res.text, "html.parser")
c = soup.select('.all-comments')

print(c[0].text)