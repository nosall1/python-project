import csv

uids={}
# 读取csv文件
with open("csv_test.csv", "r") as f:
    for line in f.readlines():
        line = line.strip('\n')  #去掉列表中每一个元素的换行符
        lines=line.split(',') # 以,分割
        uid=lines[0]
        if uid not in uids.keys():
            uids[uid]=lines[1:]


abc=open('csv_after.csv','a+')

csv_write = csv.writer(abc)

# 写入表头
row=[]
row.append("title_1")
row.append('title_2')
row.append('title_3')
row.append('title_4')
row.append('title_5')
csv_write.writerow(row)
# 写文件
for uid in uids.keys():
    row=[]
    datas=uids[uid]
    row.append(uid)
    for data in datas:
        row.append(data)
    # row.append(data)
    csv_write.writerow(row)
