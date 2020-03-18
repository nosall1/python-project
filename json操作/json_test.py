#-*- coding:utf-8 -*-
import json
import time

if __name__ == '__main__':
    file_path='json.txt'
    file_obj=open(file_path,'r',encoding='utf-8')
    all_lines=file_obj.readlines()
    data={}
    key_value=0
    for line in all_lines:
        line_info=line.split(",")
        if line_info:
            info={"name":line_info[0],'url':line_info[1].replace('\n','')}
            data[key_value]=info
            key_value+=1

    file_obj.close()
    file=open("data.json",'w',encoding='utf-8')
    # 写入文件
    json.dump(data,file,ensure_ascii=False)

    # 关闭文件
    file.close()

    # 读取json文件
    with open('data.json', 'r') as f:
        data = json.load(f)

    # 打印json文件内容
    for i in data.keys():
        print(i,":",data[i])