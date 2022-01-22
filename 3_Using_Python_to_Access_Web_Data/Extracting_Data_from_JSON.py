# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1180710.json (Sum ends with 21)

import urllib.request, urllib.response
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = input("Enter location: ")
print("Retrieving", serviceurl)

uh = urllib.request.urlopen(serviceurl, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
print('User count:', len(info))

lst = list()
for item in info['comments']:
    lst.append(item['count'])

print("Count: ", len(lst))
print("Sum: ", sum(lst))