
# Question 1
import json
import time
import datetime
import matplotlib.pyplot as plt
import numpy as np

  
# Opening JSON file
f = open('Elga.json')
  
# returns JSON object as 
# a dictionary
dic = json.load(f)
print(type(dic))

#Question 2
print(dic['captured_data'].keys())
print(dic['captured_data']['hr'].keys())
print(dic['captured_data']['slp'].keys())
print(dic['captured_data']['act'].keys())
print(dic['captured_data']['bat'].keys())
print(dic['captured_data']['err'].keys())


print(len(dic['captured_data']['hr']['RR in ms']))
print(len(dic['captured_data']['hr']['HR in BPM']))
time_in_millis=dic['captured_data']['hr']['RR in ms']
bpm=dic['captured_data']['hr']['HR in BPM']

# Python code to get the Cumulative sum of a list

new_list=[]
j=0
for i in range(0,len(time_in_millis)):
    j+=time_in_millis[i]
    new_list.append(j)
     
milli_second=new_list[-1]
print(milli_second)

# ms=datetime.datetime.fromtimestamp(milli_second/1000.0)
# print(ms)

print(dic['Start_date_time'])
print(dic['session_finish_time'])

string = "04 May 2022  01:06:48.000"
date = datetime.datetime.strptime(string, "%d %b %Y  %H:%M:%S.%f")

print(date)





# results=[]
# for i in range(len(time_in_millis)):
#     seconds=(time_in_millis[i]/bpm[i]) if bpm[i] != 0 else 0
#     results.append(seconds)
# print(results)

 
# def convert(sec):
#     return time.strftime("%H:%M:%S", time.gmtime(ist_value))
     

# result=[]
# for i in range(len(results)):
#     ist_value = results[i]
#     istvalue=convert(ist_value)
#     result.append(istvalue)
# # print(result)
# print(result[0:15])    

#Question 3
#converted time is result
#heart rate is bpm
# import pdb;pdb.set_trace()

# plt.plot(result, bpm)  # Plot the chart
# plt.show()  # display

#Question 4
# step_count=dic['captured_data']['act']['step count']
# print(len(step_count))
# print(len(bpm))
# for i in range(len(step_count)):
#     if step_count>5:
#         plt.plot(i,bpm[i],color='red',marker='.')

# plt.show()

from datetime import datetime
from pytz import timezone
format = "%Y-%m-%d %H:%M:%S %Z%z"
# Current time in UTC
now_utc = datetime.now(timezone('UTC'))
print(now_utc.strftime(format))
# Convert to Asia/Kolkata time zone
now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
print(now_asia.strftime(format))

# import datetime
# t = datetime.time(time_obj)
# c=int(datetime.timedelta(hours=t.hour, minutes=t.minute, seconds=t.second).total_seconds())

# def get_sec(time_str):
#     """Get seconds from time."""
#     h, m, s = time_str.split(':')
#     return int(h) * 3600 + int(m) * 60 + int(s)
# print(get_sec(time_obj))    

#milli converted to h m s


# converted_time=time_obj+datetime_milli_converted
# # print(converted_time)

# time_converted=time_obj.hour*10000 +time_obj.minute*100 +time_obj.second
# print(time_converted)
# # print(time_converted)
# tc=float(time_converted)
# print(type(tc))

# converted_time=tc+Seconds
# print(converted_time)
# def convert(seconds):
#     seconds = seconds % (24 * 3600)
#     hour = seconds // 3600
#     seconds %= 3600
#     minutes = seconds // 60
#     seconds %= 60
     
#     return "%d:%02d:%02d" % (hour, minutes, seconds)
     
# Driver program
# n = converted_time
# time_to_plot=convert(n)
# print(time_to_plot)

# print("Time in Date time Format: ",datetime.fromtimestamp(time_to_plot//1000))


# plt.plot(time_to_plot,bpm,linewidth=0.5)
# plt.title('Heart rate Signal')
# plt.xlabel('time')
# plt.ylabel('heart rate')
# plt.figure(figsize=(1,1))
# plt.show()
# plt.scatter(time_to_plot,dic['captured_data']['hr']['HR in BPM'],color = 'red')

# millis = int(converted_time)
# seconds=(millis/1000)%60
# seconds = int(seconds)
# minutes=(millis/(1000*60))%60
# minutes = int(minutes)
# hours=(millis/(1000*60*60))%24
# milli_converted="%d:%d:%d" % (hours, minutes, seconds)
# print(type(milli_converted))
# print(milli_converted)
# datetime_milli_converted = datetime.strptime(milli_converted, '%H:%M:%S').time()
# print(datetime_milli_converted)
# print(type(datetime_milli_converted))

# from datetime import datetime, timedelta

# n_seconds = milli_second
# date = time_obj + timedelta(hours=n_seconds)
# print(date)
#to append the seconds to start time
# from datetime import datetime
# from datetime import timedelta
# d1 = datetime(time_obj)
# d2 = d1 + timedelta(datetime_milli_converted)
# print(d2)

# print("Time in Date time Format: ",datetime.fromtimestamp(time_converted//1000))


