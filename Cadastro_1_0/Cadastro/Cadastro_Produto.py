import tkinter
import customtkinter
import sqlite3
from tkinter import messagebox


def centralizar_janela(janela):
    largura_janela = janela.winfo_reqwidth()
    altura_janela = janela.winfo_reqheight()

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    x = (largura_tela - largura_janela) // 2 
    y = (altura_tela - altura_janela) // 2

    janela.geometry(f"+{x}+{y}") 


def main():

    
    def cadastrar_produto():
        nome = entry_nome.get()
        quantidade = entry_quantidade.get()
        preco_compra = entry_preco_compra.get()
        preco_venda = entry_preco_venda.get()
        id_fornecedor = entry_id_fornecedor.get()
        descricao = entry_descricao.get()

        preco_compra = preco_compra.replace(",",".")
        preco_venda = preco_venda.replace(",",".")
        
        if quantidade.isnumeric() == False:
            return tkinter.messagebox.showerror(title="Aviso", message=f"A quantidade inserida não é um número!"),janela.focus_force()
        
        if preco_compra.isnumeric() == False:
            return tkinter.messagebox.showerror(title="Aviso", message=f"O preço de compra inserido não é um número!"),janela.focus_force()
        
        if preco_venda.isnumeric() == False:
            return tkinter.messagebox.showerror(title="Aviso", message=f"O preço de venda inserido não é um número!"),janela.focus_force()
        
        if id_fornecedor.isnumeric() == False:
            return tkinter.messagebox.showerror(title="Aviso", message=f"O id do fornecedor inserido não é um número!"),janela.focus_force()
        
        conn_fornecedor = sqlite3.connect('fornecedores.db')
        cursor_fornecedor = conn_fornecedor.cursor()
        try:
            cursor_fornecedor.execute("SELECT * FROM fornecedores WHERE id = ?", (id_fornecedor,))
            fornecedor = cursor_fornecedor.fetchone()
            if fornecedor == None:
                return tkinter.messagebox.showerror(title="Aviso", message=f"Fornecedor não encontrado!"),janela.focus_force()
            print(fornecedor) 
        except:
            return tkinter.messagebox.showerror(title="Aviso", message=f"Fornecedor não encontrado!"),janela.focus_force()
        
        if nome =="" or quantidade == "" or preco_compra =="" or preco_venda=="" or id_fornecedor =="":
            return tkinter.messagebox.showerror(title="Aviso", message=f"Preencha todos os campos!"),janela.focus_force()
        conn = sqlite3.connect('produtos.db')
        cursor = conn.cursor()

        # Cria tabela de produtos
        cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            quantidade INTEGER NOT NULL,
                            precocompra FLOAT NOT NULL,
                            precovenda FLOAT NOT NULL,
                            id_fornecedor TEXT NOT NULL,
                            descricao TEXT
                        )''')
        conn.commit()

        try:
            cursor.execute('''INSERT INTO produtos (nome , quantidade , precocompra , precovenda , id_fornecedor , descricao)
                        VALUES (?, ?, ?, ?, ?, ?)''', (nome , quantidade, preco_compra , preco_venda , id_fornecedor , descricao))
            conn.commit()
            tkinter.messagebox.showinfo(title="Aviso", message=f"Produto cadastrado com sucesso!")
            conn.close()
        except:
            tkinter.messagebox.showerror(title="Aviso", message=f"Produto não localizado!")
            janela.focus_force()
            conn.close()

        
     #cria a janela de cadastro de produto

    janela = tkinter.Tk()
    janela.geometry("325x125")
    janela.minsize(width=450, height=225)
    janela.maxsize(width=450, height=225)
    janela.title("Cadastro de produto")
    janela.focus_force()
    #cria o frame de fundo da janela,usado para definir a cor de fundo
    frame = customtkinter.CTkFrame(master=janela,
                            width=1920,
                            height=1280,    
                            corner_radius=10,fg_color="black"
                            )
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    #label do nome
    label_nome = customtkinter.CTkLabel(master=janela,text="Nome:",fg_color="black",
                                        bg_color="black",text_color="white",width=150)
    label_nome.grid(padx=0.5, pady=0.5,row=1,column =1)

    #campo de entrada do nome
    entry_nome = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_nome.grid(row=1,column =2)

    #label da quantidade
    label_cpf = customtkinter.CTkLabel(master=janela,text="Quantidade:",fg_color="black",
                                        bg_color="black",text_color="white",width=150)
    label_cpf.grid(padx=0.5, pady=0.5,row=2,column =1)

    #campo de entrada da quantidade
    entry_quantidade = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_quantidade.grid(row=2,column =2)


    #label do preço de venda
    label_preco_venda = customtkinter.CTkLabel(master=janela,text="Preço de venda:",fg_color="black",
                                        bg_color="black",text_color="white",width=150)
    label_preco_venda.grid(padx=0.5, pady=0.5,row=3,column =1)

    #campo de entrada do preço de venda
    entry_preco_venda = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_preco_venda.grid(row=3,column =2)

    #label do preço de compra
    label_celular = customtkinter.CTkLabel(master=janela,text="Preço de compra:",fg_color="black",
                                        bg_color="black",text_color="white",width=150)
    label_celular.grid(padx=0.5, pady=0.5,row=4,column =1)

    #campo de entrada do preço de compra
    entry_preco_compra = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_preco_compra.grid(row=4,column =2)


    #label do id do fornecedor
    label_id_fornecedor = customtkinter.CTkLabel(master=janela,text="Id do Fornecedor:",fg_color="black",
                                        bg_color="black",text_color="white",width=150)
    label_id_fornecedor.grid(padx=0.5, pady=0.5,row=5,column =1)

    #campo de entrada do id do fornecedor
    entry_id_fornecedor = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_id_fornecedor.grid(row=5,column =2)

    #label da descrição
    label_descricao = customtkinter.CTkLabel(master=janela,text="Descrição:",fg_color="black",
                                        bg_color="black",text_color="white",width=150)
    label_descricao.grid(padx=0.5, pady=0.5,row=6,column =1)

    #campo de entrada da descrição
    entry_descricao = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_descricao.grid(row=6,column =2)


#   botão para cadastro de produto
    button_cadastrar = customtkinter.CTkButton(master=janela,text="Cadastrar",bg_color="black",command = cadastrar_produto)
    button_cadastrar.grid(padx=0.5, pady=0.5,row=7,column =1,columnspan=2)
    janela.focus_force()
    centralizar_janela(janela)
    janela.mainloop()


if __name__ == "__main__":
    main()