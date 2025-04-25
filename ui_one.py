import tkinter as tk

def salvar_nome():
    nome = entry_nome.get()
    endereco = entry_endereco.get()
    if nome and endereco:
        with open("nomes-enderecos.txt", "a") as arquivo:
            arquivo.write(nome + "\n")
            arquivo.write(endereco + "\n")
        label_status.config(text=f'Nome "{nome}" e Endereço "{endereco}" salvos com sucesso!', fg="green")
    else:
        label_status.config(text="Digite os dados.", fg="red") 
root = tk.Tk()
root.title("Lista de nomes e endereços")
root.geometry("600x300")

label_instrucao = tk.Label(root, text="Digite um nome:")
label_instrucao.pack(pady=10)

entry_nome = tk.Entry(root)
entry_nome.pack(pady=5)

label_instrucao = tk.Label(root, text="Digite um endereço:")
label_instrucao.pack(pady=10)

entry_endereco = tk.Entry(root)
entry_endereco.pack(pady=5)

botao_salvar = tk.Button(root, text="Salvar", command=salvar_nome)
botao_salvar.pack(pady=10)

label_status = tk.Label(root, text="")
label_status.pack(pady=5)
root.mainloop()