# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Amber.html

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
import collections
collections.Callable = collections.abc.Callable

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

# Retrieve all of the anchor tags

run = 0
while run <= count:
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    print("Retrieving: ", url)
    taglist = list()
    tags = soup('a')
    for tag in tags:
        taglist.append(tag.get('href', None))
    url = taglist[position-1]
    run +=1