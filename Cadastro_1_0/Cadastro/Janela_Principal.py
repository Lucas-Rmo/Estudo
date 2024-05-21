import tkinter
import customtkinter
import sqlite3
from tkinter import messagebox
import Cadastro_Clientes,Edit_Cliente,Exibir_Clientes
import Cadastro_Fornecedor,Edit_Fornecedor,Exibir_Fornecedores
import Cadastro_Produto,Edit_Produto,Exibir_Produtos
import Entrada_Estoque,Saida_Estoque,Exibir_Estoque

def centralizar_janela(janela):
    largura_janela = janela.winfo_reqwidth()
    altura_janela = janela.winfo_reqheight()

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    x = (largura_tela - largura_janela) // 2 - 100
    y = (altura_tela - altura_janela) // 3

    janela.geometry(f"+{x}+{y}")  


def main():

    #Botões dos clientes:
    def cadastro_de_cliente():
        return Cadastro_Clientes.main()
    
    def editar_cliente():
        return Edit_Cliente.main()
    
    def listar_clientes():
        return Exibir_Clientes.main()
    
    #Botões dos fornecedores:
    def cadastro_de_fornecedor():
        return Cadastro_Fornecedor.main()
    
    def editar_fornecedor():
        return Edit_Fornecedor.main()
    
    def listar_fornecedores():
        return Exibir_Fornecedores.main()
    
    #Botões dos produtos:
    def cadastro_de_produto():
        return Cadastro_Produto.main()
    def editar_produto():
        return Edit_Produto.main()
    def listar_produtos():
        return Exibir_Produtos.main()
    
    #parte do estoque:
    def entrada_de_estoque():
        return Entrada_Estoque.main()
    def saida_de_estoque():
        return Saida_Estoque.main()
    def historico_estoque():
        return Exibir_Estoque.main()
    

    #cria a janela principal
    janela = tkinter.Tk()
    janela.geometry("325x125")
    janela.minsize(width=410, height=525)
    janela.maxsize(width=410, height=525)
    janela.title("Logado")

    #cria o frame de fundo da janela,usado para definir a cor de fundo
    frame = customtkinter.CTkFrame(master=janela,
                            width=1920,
                            height=1280,
                            corner_radius=10,fg_color="black"
                            )
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    #Parte dos clientes na janela principal
    label_cliente = customtkinter.CTkLabel(master=janela,text="Clientes:",fg_color="black",
                                       bg_color="black",text_color="white",width=60)
    label_cliente.grid(padx=0.5, pady=0.5,row=2,column =0,columnspan=2)

    button_cad_cliente = customtkinter.CTkButton(master=janela,text="Cadastro de cliente",bg_color="black",width = 200 , height=40 , command=cadastro_de_cliente)
    button_cad_cliente.grid(padx=0.5, pady=0.5,row=3,column =0)

    button_edit_cliente = customtkinter.CTkButton(master=janela,text="Alteração de cliente",bg_color="black",width = 200 , height=40, command=editar_cliente)
    button_edit_cliente.grid(padx=0.5, pady=0.5,row=3,column =1)

    button_con_cliente = customtkinter.CTkButton(master=janela,text="Consulta de clientes",bg_color="black",width = 200 , height=40, command=listar_clientes)
    button_con_cliente.grid(padx=0.5, pady=0.5,row=4,column =0,columnspan=2)

    #Parte dos fornecedores:
    label_fornecedor = customtkinter.CTkLabel(master=janela,text="Fornecedores:",fg_color="black",
                                       bg_color="black",text_color="white",width=120)
    label_fornecedor.grid(padx=0.5, pady=0.5,row=5,column =0,columnspan=2)

    button_cad_fornecedor = customtkinter.CTkButton(master=janela,text="Cadastro de fornecedor",bg_color="black",width = 200 , height=40,command=cadastro_de_fornecedor)
    button_cad_fornecedor.grid(padx=0.5, pady=0.5,row=6,column =0)

    button_edit_fornecedor = customtkinter.CTkButton(master=janela,text="Alteração de fornecedor",bg_color="black",width = 200 , height=40,command=editar_fornecedor)
    button_edit_fornecedor.grid(padx=0.5, pady=0.5,row=6,column =1)

    button_con_fornecedor = customtkinter.CTkButton(master=janela,text="Consulta de fornecedores",bg_color="black",width = 200 , height=40,command=listar_fornecedores)
    button_con_fornecedor.grid(padx=0.5, pady=0.5,row=7,column =0,columnspan=2)

    #Parte dos produtos:
    label_produtos = customtkinter.CTkLabel(master=janela,text="Produtos:",fg_color="black",
                                       bg_color="black",text_color="white",width=120)
    label_produtos.grid(padx=0.5, pady=0.5,row=8,column =0,columnspan=2)

    button_cad_produto = customtkinter.CTkButton(master=janela,text="Cadastro de produto",bg_color="black",width = 200 , height=40,command = cadastro_de_produto)
    button_cad_produto.grid(padx=0.5, pady=0.5,row=9,column =0)

    button_edit_produto = customtkinter.CTkButton(master=janela,text="Alteração de produto",bg_color="black",width = 200 , height=40,command = editar_produto)
    button_edit_produto.grid(padx=0.5, pady=0.5,row=9,column =1)

    button_con_produto = customtkinter.CTkButton(master=janela,text="Consulta de produtos",bg_color="black",width = 200 , height=40,command = listar_produtos)
    button_con_produto.grid(padx=0.5, pady=0.5,row=10,column =0,columnspan=2)

    #parte do estoque
    label_estoque = customtkinter.CTkLabel(master=janela,text="Estoque:",fg_color="black",
                                       bg_color="black",text_color="white",width=120)
    label_estoque.grid(padx=0.5, pady=0.5,row=11,column =0,columnspan=2)

    button_entrada = customtkinter.CTkButton(master=janela,text="Entrada de estoque",bg_color="black",width = 200 , height=40,command = entrada_de_estoque)
    button_entrada.grid(padx=0.5, pady=0.5,row=12,column =0)

    button_saida = customtkinter.CTkButton(master=janela,text="Saida de estoque",bg_color="black",width = 200 , height=40,command = saida_de_estoque)
    button_saida.grid(padx=0.5, pady=0.5,row=12,column =1)

    button_historico = customtkinter.CTkButton(master=janela,text="Consulta do histórico",bg_color="black",width = 200 , height=40,command = historico_estoque)
    button_historico.grid(padx=0.5, pady=0.5,row=13,column =0,columnspan=2)

    centralizar_janela(janela)
    janela.mainloop()


if __name__ == "__main__":
    main()