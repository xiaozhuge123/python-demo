year = int(input('请输入一个年份：'))
if not year % 4 and year % 100 or not year % 400:
    print('闰年')
else:
    print('平年')