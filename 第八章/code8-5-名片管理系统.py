cards = []
def menu():
    print('*' * 30)
    print('''欢迎使用【名片管理系统】
    1、新建名片
    2、显示全部
    3、查询名片
    4、修改名片
    5、删除名片
    0、退出系统''')
    print('*' * 30)

def new_card(name,phone,qq,email):
    user = {
        'name': name,
        'phone': phone,
        'qq': qq,
        'email': email
    }
    cards.append(user)
    return True


def show_card():
    for user in cards:
        print(user)


def query_card(kw):
    for card in cards:
        for k,v in card.items():
            if kw == v:
                return card
    else:
        return False


menu()


def exit_card():
    print('欢迎下次使用【名片管理系统】')


def card_index(kw):
    for i in range(len(cards)):
        card = cards[i]
        for k,v in card.items():
            if kw == v:
                return i
    else:
        return False

def modify_card(kw, name, phone, qq, email):
    card = query_card(kw)
    if name != card['name']:
        card['name'] = name
    if phone != card['phone']:
        card['phone'] = phone
    if qq != card['qq']:
        card['qq'] = qq
    if email != card['email']:
        card['email'] = email


def del_card():
    index = card_index(kw)
    if index:
        del cards[index]
        return True
    else:
        return False


while True:
    op = input('请输入你要操作的序号：')
    if op == '1':
        name = input('请输入你的名字：')
        phone = input('请输入你的手机号：')
        qq = input('请输入你的qq号：')
        email = input('请输入你的邮箱：')
        flag = new_card(name, phone, qq, email)
        if flag:
            print('成功新建名片！')
        else:
            print('新建名片失败！')
    elif op == '2':
        show_card()
    elif op == '3':
        kw = input('请输入你需要查询的关键字：')
        card = query_card(kw)
        if card:
            print(card)
        else:
            print('没有查询到相关的名片数据')
    elif op == '4':
        kw = input('请输入你需要查询的关键字：')
        name = input('请输入你需要修改的名字：')
        phone = input('请输入你需要修改的手机号：')
        qq = input('请输入你需要修改的qq号：')
        email = input('请输入你需要修改的邮箱：')
        card = query_card(kw)
        if card:
            card1 = modify_card(kw, name, phone, qq, email)
            print('更新成功')
        else:
            print('没有查询到相关的名片数据')
    elif op == '5':
        kw = input('请输入你需要删除的关键字：')
        b = del_card()
        if b:
            print('删除成功')
        else:
            print('删除失败')
    elif op == '0':
        exit_card()
        break
    else:
        print('请重试')