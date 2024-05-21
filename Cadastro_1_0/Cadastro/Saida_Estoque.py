import tkinter
import customtkinter
import sqlite3
from tkinter import messagebox
from datetime import datetime

def centralizar_janela(janela):
    largura_janela = janela.winfo_reqwidth()
    altura_janela = janela.winfo_reqheight()

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    x = (largura_tela - largura_janela) // 2 
    y = (altura_tela - altura_janela) // 2

    janela.geometry(f"+{x}+{y}") 


def main():

    def cadastrar_saida():
        id_produto = entry_id.get()
        quantidade = entry_quantidade.get()
        data = entry_data.get()
        lucro = 0
        nova_quantidade = 0
        try:
            data = datetime.strptime(data, '%d/%m/%Y')
        except:
            return tkinter.messagebox.showerror(title="Aviso", message=f"A data inserida não está no formato correto!O formato é apenas números e barras,sendo dia/mês/ano.Exemplo:12/05/1999"),janela.focus_force()

        if quantidade.isnumeric() == False:
            return tkinter.messagebox.showerror(title="Aviso", message=f"A quantidade inserida não é um número!"),janela.focus_force()

        try:
            conn_produto = sqlite3.connect('produtos.db')
            cursor_produto = conn_produto.cursor()
            cursor_produto.execute("SELECT * FROM produtos WHERE id = ?", (id_produto,))
            produto = cursor_produto.fetchone()  
            lucro = float(quantidade)*float(produto[4])
            if int(quantidade)> int(produto[2]):
                return tkinter.messagebox.showerror(title="Aviso", message=f"A quantidade inserida é maior que a quantidade do estoque!"),janela.focus_force()

            nova_quantidade = int(produto[2]) - int(quantidade) 
            print(produto)
            cursor_produto.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", 
                        (nova_quantidade, id_produto))
            conn_produto.commit()
            print(produto)
            print(nova_quantidade,id_produto)
            
            conn_produto.close()
        except:
             return tkinter.messagebox.showerror(title="Aviso", message=f"Produto não encontrado!"),janela.focus_force()


        if id_produto =="" or quantidade == "" or data =="":
            return tkinter.messagebox.showerror(title="Aviso", message=f"Preencha todos os campos!"),janela.focus_force()
        conn = sqlite3.connect('estoque.db')
        cursor = conn.cursor()

        # Cria tabela de estoque
        cursor.execute('''CREATE TABLE IF NOT EXISTS estoque (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            operacao TEXT NOT NULL,
                            id_produto INTEGER NOT NULL,
                            quantidade INTEGER NOT NULL,
                            data TEXT NOT NULL,
                            custo FLOAT ,
                            lucro FLOAT 
                        )''')
        conn.commit()

        try:
            cursor.execute('''INSERT INTO estoque (operacao , id_produto , quantidade , data , lucro )
                        VALUES (? , ?, ?, ?, ?)''', ("saida" ,id_produto , quantidade, data , lucro))
            conn.commit()
            tkinter.messagebox.showinfo(title="Aviso", message=f"Saida cadastrada com sucesso!")
            conn.close()
        except:
            tkinter.messagebox.showerror(title="Aviso", message=f"Erro ao cadastrar a saida!")
            janela.focus_force()
            conn.close()

        
     #cria a janela de saida

    janela = tkinter.Tk()
    janela.geometry("450x125")
    janela.minsize(width=450, height=125)
    janela.maxsize(width=450, height=125)
    janela.title("Saida de estoque")
    janela.focus_force()
    #cria o frame de fundo da janela,usado para definir a cor de fundo
    frame = customtkinter.CTkFrame(master=janela,
                            width=1920,
                            height=1280,    
                            corner_radius=10,fg_color="black"
                            )
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    #label do id do produto
    label_nome = customtkinter.CTkLabel(master=janela,text="Id do produto:",fg_color="black",
                                        bg_color="black",text_color="white",width=150)
    label_nome.grid(padx=0.5, pady=0.5,row=1,column =1)

    #campo de entrada do id do produto
    entry_id = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_id.grid(row=1,column =2)

    #label da quantidade
    label_quantidade = customtkinter.CTkLabel(master=janela,text="Quantidade:",fg_color="black",
                                        bg_color="black",text_color="white",width=150)
    label_quantidade.grid(padx=0.5, pady=0.5,row=2,column =1)

    #campo de entrada da quantidade
    entry_quantidade = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_quantidade.grid(row=2,column =2)

    #label da data
    label_data = customtkinter.CTkLabel(master=janela,text="Data:",fg_color="black",
                                        bg_color="black",text_color="white",width=150)
    label_data.grid(padx=0.5, pady=0.5,row=3,column =1)

    #campo de entrada da data
    entry_data = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_data.grid(row=3,column =2)

#   botão para cadastro da saida
    button_cadastrar = customtkinter.CTkButton(master=janela,text="Cadastrar",bg_color="black",command = cadastrar_saida)
    button_cadastrar.grid(padx=0.5, pady=0.5,row=4,column =1,columnspan=2)

    janela.focus_force()
    centralizar_janela(janela)
    janela.mainloop()


if __name__ == "__main__":
    main()