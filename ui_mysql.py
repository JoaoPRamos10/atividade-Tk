import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

# Conexão com o banco de dados MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="escola"
)
cursor = conn.cursor()

def salvar_visita():
    nome = entry_nome.get()
    documento = entry_documento.get()
    motivo = entry_motivo.get()
    data_visita = entry_data.get()

    if not nome or not documento or not motivo or not data_visita:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

    try:
        datetime.strptime(data_visita, "%Y-%m-%d")
        cursor.execute("INSERT INTO visitantes (nome, documento, motivo, data_visita) VALUES (%s, %s, %s, %s)",
                       (nome, documento, motivo, data_visita))
        conn.commit()
        messagebox.showinfo("Sucesso", "Visita registrada com sucesso!")
        entry_nome.delete(0, tk.END)
        entry_documento.delete(0, tk.END)
        entry_motivo.delete(0, tk.END)
        entry_data.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar: {e}")

# Interface gráfica
root = tk.Tk()
root.title("Registro de Visitantes")

tk.Label(root, text="Nome:").grid(row=0, column=0)
entry_nome = tk.Entry(root, width=50)
entry_nome.grid(row=0, column=1)

tk.Label(root, text="Documento (RG ou CPF):").grid(row=1, column=0)
entry_documento = tk.Entry(root, width=50)
entry_documento.grid(row=1, column=1)

tk.Label(root, text="Motivo da Visita:").grid(row=2, column=0)
entry_motivo = tk.Entry(root, width=50)
entry_motivo.grid(row=2, column=1)

tk.Label(root, text="Data da Visita (YYYY-MM-DD):").grid(row=3, column=0)
entry_data = tk.Entry(root, width=50)
entry_data.grid(row=3, column=1)

tk.Button(root, text="Registrar Visita", command=salvar_visita).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
