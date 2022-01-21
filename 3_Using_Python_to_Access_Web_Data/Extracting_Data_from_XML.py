# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1180709.xml (Sum ends with 77)

import urllib.request
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = input ("Enter location: ")
print('Retrieving', serviceurl)
uh = urllib.request.urlopen(serviceurl, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

lst = list()
counts = tree.findall('.//count')
for item in counts:
    lst.append(int(item.text))

print("Count:", len(lst))
print("Sum:", sum(lst))