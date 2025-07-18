import tkinter as tk
from tkinter import ttk
from config_loader import settings_loader
from views.dashboard_view import open_dashboard


def open_main_screen(user_id, user_name):
    settings = settings_loader()
    theme = settings["theme"]

    root = tk.Tk()
    root.title(settings["system_name"])
    root.geometry("800x600")
    root.configure(bg=theme["secondary_color"])

    style = ttk.Style()
    style.theme_use("default")  # ou "clam", se quiser algo mais customizável

    style.configure("Custom.TNotebook.Tab",
        background=theme["tertiary_color"],
        foreground="white",
        padding=[10, 5]
    )

    style.map("Custom.TNotebook.Tab",
        background=[("selected", theme["tertiary_color"])],
        foreground=[("selected", "white")]
    )

    notebook = ttk.Notebook(root, style="Custom.TNotebook")
    notebook.pack(fill='both', expand=True)

    tab_dashboard = tk.Frame(notebook, bg=theme["tertiary_color"])
    notebook.add(tab_dashboard, text="Dashboard")
    
    open_dashboard(tab_dashboard, user_name)

    tab_alunos = tk.Frame(notebook, bg=theme["tertiary_color"])
    notebook.add(tab_alunos, text="Alunos")

    label_alunos = tk.Label(tab_alunos, text="Gestão de alunos", bg=theme["tertiary_color"], fg=theme["text_color"])
    label_alunos.pack()

    tab_financeiro = tk.Frame(notebook, bg=theme["tertiary_color"])
    notebook.add(tab_financeiro, text="Financeiro")

    label_fin = tk.Label(tab_financeiro, text="Relatórios financeiros", bg=theme["tertiary_color"], fg=theme["text_color"])
    label_fin.pack()

    def logout(event=None):
        from login_view import open_login_view
        root.destroy()
        open_login_view()
        

    btn_logout = tk.Button(root, text="Logout", command=logout, bg=theme["primary_color"], fg="white")
    btn_logout.pack(pady=20)

    root.mainloop()