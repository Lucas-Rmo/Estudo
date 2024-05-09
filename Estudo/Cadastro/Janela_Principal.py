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
    
    #cria a janela principal
    janela = tkinter.Tk()
    janela.geometry("325x125")
    janela.minsize(width=525, height=225)
    janela.maxsize(width=525, height=225)
    janela.title("Logado")

    #cria o frame de fundo da janela,usado para definir a cor de fundo
    frame = customtkinter.CTkFrame(master=janela,
                            width=1920,
                            height=1280,
                            corner_radius=10,fg_color="black"
                            )
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    button_cliente = customtkinter.CTkButton(master=janela,text="Cadastro de cliente",bg_color="black",width = 200 , height=40)
    button_cliente.grid(padx=0.5, pady=0.5,row=0,column =2)

    button_fornecedor = customtkinter.CTkButton(master=janela,text="Cadastro de fornecedor",bg_color="black",width = 200 , height=40)
    button_fornecedor.grid(padx=0.5, pady=0.5,row=1,column =2)

    button_produto = customtkinter.CTkButton(master=janela,text="Cadastro de produto",bg_color="black",width = 200 , height=40)
    button_produto.grid(padx=0.5, pady=0.5,row=2,column =2)

    centralizar_janela(janela)
    janela.mainloop()


if __name__ == "__main__":
    main()