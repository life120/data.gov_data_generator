timeStamp1 = '2019-02-24T00:01:00+08:00'
timeStamp2 = '2019-02-24T00:58:00+08:00'
timeStamp3 = '2019-02-24T01:28:00+08:00'



def timeConvert(timeStamp):
    min = int(timeStamp[3:])
    hr = int(timeStamp[0:2])
    time = 60*hr + min
    return time

time_int_1 = timeConvert(timeStamp1[11:16])
time_int_2 = timeConvert(timeStamp2[11:16])
time_int_3 = timeConvert(timeStamp3[11:16])
diffTime1 = (time_int_2 - time_int_1)
diffTime2 = (time_int_3 - time_int_2)

print(str(diffTime1))
print(str(diffTime2))