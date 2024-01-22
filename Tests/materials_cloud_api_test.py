import requests

'''Testing Materials Cloud API
Unlike Materials Project, Materials Cloud does not have a nice wrapper, instead, we have to use the requests library
'''

'''2D materials database (10.1038/s41565-017-0035-5)'''
URL_BASE=  "https://www.materialscloud.org/mcloud/api/v2/discover/mc2d/compounds"

json_mc2D = requests.get(URL_BASE).json()

data= json_mc2D["data"]
compounds = data["compounds"]

URL_MOS2 = "https://www.materialscloud.org/mcloud/api/v2/discover/mc2d/compound/MoS2-MoS2"
json_mos2 = requests.get(URL_MOS2).json()

data_mos2 = json_mos2["data"]
data_name = list(data_mos2.keys())[0]
data_dict = data_mos2[data_name][0]
