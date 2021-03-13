import pandas as pd
import os as os
import json as json
import urllib3 as urllib3
import requests

##code for NEA weather code
# url = 'https://api.data.gov.sg/v1/environment/wind-direction?date=2020-10-10'
url = 'https://api.data.gov.sg/v1/environment/wind-direction?date='
url2 = 'https://api.data.gov.sg/v1/environment/wind-direction?date_time=2020-10-10T20%3A00%3A00&date=2020-10-10'

# data = requests.get(url).json()

##This prints out the number of headers in the json file
# for item in data:
#     print(item)

##this finds out the ID and name of each station
# for item in data['metadata']['stations']:
#     print('ID is ' + str(item['id']) + '. It is located at ' + item['name'])

##Prints out the time stamp and the data from station_id input
count = 0
station_value = ""
station_id = ""
date = ""
first_timestamp = "YYYY-MM-DDT00:00:00+08:00"
last_timestamp = "23:59:00"
date = input("Please indicate the date that you want to draw the wind direction data from(YYYY-MM-DD): ")
url = url + date

data = requests.get(url).json()
for item in data['metadata']['stations']:
    print('ID is ' + str(item['id']) + '. It is located at ' + item['name'])

station_id = input('Please indicate the station ID No: ')
fileName = str(date) + '_'+ station_id +'.txt'
previous_timestamp = first_timestamp
timeStampCount = 0
timeStampNoCount = 0
with open(fileName,'w') as myFile:
    for item in data['items']:
        timeStamp = item['timestamp']
        timeDiff = int(timeStamp[14:16]) - int(previous_timestamp[14:16]) 
        if  timeDiff != 1 or timeDiff != -59:
            if timeDiff > 0:
                timeStampNoCount = timeStampNoCount + timeDiff
            else:
                timeStampNoCount = timeStampNoCount + (60 - abs(timeDiff))
        readings = item['readings']
        for item in readings:
            if item['station_id'] == station_id:
                station_value = str(item['value'])
        if station_value == "":
            station_value = 0
            count = count + 1
        # print("At {}, readings at {} = {}".format(timeStamp, station_id, station_value))
        myFile.write("At {}, readings at {} = {}\n".format(timeStamp, station_id, station_value))
        previous_timestamp = timeStamp
        timeStampCount = timeStampCount + 1
    # print('There are {} empty slots for the day.'.format(str(count))) 
    myFile.write('There are {} empty slots for the day.\nThere are {} lines.\nThere are {} missing lines'.format(str(count), str(timeStampCount), str(timeStampNoCount)))  


print("Completed")