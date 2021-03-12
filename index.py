import pandas as pd
import os as os
import json as json
import urllib3 as urllib3
import requests

##code for NEA weather code duh
url = 'https://api.data.gov.sg/v1/environment/wind-direction?date=2020-10-10'
url2 = 'https://api.data.gov.sg/v1/environment/wind-direction?date_time=2020-10-10T20%3A00%3A00&date=2020-10-10'

data = requests.get(url).json()
# df = pd.DataFrame.from_dict(data)
print(data)
# print(data['items'][0].get('readings'))
# list1 = data['items'][0].get('readings')
# for item in list1:
#     if item.get('station_id')== 'S109':
#         print(item.get('value'))