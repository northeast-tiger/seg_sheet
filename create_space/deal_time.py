'''时间戳转北京时间，
和北京时间转时间戳'''
import time
from datetime import datetime

# 时间戳转北京时间
time_1 = 1601863976	    # 以2020/10/5 10:12:56为例子
time_tuple_1 = time.localtime(time_1)
bj_time = time.strftime("%Y/%m/%d %H:%M:%S", time_tuple_1)
print("北京时间：", bj_time)


# 北京时间转时间戳
str_time = "2020/10/05 10:12:56"
time_tuple_2 = time.strptime(str_time, "%Y/%m/%d %H:%M:%S")
time_stample = time.mktime(time_tuple_2)
print("时间戳：", int(time_stample))




# 北京时间转时间戳
deal_time = '1968/1/4 21:0:0'   # 待转换的时间
dateTime_p = datetime.strptime(deal_time, '%Y/%m/%d %H:%M:%S')
metTime = dateTime_p - datetime(1970, 1, 1)
date_tample= metTime.days * 24 * 3600 + metTime.seconds - 28800  # 换算成秒数
print("时间戳：",date_tample)


#时间戳转北京时间
import datetime
timestamp = -1893436000     # 待转换的时间戳
print(datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=timestamp+8*3600)) # 北京时间

print(type(datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=timestamp+8*3600)))