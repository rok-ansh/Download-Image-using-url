import requests

url = ("https://upload.wikimedia.org/wikipedia/en/thumb/3/35/"
       "Supermanflying.png/220px-Supermanflying.png")

response = requests.get(url)

with open("superman.png", "wb") as file:
       file.write(response.content)


