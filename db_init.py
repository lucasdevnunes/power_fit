import sqlite3
import os

db_path = os.path.join("db", "studio.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    login TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT,
    nascimento DATE,
    plano_inicio DATE,
    plano_validade DATE,
    observacoes TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS fichas_treino (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno_id INTEGER,
    grupo_muscular TEXT,
    exercicio TEXT,
    series TEXT,
    repeticoes TEXT,
    observacoes TEXT,
    data DATE,
    FOREIGN KEY (aluno_id) REFERENCES alunos (id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS presencas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno_id INTEGER,
    data DATE,
    FOREIGN KEY (aluno_id) REFERENCES alunos (id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS pagamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno_id INTEGER,
    valor REAL,
    data_pagamento DATE,
    descricao TEXT,
    FOREIGN KEY (aluno_id) REFERENCES alunos (id)
)
""")

import hashlib
pw = hashlib.sha256("admin123".encode()).hexdigest()

cursor.execute("""
INSERT OR IGNORE INTO usuarios (nome, login, senha) 
VALUES (?, ?, ?)
""", ("Administrador", "admin", pw))

conn.commit()
conn.close()

print("Banco de dados criado com sucesso!")
