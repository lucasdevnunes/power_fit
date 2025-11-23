from dotenv import load_dotenv
import sqlite3
import os

load_dotenv()

DB_NAME = os.getenv("DB_NAME", "powerfit.db")

def conexao_db():
    return sqlite3.connect(DB_NAME)

def criar_tabelas():
    con = conexao_db()
    con.execute("PRAGMA foreign_keys = ON")
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS alunos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT UNIQUE,
            telefone TEXT,
            status TEXT DEFAULT 'ativo',
            data_inicio TEXT,
            observacoes TEXT
                )
                """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS presencas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aluno_id INTEGER NOT NULL,
            data TEXT NOT NULL,
            FOREIGN KEY(aluno_id) REFERENCES alunos(id) 
                )
                """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS pagamentos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aluno_id INTEGER NOT NULL,
            valor REAL NOT NULL,
            data_pagamento TEXT NOT NULL,
            referencia_mes TEXT NOT NULL,
            forma_pagamento TEXT,
            FOREIGN KEY(aluno_id) REFERENCES alunos(id)
                )
                """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS medidas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aluno_id INTEGER NOT NULL,
            data TEXT NOT NULL,
            peso REAL,
            peito REAL,
            cintura REAL,
            quadril REAL,
            braco_direito REAL,
            braco_esquerdo REAL,
            coxa_direita REAL,
            coxa_esquerda REAL,
            FOREIGN KEY(aluno_id) REFERENCES alunos(id)
                )
                """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS saidas_financeiras(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            data TEXT NOT NULL,
            categoria TEXT
                )
                """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS treinos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aluno_id INTEGER NOT NULL,
            data TEXT NOT NULL,
            treino TEXT NOT NULL,
            observacoes TEXT,
            FOREIGN KEY(aluno_id) REFERENCES alunos(id)
                )
                """)
    
    con.commit()
    con.close()
