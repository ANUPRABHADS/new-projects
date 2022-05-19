# import requests
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# print(response.status_code)
# if response.status_code != 200:
#     raise Exception("Bad response")
#
# data=response.json()
# print(data)
# longitude=data ["iss_position"]["longitude"]
# latitude=data["iss_position"]["latitude"]
# iss_position=(longitude,latitude)
# print(iss_position)

import requests
response=requests.get(url="http://api.kanye.rest")
print(response)
if response.status_code !=200:
    raise Exception("Unsuccesfull")
data=response.json()["quote"]
print(data)