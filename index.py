import pandas as pd
import os as os
import json as json
import urllib3 as urllib3
import requests

##code for NEA weather code
url = 'https://api.data.gov.sg/v1/environment/wind-direction?date=2020-10-10'
url2 = 'https://api.data.gov.sg/v1/environment/wind-direction?date_time=2020-10-10T20%3A00%3A00&date=2020-10-10'

data = requests.get(url2).json()
# df = pd.DataFrame.from_dict(data)

# list1 = data['items'][0]
# list2 = data['items'][1]

##This prints out the number of headers in the json file
# for item in data:
#     print(item)

##this finds out the ID and name of each station
# for item in data['metadata']['stations']:
#     print('ID is ' + str(item['id']) + '. It is located at ' + item['name'])

##This finds the timestamp inside 'item'
# for item in data['items']:
#     print('Date: ' + item['timestamp'])

# {} is a dictionary
# [] is a list

##This finds the value from each item
items = data['items']
readings = items[0]['readings']

for item in readings:
    print(item['station_id'] + ' ' + str(item['value']))

print("Completed")