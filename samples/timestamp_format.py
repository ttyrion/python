from datetime import datetime

def string2timestamp(strtime):
    dt = datetime.strptime(strtime, "%Y-%m-%d %H:%M:%S")
    timestamp = int(dt.timestamp())
    return timestamp

def timestamp2string(timestamp):
    dt = datetime.fromtimestamp(timestamp)
    string_time = dt.strftime("%Y-%m-%d %H:%M:%S")
    return string_time
    
#字符串转时间戳
test = "2017-11-06 10:25:59"
timestamp = string2timestamp(test)
print("timestamp: %d" % timestamp)

#时间戳再转回字符串
string_time = timestamp2string(timestamp)
print("time: %s " % string_time)