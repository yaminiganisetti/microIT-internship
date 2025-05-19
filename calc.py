import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calc Lite")

entry = tk.Entry(root, width=20, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "0", "C", "=", "/"
]

row = 1
col = 0

for b in buttons:
    def cmd(x=b):
        if x == "=":
            calculate()
        elif x == "C":
            entry.delete(0, tk.END)
        else:
            entry.insert(tk.END, x)

    tk.Button(root, text=b, width=5, height=2, font=("Arial", 14), command=cmd).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()