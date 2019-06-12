import os
import tkinter as tk
from tkinter import filedialog
import pickle

import PairFile
import controller

pair_file = []
list_area = None
statusbar_area = None


# saying = None


def popupmsg(msg, title):
    popup = tk.Tk()
    popup.title(title)
    tk.Label(popup, text=msg, width=40, padx=5, pady=5).pack()
    tk.Button(popup, text='Ok', command=popup.destroy, width=20, padx=5, pady=5).pack(fill='x')
    popup.mainloop()


class Button(tk.Frame):
    def speak(self):
        controller.setFile(pair_file)
        controller.command()

    def quit(self):
        exit()

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        speak_btn = tk.Button(self, text='Speak', width=26, command=self.speak)

        quit_btn = tk.Button(self, text='Quit', width=26, command=self.quit)

        speak_btn.pack(side='left', fill='x')
        quit_btn.pack(side='right', fill='x')


class Adding(tk.Frame):
    def confirm(self):
        global pair_file
        if self.file_path.get() == "":
            popupmsg("Choose a file.", '!!!')
        elif self.keyword_entry.get() == "":
            popupmsg("Pick a keyword.", '!!!')
        else:
            newfile = PairFile.PairFile(path=self.file_path.get(), keyword=self.keyword_entry.get(), index=self.index)

            if newfile.is_existed(pair_file) == 4:
                popupmsg("File is existed.", 'Error!!!')
            elif newfile.is_existed(pair_file) == 5:
                popupmsg("Keyword is existed.", 'Error!!!')
            else:
                global list_area
                global statusbar_area

                key = self.keyword_entry.get()

                pair_file.append(newfile)

                name_file = str(self.index) + '. ' + pair_file[len(pair_file) - 1].name
                key_file = str(self.index) + '. \'' + key + '\''

                # cho index va status len trcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

                self.index += 1

                if self.index == 1:
                    status = "1 file..."
                else:
                    status = str(self.index) + " files..."

                Statusbar.update(statusbar_area, status)
                List.update(list_area, name_file,
                            key_file)

    def addfile(self):
        self.file_path.set(filedialog.askopenfilename())

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.index = 0
        self.file_path = tk.StringVar()

        self.file_entry = tk.Entry(self, state='disable', textvariable=self.file_path, width=43)
        self.keyword_entry = tk.Entry(self, width=43)

        self.add_btn = tk.Button(self, text='Add File', command=self.addfile, width=10)
        self.keyword_btn = tk.Button(self, text='Add Keyword', width=10)
        self.confirm_btn = tk.Button(self, text='Confirm', command=self.confirm)

        self.add_btn.grid(row=0, column=0, padx=5)
        self.keyword_btn.grid(row=1, column=0, padx=5)
        self.file_entry.grid(row=0, column=1, ipadx=13)
        self.keyword_entry.grid(row=1, column=1, ipadx=13)
        self.confirm_btn.grid(row=2, column=0, columnspan=2)


class List(tk.Frame):
    def update(self, file, keyword):
        self.files.insert(tk.END, file)
        self.keywords.insert(tk.END, keyword)

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.files = tk.Listbox(self, bd=3, width=30)
        self.keywords = tk.Listbox(self, bd=3, width=30)

        self.file_label = tk.Label(self, text='Files', bd=3, relief=tk.RIDGE, width=26)
        self.keyword_label = tk.Label(self, text='Keywords', bd=3, relief=tk.RIDGE, width=26)

        self.file_label.grid(row=0, column=0)
        self.keyword_label.grid(row=0, column=1)

        self.files.grid(row=1, column=0, ipadx=3, ipady=3)
        self.keywords.grid(row=1, column=1, ipadx=3, ipady=3)


class Statusbar(tk.Frame):
    def update(self, text):
        self.status_text.set(text)

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.status_text = tk.StringVar()
        self.status_text.set('0 file...')

        self.status = tk.Label(master=self, textvariable=self.status_text)

        self.status.pack(side=tk.LEFT)


# TODO saying
# class Saying(tk.Frame):
#     def update(self, text):
#         # global saying
#         self.saying.set(text)
#         return self
#
#     def __init__(self, master, *args, **kwargs):
#         tk.Frame.__init__(self, master, *args, **kwargs)
#
#         self.saying = tk.StringVar()
#         self.saying.set('Welcome')
#
#         self.text = tk.Label(master=self, textvariable=self.saying)
#
#         self.text.pack()


class Menu:
    def save(self):
        return

    def __init__(self, master):
        self = tk.Menu(master)
        master.config(menu=self)
        self.submenu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="file", menu=self.submenu)
        self.submenu.add_command(label="new project...")
        self.submenu.add_command(label="save", command=self.save)
        self.submenu.add_separator()
        self.submenu.add_command(label="exit", command=exit)


class Main(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        global list_area
        list_area = List(self, bd=3, relief=tk.SUNKEN)

        self.list = list_area
        self.adding = Adding(self, bd=3, relief=tk.SUNKEN)
        self.buttons = Button(self, bd=3, relief=tk.SUNKEN)

        self.list.pack(side='top', fill='both', expand=1)
        self.adding.pack(padx=2, pady=2, fill='both', expand=1)
        self.buttons.pack(side='bottom', fill='x', expand=1)


def application():
    root = tk.Tk()
    root.title("SR Project")
    root.resizable(False, False)
    Menu(root)
    Main(root, bd=5, relief=tk.SUNKEN).pack(fill='both', expand=1)

    global statusbar_area
    statusbar_area = Statusbar(root, bd=5, relief=tk.SUNKEN)
    # global saying
    # saying = Saying(root, bd=5, relief=tk.SUNKEN)
    #
    # saying.pack(fill=tk.X)
    statusbar_area.pack(side=tk.BOTTOM, fill=tk.X)
    root.mainloop()


if __name__ == '__main__':
    application()
