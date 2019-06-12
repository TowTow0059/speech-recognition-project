from tkinter import *


class Main(Frame):
    def get(self):
        # self.v.set('d')
        print(self.e.get())

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.v = StringVar()
        self.e = Entry(self, textvariable=self.v)
        self.b = Button(self, text='get', command=self.get)

        self.e.pack()
        self.b.pack()


if __name__ == '__main__':
    root = Tk()
    Main(root).pack()
    root.mainloop()
