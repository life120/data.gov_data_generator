import pandas as pd
import os as os
import json as json
import urllib3 as urllib3
import requests

##code for NEA weather code
url = 'https://api.data.gov.sg/v1/environment/wind-direction?date=2020-10-10'
url2 = 'https://api.data.gov.sg/v1/environment/wind-direction?date_time=2020-10-10T20%3A00%3A00&date=2020-10-10'

data = requests.get(url).json()
# df = pd.DataFrame.from_dict(data)

# list1 = data['items'][0]
# list2 = data['items'][1]

##This prints out the number of headers in the json file
# for item in data:
#     print(item)

##this finds out the ID and name of each station
for item in data['metadata']['stations']:
    print('ID is ' + str(item['id']) + '. It is located at ' + item['name'])

# ID is S109. It is located at Ang Mo Kio Avenue 5
# ID is S117. It is located at Banyan Road
# ID is S107. It is located at East Coast Parkway
# ID is S43. It is located at Kim Chuan Road
# ID is S108. It is located at Marina Gardens Drive
# ID is S44. It is located at Nanyang Avenue
# ID is S106. It is located at Pulau Ubin
# ID is S60. It is located at Sentosa
# ID is S115. It is located at Tuas South Avenue 3
# ID is S24. It is located at Upper Changi Road North
# ID is S116. It is located at West Coast Highway
# ID is S104. It is located at Woodlands Avenue 9
# ID is S100. It is located at Woodlands Road
# ID is S50. It is located at Clementi Road

##This finds the timestamp inside 'item'
# for item in data['items']:
#     print('Date: ' + item['timestamp'])

# {} is a dictionary
# [] is a list

##This finds the value from each item
# items = data['items']
# readings = items[0]['readings']

# for item in readings:
#     if item['station_id'] == 'S109':
#         print(item['station_id'] + ' ' + str(item['value']))


##Prints out the time stamp and the data from station_id S109
for item in data['items']:
    timeStamp = item['timestamp']
    readings = item['readings']
    for item in readings:
        if item['station_id'] == 'S109':
            S109Value = str(item['value'])
        elif item['station_id'] == 'S117':
            S117Value = str(item['value'])
        elif item['station_id'] == 'S107':
            S107Value = str(item['value'])
        elif item['station_id'] == 'S107':
            S107 = str(item['value'])
        elif item['station_id'] == 'S43':
            S43 = str(item['value'])
        elif item['station_id'] == 'S108':
            S108 = str(item['value'])
        elif item['station_id'] == 'S44':
            S44 = str(item['value'])
        elif item['station_id'] == 'S106':
            S106 = str(item['value'])
        elif item['station_id'] == 'S60':
            S60 = str(item['value'])
        elif item['station_id'] == 'S115':
            S115 = str(item['value'])
        elif item['station_id'] == 'S24':
            S24 = str(item['value'])
        elif item['station_id'] == 'S104':
            S104 = str(item['value'])
        elif item['station_id'] == 'S100':
            S100 = str(item['value'])
        elif item['station_id'] == 'S50':
            S50 = str(item['value'])
        
        print("At {}, readings at S109 = {}".format(timeStamp, S109Value))

print("Completed")