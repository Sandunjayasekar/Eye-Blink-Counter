import tkinter as tk
from blink_counter import get_blink_count, REQUIRED_BLINK_COUNT
from tkinter import messagebox

root = tk.Tk()
root.title("Eye Blink Counter")


button = tk.Button(root, text="Calculating...")


def update_label():
    blink_count = get_blink_count()
    button.config(text=blink_count)
    print(f"Blink Count: {blink_count} || Required Blink Count: {REQUIRED_BLINK_COUNT}")
    if blink_count < REQUIRED_BLINK_COUNT:
        messagebox.showwarning("Get Relax", f"Your eye blink count is low")
    root.after(1, update_label)


update_label()

root.withdraw()

root.mainloop()
