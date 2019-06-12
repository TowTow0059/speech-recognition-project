from tkinter import *

root = Tk()


def CurSelet(event):
    widget = event.widget
    selection = widget.curselection()
    picked = widget.get(selection[0])
    print('selection: ', selection[0])
    print('picked: ', picked)
    widget.insert(selection[0], 'selection')


left = Listbox(root)

for i in range(20):
    left.insert(i, "{}".format(i))

left.pack(fill='both')
right = Listbox(root)
right.insert(END, "1")
right.insert(END, "2")
right.insert(END, "3")
right.pack(fill='both')

print(left.get(1))

left.bind('<<ListboxSelect>>', CurSelet)

left.pack(side='left', fill='both')
right.pack(side='right', fill='both')
root.mainloop()
