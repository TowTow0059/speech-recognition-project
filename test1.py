import tkinter as tk

root = tk.Tk()

lb = tk.Listbox(root, width=50, height=20)
lb2 = tk.Listbox(root, width=50, height=20)

vert = tk.Scrollbar(lb, orient="vertical")
hori = tk.Scrollbar(lb, orient=tk.HORIZONTAL)

lb.config(yscrollcommand=vert.set, xscrollcommand=hori.set)

vert.config(command=lb.yview)
hori.config(command=lb.xview)

vert.pack(side="right", fill="y")
hori.pack(side='bottom', fill='x')

lb.pack(side="left", fill="both", expand=True)
# lb2.pack(side="right", fill="both", expand=True)

# lb.insert(tk.END,
#           'asdsadaasdsadaasdsadaasdsadaasdsadaasdsadaasdsadaasdsadaasdsadaasdsadaasdsadaasdsadaasdsadaasdsadaasdsadaasdsadaasdsadaasdsadaasdsadaasdsada')
#
# for i in range(0, 100):
#     lb.insert("end", "item #%s" % i)
#     lb2.insert("end", "item #%s" % i)

root.mainloop()
