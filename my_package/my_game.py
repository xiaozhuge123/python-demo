# 石头剪刀布
import random

def game1():
    player_score,computer_score = 0,0
    for i in range(3):
        plager = input('请输入你的选择：')
        computer = random.choice(['石头','剪刀','布'])
        print('电脑的选择：', computer)
        if plager == computer:
            player_score += 1
            computer_score += 1
        elif (plager == '石头' and computer == '剪刀') or (plager == '剪刀' and computer == '布') or (plager == '布' and computer == '石头'):
            player_score += 1
        else:
            computer_score += 1
    if player_score > computer_score:
        print('选手赢了')
    elif player_score == computer_score:
        print('平局')
    else:
        print('电脑赢了')


# 猜数字
def guess_num(start,end):
    num = random.randint(start,end)
    while True:
        num1 = int(input('请输入你的数字：'))
        if num1 > num:
            print('猜大了')
        elif num1 < num:
            print('猜小了')
        else:
            print('恭喜你猜中了')
            break



