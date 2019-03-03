import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file='python-logo-small.gif')

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interace
exists to allow additional image file
formats to be added easily."""

w = tk.Label(root,
             compound = tk.CENTER,
             text=explanation,
             image=logo).pack(side="right")

root.mainloop()
