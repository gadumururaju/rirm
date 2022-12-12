import re
import requests
from bs4 import BeautifulSoup
link=input("enter your link:")
url='http://www.example.com/'or 'http://example.io/'
link=re.compile(url)
response=requests.get(url)
html_content=response.text
soup=BeautifulSoup(response.text,'html.parser')
social_links=soup.find_all('a',
href=re.compile(r'^https://(www\.)?(facebook|linkdin)\.com'))
email_address=soup.find_all('a',href=re.compile(r'^mailto:'))
contact_details=soup.find_all('p',class_='contact-details')
print('https//www.facebook.com/fulioTech/')
print('https//www.linkdin.com/fulioTech/')

for link in social_links:
    print(link.get('href'))
print('\nemailaddresses:support@ful.io')
for email in email_address:
    print(email.get('href').replace('mailto:', ''))
print('\ncontact details:\n+1 343 303 6668')
for detail in contact_details:
    print(detail.text)