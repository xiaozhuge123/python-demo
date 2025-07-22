weight = float(input('请输入你的体重，单位kg:'))
height = float(input('请输入你的身高，单位米:'))
bmi = weight / (height * height)
if bmi < 18.5:
    print('过瘦')
elif bmi < 23.9:
    print('正常')
else:
    print('过胖')

# 日期判断
num = int(input('请输入数字：'))
if num == 1:
    print('星期一')
elif num == 2:
    print('星期二')
elif num == 3:
    print('星期三')
elif num == 4:
    print('星期四')
elif num == 5:
    print('星期五')
elif num == 6:
    print('星期六')
elif num == 7:
    print('星期天')
else:
    print('other')