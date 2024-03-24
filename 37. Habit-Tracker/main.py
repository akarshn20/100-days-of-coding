import requests
from datetime import datetime

USER_NAME = "akarsh"
TOKEN = "hdadu90qwuoahf8u93w040"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Submits",
    "type": "int",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation = f"{pixela_endpoint}/{USER_NAME}/graphs/graph1"

today = datetime(year=2024, month=3, day=23)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5"
}

# response = requests.post(url=pixel_creation, json=pixel_data, headers=headers)
# print(response.text)

edit_pixel = f"{pixel_creation}/{today.strftime('%Y%m%d')}"

edit_data = {
    "quantity": "3"
}

# response = requests.put(url=edit_pixel, json=edit_data, headers=headers)
# print(response.text)

delete_pixel = f"{pixel_creation}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=edit_pixel, headers=headers)
print(response.text)

