import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from MTU import *


class Window(object):

    def __init__(self):
        root = tk.Tk()
        root.minsize(580, 320)  # 窗口大小
        root.resizable(width=False, height=False)  # False窗口大小不可变

        root.title('MTU嗅探')  # 窗口标题

        label1 = Label(text='IP地址：')  # 标签
        label1.place(x=10, y=10, width=80, height=25)  # 确定位置

        self.line_text = Entry(root)  # 单行文本输入
        self.line_text.place(x=80, y=10, width=420, height=25)

        button = Button(text='开始查询', command=self.inquiry)  # 按钮
        button.place(x=500, y=10, width=60, height=25)

        label2 = Label(text='查询结果:')
        label2.place(x=10, y=100, width=80, height=20)
        self.text = Text(root)  # 多行文本显示
        self.text.place(x=80, y=50, width=480, height=240)

        root.mainloop()  # 主循环

    '''查询'''

    def inquiry(self):

        ipaddr = self.line_text.get()  # 获取输入的内容
        self.text.delete(1.0, tk.END)  # 用于删除后续显示的文件
        self.text.insert('insert', '\n请稍等...\n')
        if not ipaddr:  # 没有输入句子就查询，会出现弹窗警告
            messagebox.showinfo("Warning", '请先输入需要查询的IP地址!')
        else:

            mtu = 1500
            while mtu > 0:
                res = mtu_one(mtu, ipaddr)
                if res == 1 or res is None:
                    mtu -= 1
                elif res == 2:
                    infos = []
                    print('this way min mtu: %d' % mtu)
                    infos.append(f'{ipaddr}的MTU值为：{mtu}\n')
                    # 查找到的内容插入文本，并显示
                    self.text.insert('insert', '\n\n\n'.join(infos)[:-1])
                    break

if __name__ == '__main__':
    Window()
