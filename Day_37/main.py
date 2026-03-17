import requests
import datetime as dt

USERNAME = "amardeep"
TOKEN = "HSAsd7348gi4kgo0fdj839"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

# ------------- Create a new account -----------------------------
parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# responce = requests.post(url=PIXELA_ENDPOINT, json=parameters)
# print(responce.text)

# ------------- setting up a new graph ----------------------------
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "running graph",
    "unit": "km",
    "type": "float",
    "color": "shibafu"
}
auth_header = {
    "X-USER-TOKEN": TOKEN
}

# responce = requests.post(
#     url=graph_endpoint, json=graph_config, headers=auth_header)
# print(responce.text)

# -------------- post some data ---------------------------------

# post url = https://pixe.la/v1/users/a-know/graphs/test-graph -H 'X-USER-TOKEN:thisissecret'
# -d '{"date":"20180915","quantity":"5"}'

today = dt.datetime(year=2025, month=10, day=13)
post_url = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_config['id']}"
post_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "20.0"
}
# responce = requests.post(url=post_url, json=post_data, headers=auth_header)
# print(responce.text)

# --------------- update some pixel data --------------------------------

# PUT - /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>

put_url = f"{post_url}/{today.strftime("%Y%m%d")}"
update_data = {
    "quantity": "10.0"
}

# responce = requests.put(url=put_url, json=update_data, headers=auth_header)
# print(responce.text)

# ---------------- Delete some pixel data --------------------------------

# DELETE - /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>

delete_url = put_url
responce = requests.delete(url=delete_url, headers=auth_header)
print(responce.text)
