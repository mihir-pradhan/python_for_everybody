# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1180707.html (Sum ends with 90)

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import collections
collections.Callable = collections.abc.Callable

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

numlist = list()
# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
    # Append to list    
    numlist.append(int(tag.contents[0]))

# Print Count and Sum
print("Count", len(numlist))
print("Sum", sum(numlist))