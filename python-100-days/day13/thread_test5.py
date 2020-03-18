#-*- coding:utf-8 -*-
from multiprocessing import Queue,Process
from time import time


def task_handler(curr_list,result_queue):
    total=0
    for num in curr_list:
        total+=num
    result_queue.put(total)


def main():
    process=[]
    number_list=[x for x in range(1,100000001)]
    result_queue=Queue()
    index=0
    # 启动8个进程将数据切片后进行运算
    for _ in range(8):
        p=Process(target=task_handler,args=(number_list[index:index+12500000],result_queue))
        index+=12500000
        process.append(p)
        p.start()

    # 开始记录所有进程执行完成花费时间
    start=time()
    for p in process:
        p.join()

    # 合并执行结果
    total=0
    while not result_queue.empty():
        total+=result_queue.get()
    print(total)
    end=time()
    print('Execution time: ', (end - start), 's', sep='')

if __name__ == '__main__':
    main()