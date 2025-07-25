while True:
    num = input('请输入一个式子：')
    try:
        if '+' in num:
            num_split = num.split('+')
            sum_num = int(num_split[0]) + int(num_split[1])
            print(sum_num)
        elif '-' in num:
            num_split = num.split('-')
            sum_num = int(num_split[0]) - int(num_split[1])
            print(sum_num)
        elif '*' in num:
            num_split = num.split('*')
            sum_num = int(num_split[0]) * int(num_split[1])
            print(sum_num)
        elif '/' in num:
            num_split = num.split('/')
            if int(num_split[1]) == 0:
                raise Exception('除数不能为0')
            sum_num = int(num_split[0]) / int(num_split[1])
            print(sum_num)
        else:
            print('请输入正确的式子')
    except Exception as e:
        print(e)