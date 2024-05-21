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

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def main():
    
    def buscar_produto():
        # Conectar ao banco de dados
        conn = sqlite3.connect('produtos.db')
        cursor = conn.cursor()

        produto_id = entry_id.get()
        # Consultar o banco de dados para obter os dados do produto
        cursor.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,))
        # Retorna uma tupla com os dados do produto
        produto = cursor.fetchone()  

        # Preenche os campos da tela com os dados do produto, se encontrado
        if produto:
            
            entry_nome.delete(0,tkinter.END)
            entry_quantidade.delete(0,tkinter.END)
            entry_preco_compra.delete(0,tkinter.END)
            entry_preco_venda.delete(0,tkinter.END)
            entry_id_fornecedor.delete(0,tkinter.END)
            entry_descricao.delete(0,tkinter.END)

            entry_nome.insert(0,str(produto[1]))
            entry_quantidade.insert(0,str(produto[2]))
            entry_preco_compra.insert(0,str(produto[3]))
            entry_preco_venda.insert(0,str(produto[4]))
            entry_id_fornecedor.insert(0,str(produto[5]))
            entry_descricao.insert(0,str(produto[6]))
            

        else:
            # Se o produto não for encontrado, limpa os campos
            entry_nome.delete(0,tkinter.END)
            entry_quantidade.delete(0,tkinter.END)
            entry_preco_compra.delete(0,tkinter.END)
            entry_preco_venda.delete(0,tkinter.END)
            entry_id_fornecedor.delete(0,tkinter.END)
            entry_descricao.delete(0,tkinter.END)
            tkinter.messagebox.showerror(title="Atenção!", message=f"Id não encontrado!")
            janela.focus_force()
        # Fecha a conexão com o banco de dados
        conn.close()
    
    def alterar_produto():

        #conecta no banco de dados
        conn = sqlite3.connect('produtos.db')
        cursor = conn.cursor()

        # Obter os novos valores dos campos de entrada e o ID
        produto_id = entry_id.get()

        novo_nome = entry_nome.get()
        nova_quantidade = entry_quantidade.get()
        novo_preco_compra = entry_preco_compra.get()
        novo_preco_venda = entry_preco_venda.get()
        novo_id_fornecedor = entry_id_fornecedor.get()
        nova_descricao = entry_descricao.get()
        novo_preco_compra = novo_preco_compra.replace(",",".")
        novo_preco_venda = novo_preco_venda.replace(",",".")
        
        if nova_quantidade.isnumeric() == False:
            return tkinter.messagebox.showerror(title="Aviso", message=f"A quantidade inserida não é um número inteiro!"),janela.focus_force()
        
        if novo_preco_compra.isnumeric() == False and is_float(novo_preco_compra)==False:
            return tkinter.messagebox.showerror(title="Aviso", message=f"O preço de compra inserido não é um número válido!"),janela.focus_force()
        
        if novo_preco_venda.isnumeric() == False and is_float(novo_preco_venda)==False:
            return tkinter.messagebox.showerror(title="Aviso", message=f"O preço de venda inserido não é um número válido!"),janela.focus_force()
        
        if novo_id_fornecedor.isnumeric() == False:
            return tkinter.messagebox.showerror(title="Aviso", message=f"O id do fornecedor inserido não é um número!"),janela.focus_force()
        
        conn_fornecedor = sqlite3.connect('fornecedores.db')
        cursor_fornecedor = conn_fornecedor.cursor()
        try:
            cursor_fornecedor.execute("SELECT * FROM fornecedores WHERE id = ?", (novo_id_fornecedor,))
            fornecedor = cursor_fornecedor.fetchone()
            if fornecedor == None:
                return tkinter.messagebox.showerror(title="Aviso", message=f"Fornecedor não encontrado!"),janela.focus_force()
            
        except:
            return tkinter.messagebox.showerror(title="Aviso", message=f"Fornecedor não encontrado!"),janela.focus_force()


         # Executar a instrução SQL UPDATE
        cursor.execute("UPDATE produtos SET nome = ?, quantidade = ? , precocompra = ? , precovenda = ? , id_fornecedor = ? , descricao = ? WHERE id = ?", 
                    (novo_nome, nova_quantidade, novo_preco_compra, novo_preco_venda, novo_id_fornecedor,nova_descricao,produto_id))

        conn.commit()
        conn.close()
        tkinter.messagebox.showinfo(title="Sucesso!", message=f"Dados alterados com sucesso!")
        entry_nome.delete(0,tkinter.END)
        entry_quantidade.delete(0,tkinter.END)
        entry_preco_compra.delete(0,tkinter.END)
        entry_preco_venda.delete(0,tkinter.END)
        entry_id_fornecedor.delete(0,tkinter.END)
        entry_descricao.delete(0,tkinter.END)


    #cria a janela principal
    janela = tkinter.Tk()
    janela.geometry("410x275")
    janela.minsize(width=410, height=275)
    janela.maxsize(width=410, height=275)
    janela.title("Alteração de Produto")



    #cria o frame de fundo da janela,usado para definir a cor de fundo
    frame = customtkinter.CTkFrame(master=janela,
                            width=1920,
                            height=1280,
                            corner_radius=10,fg_color="black"
                            )
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    label_id_produto = customtkinter.CTkLabel(master=janela,text="Id do Produto:",fg_color="black",
                                       bg_color="black",text_color="white",width=100)
    label_id_produto.grid(padx=0.5, pady=0.5,row=0,column =0)

    entry_id = customtkinter.CTkEntry(master=janela,
                            width=250,
                            height=25,
                            corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_id.grid(row=0,column =1)

    button_id = customtkinter.CTkButton(master=janela,text="Buscar id",bg_color="black",command=buscar_produto)
    button_id.grid(padx=0.5, pady=0.5,row=1,column =0,columnspan=2)
    
    #label do nome
    label_nome = customtkinter.CTkLabel(master=janela,text="Nome:",fg_color="black",
                                        bg_color="black",text_color="white",width=150)
    label_nome.grid(padx=0.5, pady=0.5,row=2,column =0)

    #campo de entrada do nome
    entry_nome = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_nome.grid(row=2,column =1)
    

    #label da quantidade
    label_quantidade = customtkinter.CTkLabel(master=janela,text="Quantidade:",fg_color="black",
                                        bg_color="black",text_color="white",width=150)
    label_quantidade.grid(padx=0.5, pady=0.5,row=3,column =0)

    #campo de entrada da quantidade
    entry_quantidade = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_quantidade.grid(row=3,column =1)


    #label do preço de compra
    label_preco_compra = customtkinter.CTkLabel(master=janela,text="Preço de compra:",fg_color="black",
                                        bg_color="black",text_color="white",width=150)
    label_preco_compra.grid(padx=0.5, pady=0.5,row=4,column =0)

    #campo de entrada do preço de compra
    entry_preco_compra = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_preco_compra.grid(row=4,column =1)

    #label do preço de venda
    label_preco_venda = customtkinter.CTkLabel(master=janela,text="Preço de venda:",fg_color="black",
                                        bg_color="black",text_color="white",width=150)
    label_preco_venda.grid(padx=0.5, pady=0.5,row=5,column =0)

    #campo de entrada do celular
    entry_preco_venda = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_preco_venda.grid(row=5,column =1)


    #label do id do fornecedor
    label_id_fornecedor = customtkinter.CTkLabel(master=janela,text="Id do fornecedor:",fg_color="black",
                                        bg_color="black",text_color="white",width=150)
    label_id_fornecedor.grid(padx=0.5, pady=0.5,row=6,column =0)

    #campo de entrada do id do fornecedor
    entry_id_fornecedor = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_id_fornecedor.grid(row=6,column =1)

    #label do id da descrição
    label_descricao = customtkinter.CTkLabel(master=janela,text="Descrição:",fg_color="black",
                                        bg_color="black",text_color="white",width=150)
    label_descricao.grid(padx=0.5, pady=0.5,row=7,column =0)

    #campo de entrada da descrição
    entry_descricao = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_descricao.grid(row=7,column =1)

#   botão para alteração do produto
    button_cadastrar = customtkinter.CTkButton(master=janela,text="Alterar",bg_color="black",command=alterar_produto)
    button_cadastrar.grid(padx=0.5, pady=0.5,row=8,column =0,columnspan=2)


    centralizar_janela(janela)
    janela.mainloop()


if __name__ =="__main__":
    main()