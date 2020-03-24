#-*- coding:utf-8 -*-
import asyncio


@asyncio.coroutine
def countdown(name,n):
    while n>0:
        print(f'Countdown[{name}]:{n}')
        yield from asyncio.sleep(1)
        n-=1

def main():
    loop=asyncio.get_event_loop()
    tasks=[
        countdown('A',10),countdown('B',5)
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
if __name__ == '__main__':
    main()