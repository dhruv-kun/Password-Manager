import tkinter as tk

root = tk.Tk()

# def show():
# 	txt = account.get() + "\n" + password.get() + "\n" + key.get()
# 	msg.set(txt)
# 	text.update()

tk.Label(root, text="Account").grid(row=0)
tk.Label(root, text="Password").grid(row=1)
tk.Label(root, text="Key").grid(row=2)

account = tk.Entry(root)
key = tk.Entry(root)
password = tk.Entry(root)
account.grid(row=0, column=1)
password.grid(row=1, column=1)
key.grid(row=2, column=1)

bttn = tk.Button(root, text="Print")
bttn.grid(row=3, columnspan=2, padx=5, pady=5)
msg = tk.StringVar()
msg.set(" " * 200 + "\n" * 3)
text = tk.Message(root, bg="black", fg="green", textvariable=msg)
text.grid(row=4, rowspan=3, columnspan=2, pady=5)
root.mainloop()