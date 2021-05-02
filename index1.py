import pandas as pd
import os as os
import json as json
import urllib3 as urllib3
import requests
from calendar import monthrange
import time


def loadStationID():
    data = open("station.json")
    data = json.load(data)
    station_list = []
    station_id = ""
    for item in data['metadata']['stations']:
        station_list.append(item['id'])
        print('Station ' + item['id'] + ' is located at ' + item['name'])

    while station_id == "":
        station_id = input(
            "Please indicate the station id of interest(e.g. S109): ")
        if station_id in station_list:
            station_id = station_id
        else:
            print(
                "Please choose a station from the list provided. If you wish to exit, please press Ctrl+c")
            station_id = ""
    return station_id


def generateMonthTxtFile(date, station_id):
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
        generateTxtFile(date, station_id)
        print
    return None


def dataTypeChecker():
    dataType = input(
        "Please indicate if you want Daily or Monthly data? (D = Daily; M = Monthly): ")
    while dataType != "D" and dataType != "M":
        dataType = input(
            "The ID is not one of the station. Please indicate if you want Daily or Monthly data? (D = Daily; M = Monthly): ")
    return dataType


station_id = loadStationID()
# dataType = dataTypeChecker()
# if dataType == "D":
#     day_input = input(
#         "Please indicate the date that you want to download the wind direction data from(YYYY-MM-DD): ")
#     try:
#         generateTxtFile(day_input, station_id)
#         print('Data prepared and downloaded. Thank you and enjoy!')
#     except:
#         print('There seems to be something wrong on {}. Please ensure the date is from 2016 onwards. Thank you.'.format(day_input))
# elif dataType == "M":
#     month_input = input("Please indicate the month of interest(YYYY-MM): ")
#     generateMonthTxtFile(month_input, station_id)
# else:
#     print('Please re-run the software and key either D (Daily) or M (Monthly)')
