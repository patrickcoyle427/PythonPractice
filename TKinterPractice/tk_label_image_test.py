import tkinter as tk

root = tk.Tk()
# sets the root of the tkinter window
# creates an instance of the tk.Tk() class
logo = tk.PhotoImage(file='python-logo-small.gif')

w1 = tk.Label(root, image=logo).pack(side='right')

explanation = '''At present, only GIF and PPM/PGM formats
are supported, but an interace
exists to allow additional image file
formats to be added easily.'''

w2 = tk.Label(root,
              justify=tk.LEFT,
              padx = 10,
              text=explanation).pack(side='left')

root.mainloop()
# runs the mainloop method of the root class

