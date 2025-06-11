import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib
from config_loader import settings_loader
from main_screen import open_main_screen

def open_login_view():
    settings = settings_loader()
    theme = settings["theme"]

    def auth(event=None):
        login = entry_login.get()
        passw = hashlib.sha256(entry_passw.get().encode()).hexdigest()

        conn = sqlite3.connect(settings["db_path"])
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome FROM usuarios WHERE login=? AND senha=?", (login, passw))
        result = cursor.fetchone()
        conn.close()

        if result:
            user_id, name = result
            root.destroy()
            open_main_screen(user_id, name)
        else:
            messagebox.showerror("Erro", "Login ou senha incorretos.")

    root = tk.Tk()
    root.title(settings["system_name"])
    root.geometry("800x600")
    root.configure(bg=theme["secondary_color"])

    tk.Label(root, text="LOGIN", font=(theme["font"], 30), bg=theme["secondary_color"], fg=theme["primary_color"]).pack(pady=70)
    tk.Label(root, text="Usuário:", bg=theme["secondary_color"], fg=theme["text_color"]).pack()
    entry_login = tk.Entry(root)
    entry_login.pack()
    tk.Label(root, text="Senha:", bg=theme["secondary_color"], fg=theme["text_color"]).pack()
    entry_passw = tk.Entry(root, show="*")
    entry_passw.pack()
    tk.Button(root, text="Entrar", bg=theme["primary_color"], fg="white", command=auth).pack(pady=20)

    root.bind("<Return>", auth)

    root.mainloop()