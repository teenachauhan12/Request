import requests

r = requests.delete('https://httpbin.org / delete', data ={'key':'value'})
print(r)
print(r.json())




