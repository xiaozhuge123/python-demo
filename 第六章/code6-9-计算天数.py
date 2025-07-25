list1 = [0,31,28,30,31,30,31,30,31,31,30,31,31]
print(sum(list1))
date = input('请输入日期：')
date_split = date.split('-')
year = int(date_split[0])
month = int(date_split[1])
day = int(date_split[2])

if not year % 4 and year % 100 or not year % 400:
    list1[2] = 29
sum = 0
for i in range(month):
    sum += list1[i]
sum += day
print(sum)

