import pandas as pd
import os as os
import json as json
import urllib3 as urllib3
import requests
from calendar import monthrange
import time

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
        newMinValue = newMin - 60*(newMin//60)
        if newMinValue < 10:
            newMinStr = ':0' + str(newMinValue)
        elif newMinValue > 9:
            newMinStr = ':' + str(newMinValue)
        newHr = int(part2) + newMin//60
        if newHr < 10:
            newHrStr = '0' + str(newHr)
        else:
            newHrStr = str(newHr) 
        tempTimeStamp = part1 + newHrStr + newMinStr + part4
        return tempTimeStamp

def firstTimeStamp(currentTimeStamp):
    part1 = currentTimeStamp[:11]
    part2 = currentTimeStamp[11:13]
    part4 = currentTimeStamp[16:]
    newMinStr = ':00'
    tempTimeStamp = part1 + part2 + newMinStr + part4
    return tempTimeStamp

def generateDayTxtFile(date,station_id):
    count = 0
    station_value = ""
    station_id = station_id
    date = date
    first_timestamp = "YYYY-MM-DDT00:00:00+08:00"
    last_timing = "YYYY-MM-DDT23:59:00+08:00"
    missing_timestamp = []
    url = 'https://api.data.gov.sg/v1/environment/wind-direction?date='
    timeStampCount = 0
    timeStampNoCount = 0
    url = url + date
    # puts the data into a variable
    data = requests.get(url).json()
    
    fileName = str(date) + '_'+ station_id +'.txt'
    previous_timestamp = first_timestamp
    with open(fileName,'w') as myFile:
        for item in data['items']:
            timeStamp = item["timestamp"]
            readings = item['readings']
            if count == 0:
                temTimeStamp = firstTimeStamp(timeStamp)
                for item in readings:
                    if item['station_id'] == station_id:
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
                    if item['station_id'] == station_id:
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
        lastDataTiming = timeStamp
        if lastDataTiming[11:16] != last_timing[11:16]:
            previousTimeStamp = timeConvert(lastDataTiming[11:16])
            current_timing = timeConvert(last_timing[11:16])
            timeDiff = current_timing - previousTimeStamp + 1
            for time in range(1,timeDiff):
                tempTimeStamp = newTimeStamp(previous_timestamp, time)
                myFile.write(tempTimeStamp + ";" + station_value + "\n")

        myFile.write('There are {} slots for the day.\nThere are {} lines.\nThere are {} missing lines'.format(str(count), str(timeStampCount), str(timeStampNoCount)))  
        myFile.write('\n' + str(1438 - timeStampCount))
        myFile.write('\nTimestamp missing in the list are listed below:\n')
        for item in missing_timestamp:
            myFile.write(item + "\n")
    timeStamp = ""
    print('There are {} slots for the day.\nThere are {} lines in the document.\nThere are {} missing lines'.format(str(count), str(timeStampCount), str(timeStampNoCount)))  
    print('\n' + str(1438 - timeStampCount))
    print("Completed")
    print(missing_timestamp)
##Prints out the time stamp and the data from station_id input

def loadStationID():
    data = open("station.json")
    data = json.load(data)
    station_list = []
    station_id = ""
    for item in data['metadata']['stations']:
        station_list.append(item['id'])
        print('Station ' + item['id'] + ' is located at ' + item['name'])
    
    while station_id == "":
        station_id = input("Please indicate the station id of interest(e.g. S109): ")
        if station_id in station_list:
            station_id = station_id
        else:
            print("Please choose a station from the list provided. If you wish to exit, please press Ctrl+c")
            station_id = ""
    return station_id

def generateMonthTxtFile(date,station_id):
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
        generateDayTxtFile(date, station_id)
        print
    return None

def dataTypeChecker():
    dataType = input("Please indicate if you want Daily or Monthly data? (D = Daily; M = Monthly): ")
    while dataType != "D" and dataType != "M":
        dataType = input("The ID is not one of the station. Please indicate if you want Daily or Monthly data? (D = Daily; M = Monthly): ")
    return dataType

station_id = loadStationID()
dataType = dataTypeChecker()
if dataType == "D":
    date = input("Please indicate the date that you want to download the wind direction data from(YYYY-MM-DD): ")
    generateDayTxtFile(date,station_id)
elif dataType == "M":
    month_input = input("Please indicate the month of interest(YYYY-MM): ")
    generateMonthTxtFile(month_input, station_id)
else:
    print('Please re-run the software and key either D (Daily) or M (Monthly)')



# if dataType == "D":
#     date = input("Please indicate the date that you want to download the wind direction data from(YYYY-MM-DD): ")
#     generateDayTxtFile(date)
# elif dataType == "M":
#     month_input = input("Please indicate the month and year that you want to download from? (YYYY-MM): ")
#     station_id = input("Please indicate the station id: ")
#     year = int(month_input[0:4])
#     yearStr = str(year)
#     month = int(month_input[5:])
#     if month < 10:
#         monthStr = "0" + str(month)
#     else:
#         monthStr = str(month)
#     month_range = monthrange(year, month)
#     total_days = month_range[1]
#     for i in range(total_days):
#         i = i + 1
#         if i < 10:
#             dayStr = "0" + str(i)
#         else:
#             dayStr = str(i)
#         date = yearStr + "-" + monthStr + "-" + dayStr
#         generateMonthTxtFile(date,station_id)
        
        

