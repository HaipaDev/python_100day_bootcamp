import requests
from datetime import datetime,timedelta

USERNAME="maciejkrefft03"
TOKEN="g456457j2j523fhfghfg"

pixela_endpoint=f"https://pixe.la/v1/users"

user_params={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

user_response=requests.post(url=pixela_endpoint,json=user_params)
#user_response.raise_for_status()
print(user_response.text)
print(f"https://pixe.la/v1/users/@{USERNAME}")

GRAPH_ID="graph1"
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config={
    "id":GRAPH_ID,
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}
headers={"X-USER-TOKEN":TOKEN}

graph_reponse=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
#graph_reponse.raise_for_status()
print(graph_reponse.text)
print(f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}.html")


today=str(datetime.now().strftime("%Y%m%d"))
yesterday=str((datetime.now()-timedelta(days=1)).strftime("%Y%m%d"))

# pixel_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# pixel_creation_config={
#     "date":today,
#     "quantity":"9.74"
# }

# pixel_creation_response=requests.post(url=pixel_creation_endpoint,json=pixel_creation_config,headers=headers)
# #pixel_creation_response.raise_for_status()
# print(pixel_creation_response.text)


pixel_updating_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday}"
pixel_updating_config={
    "quantity":"4"
}

pixel_updating_response=requests.put(url=pixel_updating_endpoint,json=pixel_updating_config,headers=headers)
#pixel_updating_response.raise_for_status()
print(pixel_updating_response.text)


pixel_delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday}"

pixel_delete_response=requests.delete(url=pixel_delete_endpoint,headers=headers)
#pixel_delete_response.raise_for_status()
print(pixel_delete_response.text)