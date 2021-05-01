import tkinter as tk
from tkinter import ttk

root = tk.Tk()
container = ttk.Frame(root)
canvas = tk.Canvas(container, bg = 'red')
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

for i in range(50):
    ttk.Label(scrollable_frame, text="Sample scrolling label").pack()

container.place(x = 10, y = 20, height = 600, width = 1350)
canvas.place(x = 10, y= 0, height = 600, width = 1350)
scrollbar.place(x = 500, y = 0, height = 600)

root.mainloop()