import time

'''
time.time() :
Returns the current time in seconds since the Unix epoch (Jan 1 1970).
'''
print(time.time())

print("-----------------------------------------------------------------------------")

'''
time.sleep(seconds) :
Pauses the program for the given number of seconds.
'''
time.sleep(1) # Sleeps (delay) for 1 seconds

print("-----------------------------------------------------------------------------")

'''
time.ctime() :
Converts seconds since epoch to a readable string.
'''
print(time.ctime()) # Gives current Day MM DD Time YYYY

print("-----------------------------------------------------------------------------")

'''
time.localtime() :
Returns local time as a struct_time object.
'''
t = time.localtime()
print(time.localtime())
print(t.tm_year, t.tm_mon, t.tm_mday)

print("-----------------------------------------------------------------------------")

'''
time.gmtime() :
Same as localtime() but returns UTC time.
'''
print(time.gmtime())

print("-----------------------------------------------------------------------------")

'''
time.strftime() :
Formats time into a custom string.
'''
print(time.strftime("%d-%m-%Y %H:%M:%S"))

print("-----------------------------------------------------------------------------")

'''
time.pref_counter() :
High-resolution timer for performance measurement.
'''
start = time.perf_counter()
# Logic
end = time.perf_counter() - start
print(end)

print("-----------------------------------------------------------------------------")

'''
time.process_time() :
Returns CPU time used by the process.
'''
print(time.process_time())

print("-----------------------------------------------------------------------------")

'''
time.monotonic() :
Returns a clock that never goes backword.
'''
print(time.monotonic())
