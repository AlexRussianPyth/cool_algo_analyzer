import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

from graph import Graph
from numerical import BigSlice

def get_n():
    started = start_n.get()
    stopped = stop_n.get()
    new_data = BigSlice(int(started),int(stopped))
    new_graph = Graph(new_data)

# GUI
win = tk.Tk()
win.title("Algo Analyzer")
win.config(bg="#ffdf6b", padx=20, pady=20)

lbl_start = tk.Label(text="Start N", bg="#ffdf6b")
lbl_start.grid(row=0, column=0)
lbl_stop = tk.Label(text="Stop N", bg="#ffdf6b")
lbl_stop.grid(row=0, column=1)

start_n = tk.Entry()
start_n.grid(row=1, column=0)
stop_n = tk.Entry()
stop_n.grid(row=1, column=1)

btn = tk.Button(text="Make Graph", command=get_n)
btn.grid(row=2, column=0, columnspan=2, stick="we", pady=10)

win.mainloop()

