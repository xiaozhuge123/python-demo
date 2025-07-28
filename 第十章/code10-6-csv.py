import csv

# 读取
# with open('data.csv','r',encoding='utf-8') as f:
#     cf = csv.reader(f)
#     header = next(cf)
#     score = []
#     for row in cf:
#         score.append(int(row[2]))
#     print('平均分为%.2f' %(sum(score)/len(score)))

# 写入
with open('data.csv', 'a', encoding='utf-8') as f:
    w = csv.writer(f)
    # w.writerow(['as','java',60])
    w.writerows([['ed','python',60],['rf','java',80],['bg','html',78]])