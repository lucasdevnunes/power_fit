import tkinter as tk
from app.database.database import criar_tabelas

criar_tabelas()

class App:
    def __init__(self, master=None):
        pass
root = tk.Tk()
App(root)
root.mainloop()
