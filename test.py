import json as json
import requests
from calendar import monthrange

def loadStationID():
    data = open("station.json")
    data = json.load(data)
    for item in data['metadata']['stations']:
        print('Station ' + item['id'] + ' is located at ' + item['name'])

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

def firstTimeStamp(currentTimeStamp):
    part1 = currentTimeStamp[:11]
    part2 = currentTimeStamp[11:13]
    part4 = currentTimeStamp[16:]
    newMinStr = ':00'
    tempTimeStamp = part1 + part2 + newMinStr + part4
    return tempTimeStamp

loadStationID()

station_id = input("Please indicate the station id of interest(e.g. S109): ")
month_input = input("Please indicate the month of interest(YYYY-MM): ")

year = int(month_input[0:4])
yearStr = str(year)
month = int(month_input[5:])
if month < 10:
    monthStr = "0" + str(month)
else:
    monthStr = str(month)

month_range = monthrange(year, month)
total_days = month_range[1]
count = 0
station_value = ""
first_timestamp = "YYYY-MM-DDT00:00:00+08:00"
# last_timestamp = "23:59:00"
missing_timestamp = []
url = 'https://api.data.gov.sg/v1/environment/wind-direction?date='
timeStampCount = 0
timeStampNoCount = 0
fileName = str(month_input) + '_'+ station_id +'.txt'
with open(fileName,'w') as myFile:    
    for i in range(total_days):
        i = i + 1
        if i < 10:
            dayStr = "0" + str(i)
        else:
            dayStr = str(i)
        date = yearStr + "-" + monthStr + "-" + dayStr
        url = url + date
        data = requests.get(url).json()
        previous_timestamp = first_timestamp
        for item in data['items']:
            timeStamp = item['timestamp']
            readings = item['readings']
            if count == 0:
                temTimeStamp = firstTimeStamp(timeStamp)
                for item in readings:
                    if item['station_id'] == station_id:
                        station_value = str(item['value'])
                if station_value == "":
                    station_value = str(0)
                myFile.write(temTimeStamp + "," + station_value + "\n")
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
                
                myFile.write(timeStamp + "," + station_value + "\n")
                previous_timestamp = timeStamp
                timeStampCount = timeStampCount + 1
                timeDiff = 0

        # myFile.write('There are {} slots for the day.\nThere are {} lines.\nThere are {} missing lines'.format(str(count), str(timeStampCount), str(timeStampNoCount)))  
        # myFile.write('\n' + str(1438 - timeStampCount))
        # myFile.write('\nTimestamp missing in the list are listed below:\n')
        # for item in missing_timestamp:
        #     myFile.write(item + "\n")
        print("Finished printing date: " + date + " at station id: " + station_id)
        url = 'https://api.data.gov.sg/v1/environment/wind-direction?date='

    

print("done")


    



        
        