#-*- coding:utf-8 -*-
"""
异步I/O - async / await
"""
# 指定范围的数字生成器
import asyncio


def num_generator(m,n):
    yield from range(m,n+1)

# 素数过滤器
async def prime_filter(m,n):
    primes=[]
    for i in num_generator(m,n):
        flag=True
        for j in range(2,int(i**0.5+1)):
            if i%j==0:
                flag=False
                break
        if flag:
            print('Prime=>',i)
            primes.append(i)
        await asyncio.sleep(0.001)

    return tuple(primes)
# 平方映射器
async def square_mapper(m,n):
    squares=[]
    for i in num_generator(m,n):
        print('Square =>',i*i)
        squares.append(i*i)

        await asyncio.sleep(0.001)

    return squares

def main():
    # 获得系统默认的事件循环获得系统默认的事件循环
    loop=asyncio.get_event_loop()
    # async.gather返回的是已完成Task的result
    future=asyncio.gather(prime_filter(2,100),square_mapper(1,100))
    # 注册一个回调函数
    future.add_done_callback(lambda x:print(x.result()))
    # 等待future运行完成
    loop.run_until_complete(future)
    loop.close()
if __name__ == '__main__':
    main()