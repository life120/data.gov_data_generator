import pandas as pd
import os as os
import json as json
import urllib3 as urllib3
import requests

count = 0
station_value = ""
station_id = ""
date = ""
first_timestamp = "YYYY-MM-DDT00:00:00+08:00"
last_timestamp = "23:59:00"

##code for NEA weather code
# url = 'https://api.data.gov.sg/v1/environment/wind-direction?date=2020-10-10'
url = 'https://api.data.gov.sg/v1/environment/wind-direction?date='
url2 = 'https://api.data.gov.sg/v1/environment/wind-direction?date_time=2020-10-10T20%3A00%3A00&date=2020-10-10'

def timeConvert(timeStamp):
    min = int(timeStamp[3:])
    hr = int(timeStamp[0:2])
    time = 60*hr + min
    return time

def newTimeStamp(currentTimeStamp, time):
    part1 = currentTimeStamp[:11]
    part2 = currentTimeStamp[11:13]
    part4 = currentTimeStamp[16:]
    oldMin = int(currentTimeStamp[14:16])
    newMin = oldMin + time
    
    if newMin < 10:
        newMinStr = ':0' + str(newMin)
        tempTimeStamp = part1 + part2 + newMinStr + part4
        return tempTimeStamp
    elif newMin > 9 and newMin < 60:
        newMinStr = ':' + str(newMin)
        tempTimeStamp = part1 + part2 + newMinStr + part4
        return tempTimeStamp
    elif newMin > 59:
        newMinStr = ':0' + str(newMin - 60)
        newHr = int(part2) + 1
        if newHr < 10:
            newHrStr = '0' + str(newHr)
        else:
            newHrStr = str(newHr)
        tempTimeStamp = part1 + newHrStr + newMinStr + part4
        return tempTimeStamp

##Prints out the time stamp and the data from station_id input



date = input("Please indicate the date that you want to draw the wind direction data from(YYYY-MM-DD): ")
url = url + date

# puts the data into a variable
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
        if count == 0:
            timeStamp = first_timestamp
            station_value = item['value']
            myFile.write(timeStamp + ";" + station_id)
            count = count + 1

        if count > 0:
            timeStamp = item['timeStamp']
            station_value = item['value']
            currentTimeStamp = timeConvert(timeStamp[11:16])
            previousTimeStamp = timeConvert(previous_timestamp[11:16])
            timeDiff = currentTimeStamp - previousTimeStamp
            station_value = str(item['value'])
            if timeDiff > 1:
                timeStampNoCount = timeStampNoCount + timeDiff - 1
                for time in range(1,timeDiff):
                    tempTimeStamp = newTimeStamp(previous_timestamp, time)
                    print("At {}, readings at {} = {}\n".format(tempTimeStamp, station_id, station_value))
            
            print("At {}, readings at {} = {}\n".format(timeStamp, station_id, station_value))
            previous_timestamp = timeStamp
            timeStampCount = timeStampCount + 1
            timeDiff = 0

            timeStamp = item['timestamp']
            currentTimeStamp = timeConvert(timeStamp[11:16])
            previousTimeStamp = timeConvert(previous_timestamp[11:16])
            timeDiff = currentTimeStamp - previousTimeStamp
            if timeDiff > 1:
                timeStampNoCount = timeStampNoCount + timeDiff - 1

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
            timeDiff = 0
    # print('There are {} empty slots for the day.'.format(str(count)))
    timeStampNoCount = timeStampNoCount - 1 
    myFile.write('There are {} empty slots for the day.\nThere are {} lines.\nThere are {} missing lines'.format(str(count), str(timeStampCount), str(timeStampNoCount)))  
    myFile.write('\n' + str(1438 - timeStampCount))

print('There are {} empty slots for the day.\nThere are {} lines.\nThere are {} missing lines'.format(str(count), str(timeStampCount), str(timeStampNoCount)))  
print('\n' + str(1438 - timeStampCount))
print("Completed")
