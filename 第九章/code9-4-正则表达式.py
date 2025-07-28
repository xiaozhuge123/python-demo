import re
# 查询字符串是否是纯数字
result = re.match(r'\d+', '123sff456asfd') # <re.Match object; span=(0, 3), match='123'>
print(result)

# 匹配身份证
result = re.match(r'^\d{17}(\d|X)$', '12345678901234567X')
print(result)

# 匹配手机号
result = re.match(r'^1\d{10}$', '12345678901')
print(result)

from my_package import my_tools

number = my_tools.is_phone_number('12345678901')
if number:
    print('手机号正确')
else:
    print('手机号错误')
