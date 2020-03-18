#-*- coding:utf-8 -*-

from threading import Thread
import tkinter
import tkinter.messagebox
import time
def main():
    class DownloadTaskHandler(Thread):
        def run(self):
            time.sleep(10)
            tkinter.messagebox.showinfo('提示','下载完成')
            # 启动过下载按钮
            button1.config(state=tkinter.NORMAL)

    def download():
        # 禁止下载按钮
        button1.config(state=tkinter.DISABLED)
        # 设置daemon参数将线程设置为守护线程(主程序退出就不再保留执行)
        # 在线程中处理耗时间的下载任务
        DownloadTaskHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('关于','111')

    top=tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost',1)

    panel=tkinter.Frame(top)
    button1=tkinter.Button(panel,text='下载',command=download)
    button1.pack(side='left')
    button2=tkinter.Button(panel,text='关于',command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()

if __name__ == '__main__':
    main()