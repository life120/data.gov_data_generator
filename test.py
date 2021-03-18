
dict = [{'timeStamp' : '2018-02-24T00:01:00+08:00', 'value' : 10},{'timeStamp' : '2018-02-24T00:02:00+08:00', 'value' : 9}, {'timeStamp' : '2018-02-24T00:09:00+08:00', 'value' : 10}, {'timeStamp' : '2018-02-24T00:10:00+08:00', 'value' : 11}, {'timeStamp' : '2018-02-24T00:50:00+08:00', 'value' : 2}, {'timeStamp' : '2018-02-24T01:05:00+08:00', 'value' : 7}]
previous_timestamp = '2018-02-24T00:00:00+08:00'
count = 0
station_id = 'S109'
timeStampNoCount = 0
timeStampCount = 0
timeDiff = 0

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

for item in dict:
    if count == 0:
        timeStamp = previous_timestamp
        station_value = item['value']
        print("At {}, readings at {} = {}\n".format(timeStamp, station_id, station_value))
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
print(timeStampNoCount)


