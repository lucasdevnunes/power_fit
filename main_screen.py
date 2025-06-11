import tkinter as tk
from config_loader import settings_loader


def open_main_screen(user_id, user_name):
    settings = settings_loader()
    theme = settings["theme"]

    root = tk.Tk()
    root.title("Painel Principal")
    root.geometry("800x600")
    root.configure(bg=theme["secondary_color"])

    tk.Label(root, text=f"Bem-vindo, {user_name}", font=(theme["font"], 24),
             bg=theme["secondary_color"], fg=theme["primary_color"]).pack(pady=40)

    def logout(event=None):
        from login_view import open_login_view
        root.destroy()
        open_login_view()
        

    btn_logout = tk.Button(root, text="Logout", command=logout, bg=theme["primary_color"], fg="white")
    btn_logout.pack(pady=20)
    root.focus_force()
    root.bind("<Return>", logout)

    root.mainloop()