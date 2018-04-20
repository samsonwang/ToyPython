
'''
decode web page

Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
'''

import urllib.request
import urllib.parse


str_url = "https://github.com"
# req type is HttpResponse
req = urllib.request.urlopen(str_url)

req_body = req.read()

#print("req_body", req_body)
print("req_body.decode", req_body.decode('utf-8'))


