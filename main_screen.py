import tkinter as tk
from tkinter import ttk
from config_loader import settings_loader


def open_main_screen(user_id, user_name):
    settings = settings_loader()
    theme = settings["theme"]

    root = tk.Tk()
    root.title("Painel Principal")
    root.geometry("800x600")
    root.configure(bg=theme["secondary_color"])

    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    tab_dashboard = tk.Frame(notebook)
    notebook.add(tab_dashboard, text="Dashboard")

    label_dash = tk.Label(tab_dashboard, text=f"Bem-vindo, {user_name}!", font=("Arial", 16))
    label_dash.pack(pady=20)

    tab_alunos = tk.Frame(notebook)
    notebook.add(tab_alunos, text="Alunos")

    label_alunos = tk.Label(tab_alunos, text="Gestão de alunos")
    label_alunos.pack()

    tab_financeiro = tk.Frame(notebook)
    notebook.add(tab_financeiro, text="Financeiro")

    label_fin = tk.Label(tab_financeiro, text="Relatórios financeiros")
    label_fin.pack()

    def logout(event=None):
        from login_view import open_login_view
        root.destroy()
        open_login_view()
        

    btn_logout = tk.Button(root, text="Logout", command=logout, bg=theme["primary_color"], fg="white")
    btn_logout.pack(pady=20)

    root.mainloop()