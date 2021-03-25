
import pandas as pd
import os as os
import json as json
import urllib3 as urllib3
import requests
from calendar import monthrange
import time



def generateMonthTxtFile(date,station_id):
    count = 0
    station_value = ""
    station_id_value = station_id
    date = date
    first_timestamp = "YYYY-MM-DDT00:00:00+08:00"
    # last_timestamp = "23:59:00"
    missing_timestamp = []
    url = 'https://api.data.gov.sg/v1/environment/wind-direction?date='
    timeStampCount = 0
    timeStampNoCount = 0
    url = url + date
    # puts the data into a variable
    data = requests.get(url).json()
    # for item in data['metadata']['stations']:
    #     print('ID is ' + str(item['id']) + '. It is located at ' + item['name'])
    fileName = str(date) + '_'+ station_id_value +'.txt'
    previous_timestamp = first_timestamp
    with open(fileName,'w') as myFile:
        for item in data['items']:
            timeStamp = item["timestamp"]
            readings = item['readings']
            if count == 0:
                temTimeStamp = firstTimeStamp(timeStamp)
                for item in readings:
                    if item['station_id'] == station_id_value:
                        station_value = str(item['value'])
                if station_value == "":
                    station_value = str(0)
                myFile.write(temTimeStamp + ";" + station_value + "\n")
                count = count + 1

            if count > 0:
                count = count + 1
                currentTimeStamp = timeConvert(timeStamp[11:16])
                previousTimeStamp = timeConvert(previous_timestamp[11:16])
                timeDiff = currentTimeStamp - previousTimeStamp
                for item in readings:
                    if item['station_id'] == station_id_value:
                        station_value = str(item['value'])
                if station_value == "":
                    station_value = str(0)
                
                if timeDiff > 1:
                    timeStampNoCount = timeStampNoCount + timeDiff - 1
                    missing_timestamp.append(timeStamp)
                    for time in range(1,timeDiff):
                        tempTimeStamp = newTimeStamp(previous_timestamp, time)
                        myFile.write(tempTimeStamp + ";" + station_value + "\n")
                
                myFile.write(timeStamp + ";" + station_value + "\n")
                previous_timestamp = timeStamp
                timeStampCount = timeStampCount + 1
                timeDiff = 0

        myFile.write('There are {} slots for the day.\nThere are {} lines.\nThere are {} missing lines'.format(str(count), str(timeStampCount), str(timeStampNoCount)))  
        myFile.write('\n' + str(1438 - timeStampCount))
        myFile.write('\nTimestamp missing in the list are listed below:\n')
        for item in missing_timestamp:
            myFile.write(item + "\n")

    print('There are {} empty slots for the day.\nThere are {} lines.\nThere are {} missing lines'.format(str(count), str(timeStampCount), str(timeStampNoCount)))  
    print('\n' + str(1438 - timeStampCount))
    print("Completed")
    print(missing_timestamp)

dataType = input("Please indicate if you want daily data or month data? (D = Daily; M = Monthly):")

if dataType == "D":
    date = input("Please indicate the date that you want to download the wind direction data from(YYYY-MM-DD): ")
    generateDayTxtFile(date)
elif dataType == "M":
    month_input = input("Please indicate the month and year that you want to download from? (YYYY-MM): ")
    station_id = input("Please indicate the station id: ")
    year = int(month_input[0:4])
    yearStr = str(year)
    month = int(month_input[5:])
    if month < 10:
        monthStr = "0" + str(month)
    else:
        monthStr = str(month)
    month_range = monthrange(year, month)
    total_days = month_range[1]
    for i in range(total_days):
        i = i + 1
        if i < 10:
            dayStr = "0" + str(i)
        else:
            dayStr = str(i)
        date = yearStr + "-" + monthStr + "-" + dayStr
        generateMonthTxtFile(date,station_id)
        
        