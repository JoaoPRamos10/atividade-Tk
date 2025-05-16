import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
from datetime import datetime

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="controle_visitantes" 
    )

def inserir_visitante():
    nome = entry_nome.get()
    documento = entry_documento.get()
    motivo = entry_motivo.get()
    data_visita = entry_data_visita.get()

    if nome and documento and motivo and data_visita:

        try:
            data_visita_formatada = datetime.strptime(data_visita, "%d/%m/%Y").date()
        except ValueError:
            messagebox.showwarning("Atenção", "Data no formato inválido. Use dd/mm/aaaa!")
            return

        try:
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO visitantes (nome, documento, motivo_visita, data_visita)
                VALUES (%s, %s, %s, %s)
            """, (nome, documento, motivo, data_visita_formatada))
            conn.commit()
            conn.close()

            messagebox.showinfo("Sucesso", "Visitante registrado com sucesso!")
            limpar_campos()

            listar_visitantes()

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
    else:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_documento.delete(0, tk.END)
    entry_motivo.delete(0, tk.END)
    entry_data_visita.delete(0, tk.END)

def listar_visitantes():
    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM visitantes")
        visitantes = cursor.fetchall()
        conn.close()

        for i in tree.get_children():
            tree.delete(i)

        for visitante in visitantes:
            # Converte a data para o formato dd/mm/yyyy
            data_visita = visitante[4].strftime("%d/%m/%Y") if visitante[4] else ""
            tree.insert("", "end", values=(visitante[0], visitante[1], visitante[2], visitante[3], data_visita))

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

root = tk.Tk()
root.title("Controle de Visitantes")
root.geometry("600x400")

frame = tk.Frame(root)
frame.pack(pady=20)

label_nome = tk.Label(frame, text="Nome:")
label_nome.grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(frame)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

label_documento = tk.Label(frame, text="Documento (RG/CPF):")
label_documento.grid(row=1, column=0, padx=10, pady=5)
entry_documento = tk.Entry(frame)
entry_documento.grid(row=1, column=1, padx=10, pady=5)

label_motivo = tk.Label(frame, text="Motivo da Visita:")
label_motivo.grid(row=2, column=0, padx=10, pady=5)
entry_motivo = tk.Entry(frame)
entry_motivo.grid(row=2, column=1, padx=10, pady=5)

label_data_visita = tk.Label(frame, text="Data da Visita (dd/mm/yyyy):")
label_data_visita.grid(row=3, column=0, padx=10, pady=5)
entry_data_visita = tk.Entry(frame)
entry_data_visita.grid(row=3, column=1, padx=10, pady=5)

btn_inserir = tk.Button(root, text="Registrar Visitante", command=inserir_visitante)
btn_inserir.pack(pady=10)

tree = ttk.Treeview(root, columns=("ID", "Nome", "Documento", "Motivo", "Data Visita"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Documento", text="Documento")
tree.heading("Motivo", text="Motivo")
tree.heading("Data Visita", text="Data Visita")
tree.pack(pady=20)

listar_visitantes()

root.mainloop()
