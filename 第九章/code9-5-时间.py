import time,my_package.my_tools

time1 = time.time()
print(time1)

time2 = time.localtime()
print(time2)

time3 = time.strftime('%Y-%m-%d %H:%M:%S', time2)
print(time3)
print('*' * 20)

current_time = my_package.my_tools.getCurrentTime()
print(current_time)
