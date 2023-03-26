import requests
response = requests.get("https://randomuser.me/api")
# print(response.status_code)
# print(response.json())

gender = response.json()['results'][0]['gender']
# print(gender)

title = response.json()['results'][0]['name']['title']
first_name = response.json()['results'][0]['name']['first']
last_name = response.json()['results'][0]['name']['last']

# print(first_name) 
print(f' {title}. {first_name} {last_name}')