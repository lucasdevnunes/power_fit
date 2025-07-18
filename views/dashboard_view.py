import tkinter as tk
from tkinter import ttk
from datetime import date, timedelta
import sqlite3
from config_loader import settings_loader

def get_dashboard_stats(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    hoje = date.today().isoformat()
    daqui7 = (date.today() + timedelta(days=7)).isoformat()
    c.execute("SELECT COUNT(*) FROM alunos WHERE plano_validade>=?", (hoje,))
    ativos = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM presencas WHERE data=?", (hoje,))
    presencas = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM fichas_treino WHERE data=?", (hoje,))
    treinos = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM alunos WHERE plano_validade BETWEEN ? AND ?", (hoje, daqui7))
    vencendo = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM alunos WHERE plano_validade<?", (hoje,))
    vencidos = c.fetchone()[0]
    conn.close()
    return ativos, presencas, treinos, vencendo, vencidos

def open_dashboard(frame_pai, user_name):
    from config_loader import settings_loader
    settings = settings_loader()
    theme = settings["theme"]

    for widget in frame_pai.winfo_children():
        widget.destroy()

    ativos, presencas, treinos, vencendo, vencidos = get_dashboard_stats(settings["db_path"])

    frame_top = tk.Frame(frame_pai, bg=theme["secondary_color"])
    frame_top.pack(pady=20)
    tk.Label(frame_top, text=f"👥 Ativos: {ativos}", bg=theme["secondary_color"], fg=theme["text_color"], font=(theme["font"], 14)).pack(side="left", padx=20)
    tk.Label(frame_top, text=f"📆 Hoje: {presencas}", bg=theme["secondary_color"], fg=theme["text_color"], font=(theme["font"], 14)).pack(side="left", padx=20)
    tk.Label(frame_top, text=f"💬 Treinos hoje: {treinos}", bg=theme["secondary_color"], fg=theme["text_color"], font=(theme["font"], 14)).pack(side="left", padx=20)

    frame_mid = tk.Frame(frame_pai, bg=theme["secondary_color"])
    frame_mid.pack(pady=10)
    tk.Label(frame_mid, text=f"⚠️ Vencendo em breve: {vencendo}", bg=theme["secondary_color"], fg=theme["text_color"], font=(theme["font"], 14)).pack(side="left", padx=20)
    tk.Label(frame_mid, text=f"⛔ Vencidos: {vencidos}", bg=theme["secondary_color"], fg=theme["text_color"], font=(theme["font"], 14)).pack(side="left", padx=20)

    frame_bot = tk.Frame(frame_pai, bg=theme["secondary_color"])
    frame_bot.pack(pady=30)
    ttk.Button(frame_bot, text="➕ Novo Aluno").pack(side="left", padx=10)
    ttk.Button(frame_bot, text="📋 Registrar Presença").pack(side="left", padx=10)
    ttk.Button(frame_bot, text="🏋️ Fichas de Treino").pack(side="left", padx=10)
